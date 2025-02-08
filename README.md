# ![V·I·T·R·I·O·L][vitriol.png] <img align="right" src="https://img.shields.io/github/v/tag/jmurowaniecki/vitriol?sort=semver&style=flat-square" />

![Mapped key layout][keyboard.png]
<!-- by Ioxn Ioannes Vicarius Umbrae. -->


**V.I.T.R.I.O.L.¹** is a symbolic mapping for X11-based keyboard layouts for all those who need characters with astronomical, astrological, alchemical, mathematical and/or gender-diverse symbology and **Juvelic symbology²**.

This library aims to contribute with easy and quick access resources for studies and publications, not only for the cases mentioned above.

If you need a specific mapping and/or have any ideas, questions, criticisms or suggestions, feel free to contact us and/or open an issue, pull request or even fork this project.

> ¹ : It literally means _"Visita Interiora Terrae, Rectificando, Invenies Occultum Lapidem."_

> ² : It's not complete (yet), but it's a work-in-progress.



## Requirements

Make sure your system has the `unicode` package (from the `utils` section) and `ttf-ancient-fonts` and Python v3 installed and up to date.

```sh
# Ubuntu
sudo apt update && \
sudo apt install unicode ttf-ancient-fonts python3

# Arch
yay -Syu unicode-emoji python3

# Alpine
apk add unicode-character-database python3
```


## Installation

The automated installation process can be performed using the `make install` commands or by running the `install.py` file.


## Manual Installation

Add the contents of the `evdev.lst` file to the `!variant` section of the `/usr/share/X11/xkb/rules/evdev.lst` file, and to `evdev.xml` for its corresponding `variantList` in the **BR** section of the `/usr/share/X11/xkb/rules/evdev.xml` file.

Then finally add the `vitriol.xkb` file to your symbols file `/usr/share/X11/xkb/symbols/br`.

After performing the installation you need to restart your X11 session (log out).


## Getting Started

1. Perform the installation using the steps in the **Makefile**: `make install`;
2. Open your system settings and go to **`Language / Keyboard settings`**;
3. Select the desired **Portuguese (Brazil, Esoteric)** mapping;
4. To test, press **` Alt Gr. `** + **` X `** to print the character ' **` 🜏 `** '.

> Be aware that any system updates will overwrite your settings, and you may need to repeat the installation process after updating the system.

## Mappings

Due to the constant need to use esoteric, astrological and Juvelic symbols, as well as the extension of the symbols in use, it became necessary to subdivide into individual mappings to meet the symbolic needs of the work carried out.

> If you are interested in custom and/or printed keys take a [look here][max-keyboard-url].

> If you want to make a custom keyboard using Arduino [this can help you][diy-with-arduino].

> Due to errors rendering the _Level 3_, _Super_ or _Meta_ characters using the `draw-key` program from [gkbd-keyboard-drawing](https://github.com/GNOME/libgnomekbd/blob/master/libgnomekbd/gkbd-keyboard-drawing.c) some keys and their values ​​may have been rendered and positioned manually on the example keyboard.

> [See the table of Juvelic terms - WIP](doc/TERMOS-JUVELICOS.md)

> The QWERTY layout was designed in the 19th century. Colemak is a modern alternative to the QWERTY and Dvorak layouts, designed for efficient and ergonomic touch typing in English. [Learn more about…](https://colemak.com/)

> [See more about the XKB protocol.](https://www.x.org/releases/X11R7.7/doc/kbproto/xkbproto.html)

> Future reference https://shapecatcher.com/unicode/block/Gothic

[](ASSETS)

[ico-version     ]: https://img.shields.io/github/v/tag/jmurowaniecki/vitriol?sort=semver&style=flat-square
[vitriol.png     ]: ./doc/assets/vitriol.png
[keyboard.png    ]: ./doc/assets/layout.png
[max-keyboard-url]: https://www.maxkeyboard.com/
[diy-with-arduino]: https://www.makeuseof.com/tag/make-custom-shortcut-buttons-arduino/
[TODO            ]: https://img.shields.io/badge/atalho_de_teclas_-indefinido-violet?style=flat-square
