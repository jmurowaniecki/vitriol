#!/usr/bin/env python3

"""Installer for VITRIOL keyboard layout.

Author....: John Murowaniecki
Repository: https://github.com/jmurowaniecki/vitriol
"""

import xml.etree.ElementTree as ET
import xml.dom.minidom
import argparse
import os
import re


class Application:
    """Installer for VITRIOL keyboard layout.

    Raises:
        NotADirectoryError: Informs that the target directory doesn't exist.
    """
    Name          = "V.I.T.R.I.O.L."
    Description   = "Keyboard mapping installer."
    Documentation = "For more information see https://github.com/jmurowaniecki/vitriol"



    def __init__(self):
        """Installer constructor.
        """
        self.parser = argparse.ArgumentParser(
            description=(f"\033[1;32m{Application.Name}\033[0m - {Application.Description}"),
            epilog=Application.Documentation,
        )

        self.parser.add_argument(
            "action",
            nargs="?",
            default="check",
            help="Action to be performed.",
            choices=["check", "install", "update", "uninstall", "help"],
        )

        self.parser.add_argument(
            "-T",
            "--target",
            default="/usr/share/X11/xkb",
            type=self.isValidTargetDirectory,
            help="Target folder to install artefacts.",
        )

        self.parser.add_argument(
            "-V",
            "--verbose",
            default=False,
            action='store_true',
            help="Output verbosity.",
        )

        self.parser.add_argument(
            "-F",
            "--force",
            default=False,
            action='store_true',
            help="Force install/update.",
        )

        self.variants = [
            "vitrioles",
            "vitriolas",
            "vitriolic",
            "vitriolma",
        ]
        self.source = {
            "evdev.lst": { "from": "rules/evdev",    "to": "rules/evdev", "ext": ".lst", "marks": [ "vitriol"                       ], "checked": False, "exec": self.installerLST    },
            "evdev.xml": { "from": "rules/evdev",    "to": "rules/evdev", "ext": ".xml", "marks": [ "<name>vitrioles</name>"        ], "checked": False, "exec": self.installerXML    },
            "base.lst":  { "from": "rules/evdev",    "to": "rules/base",  "ext": ".lst", "marks": [ "vitriol"                       ], "checked": False, "exec": self.installerLST    },
            "base.xml":  { "from": "rules/evdev",    "to": "rules/base",  "ext": ".xml", "marks": [ "<name>vitrioles</name>"        ], "checked": False, "exec": self.installerXML    },
            "symbol.br": { "from": "symbols/br.xkb", "to": "symbols/br",  "ext": "",     "marks": [ "// <vitriol>", "// </vitriol>" ], "checked": False, "exec": self.installerSymbol },
        }
        self.args = self.parser.parse_args()
        {
            "help"     : self.help,
            "check"    : self.check,
            "update"   : self.update,
            "install"  : self.install,
            "uninstall": self.uninstall,
        }[self.args.action]()



    @staticmethod
    def read(file, mode="rt"):
        """Open file for reading only.
        """
        opens = open(file, mode, encoding="utf-8")
        lines = opens.readlines()
        opens.close()
        return lines



    @staticmethod
    def isValidTargetDirectory(string):
        """Check if target directory is valid.
        """
        if os.path.isdir(string):
            return string if string[-1] != "/" else string[:-1]

        raise NotADirectoryError(f"{string} is NOT a valid target directory.")



    def help(self):
        """Method: help - Shows standard help for arguments parsed.
        """
        self.parser.print_help()



    def installerSymbol(self, target, fragment):
        """Installer for Symbol/XKB file.
        """
        if not [line for line in open(target, encoding="utf-8") if re.search("^.*vitriol.*$", line)]:
            if self.simulate:
                print(f"- {target} not installed.")
                return

            orig = self.read(fragment)
            file = self.read(target)

            dest = open(target, "w", encoding="utf-8")
            dest.writelines(file)
            dest.writelines(orig)
            dest.close()

        print("- Symbol files installed.")



    def installerLST(self, target, fragment):
        """Installer for LST files.
        """
        if not [line for line in open(target, encoding="utf-8") if re.search("^.*vitriol.*$", line)]:
            if self.simulate:
                print(f"- {target} not installed.")
                return

            orig = self.read(fragment)
            file = self.read(target)
            if not self.source["evdev.lst"]["marks"][0] in file:
                regExprComp = re.compile(r'^.*nativo .* br: Portuguese \(Brazil,.*$')
                for line in file:
                    found = regExprComp.search(line)
                    if found:
                        file.insert(file.index(line), ''.join(orig))
                        break

                open(target, "w", encoding="utf-8").writelines(file)

        print("- LST files installed.")



    def installerXML(self, target, fragment):
        """Installer for XML files.
        """
        found = [line for line in open(target, encoding="utf-8") if re.search("^.*vitriol.*$", line)]
        if self.force or not found:
            if self.simulate:
                print(f"- {target} not installed.")
                return

            orig = self.getSymbols(target)
            tree = ET.parse(target)
            root = tree.getroot()

            for model_list in root.findall(".//name/[.='br']../..variantList"):
                model_list.clear()
                model_list.insert(0, orig)

            tree.write(target)

        print("- XML files installed.")



    def getSource(self, source, default_path = "install/"):
        """Decode source path.
        """
        (name, rules) = source
        if self.verbose:
            print(f"Name and rules: {name} {rules}.")

        # return "%s%s%s" % (default_path, self.source[source]['from'], self.source[source]['ext'])
        return f"{default_path}{rules['from']}{rules['ext']}"



    def getTarget(self, target):
        """Decode target path.
        """
        (name, rules) = target
        if self.verbose:
            print(f"Name and rules: {name} {rules}.")
        return f"{self.args.target}/{rules['to']}{rules['ext']}"

    def getSymbols(self, target):
        symbols = f"{self.args.target}/{self.source['symbol.br']['to']}"
        updates = f"install/{self.source['symbol.br']['from']}"
        content = open(symbols, encoding="utf-8").read()
        content+= open(updates, encoding="utf-8").read()
        # content = re.sub(r'// <vitriol>.*?// </vitriol>', '', content, flags=re.DOTALL)
        pattern = r'xkb_symbols\s+"([^"]+)"\s*\{[^}]*?name\[Group1\]="([^"]+)"'
        matches = re.findall(pattern, content)
        results = [{"name": name, "description": description} for name, description in matches]

        variants = ET.Element("variants")

        for item in results:
            variant = ET.SubElement(variants, "variant")
            xmlNode = ET.SubElement(variant, "configItem")
            name    = ET.SubElement(xmlNode, "name")
            name.text = item["name"]
            description = ET.SubElement(xmlNode, "description")
            description.text = item["description"]

        xml_string = ET.tostring(variants, encoding="unicode")
        return xml_string



    simulate = False
    verbose  = False
    force    = False



    def check(self):
        """Method: check - Only check for files having signatures.
        """
        self.simulate = True
        self.verbose  = False
        self.force    = False
        self.install()



    def install(self):
        """Method: install - Perform installation procedures.
        """
        for target in self.source.items():
            origins = self.getSource(target)
            destiny = self.getTarget(target)
            (source, rules) = target
            if self.verbose:
                print(f"Source name and rules: {source} {rules}.")
            self.source[source]["exec"](destiny, origins)



    def update(self):
        """Method: update - Perform update procedures.
        """
        print("Update method not implemented.")
        self.help()



    def uninstall(self):
        """Method: uninstall - Perform uninstall procedures.
        """
        print("Uninstall method not implemented.")
        self.help()



if __name__ == "__main__":
    Application()
