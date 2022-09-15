#!/usr/bin/env python3

"""Installer for VITRIOL keyboard layout.

Author....: John Murowaniecki
Repository: https://github.com/jmurowaniecki/vitriol
"""

import xml.etree.ElementTree as ET
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
            default="/usr/share/X11/xkb/rules",
            type=self.isValidTargetDirectory,
            help="Target folder to install artefacts.",
        )

        self.source = {
            "evdev.lst": { "from": "rules/evdev",         "to": "rules/evdev", "ext": ".lst", "marks": [ "vitriol" ],                       "checked": False, "exec": self.installerLST },
            "evdev.xml": { "from": "rules/evdev",         "to": "rules/evdev", "ext": ".xml", "marks": [ "<name>vitriol</name>" ],          "checked": False, "exec": self.installerXML },
            "base.lst":  { "from": "rules/evdev",         "to": "rules/base",  "ext": ".lst", "marks": [ "vitriol" ],                       "checked": False, "exec": self.installerLST },
            "base.xml":  { "from": "rules/evdev",         "to": "rules/base",  "ext": ".xml", "marks": [ "<name>vitriol</name>" ],          "checked": False, "exec": self.installerXML },
            "symbol.br": { "from": "symbols/vitriol.xkb", "to": "symbols/br",  "ext": "",     "marks": [ "// <vitriol>", "// </vitriol>" ], "checked": False, "exec": self.installerSymbol },
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
                for line in file:
                    found = re.search("^.*nativo .* br: Portuguese \(Brazil,.*$", line)
                    if found:
                        file.insert(file.index(line), orig[0])
                        print (file[file.index(line) - 5: file.index(line) + 5])
                        break
                open(target, "w", encoding="utf-8").writelines(file)

        print("- LST files installed.")



    def installerXML(self, target, fragment):
        """Installer for XML files.
        """
        if not [line for line in open(target, encoding="utf-8") if re.search("^.*vitriol.*$", line)]:
            if self.simulate:
                print(f"- {target} not installed.")
                return

            orig = ET.parse(fragment)
            tree = ET.parse(target)
            root = tree.getroot()

            for model_list in root.findall(".//name/[.='br']../..variantList"):
                model_list.insert(0, orig.getroot())

            tree.write(target)

        print("- XML files installed.")



    def getSource(self, source, default_path = "install/"):
        """Decode source path.
        """
        (name, rules) = source
        # return "%s%s%s" % (default_path, self.source[source]['from'], self.source[source]['ext'])
        return f"{default_path}{rules['from']}{rules['ext']}"



    def getTarget(self, target):
        """Decode target path.
        """
        (name, rules) = target
        return f"{self.args.target}/{rules['to']}{rules['ext']}"



    simulate = False



    def check(self):
        """Method: check - Only check for files having signatures.
        """
        self.simulate = True
        self.install()



    def install(self):
        """Method: install - Perform installation procedures.
        """
        for target in self.source.items():
            origins = self.getSource(target)
            destiny = self.getTarget(target)
            (source, rules) = target
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
