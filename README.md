# Esoteric keyboard layout

![Keyboard mapping][keyboard.png]

[![StyleCI    ][ico-styleci]][url-styleci]
[![Codacy     ][ico-codacy ]][url-codacy]
[![Codeclimate][ico-codecli]][url-codecli]
[![Version    ][ico-version]](#)

**V.I.T.R.I.O.L.¹** is an esoteric keyboard layout for those who need to use characters with astronomical, astrological, alchemical and mathematical meanings.

> ¹ : _"Visita Interiora Terrae, Rectificando, Invenies Occultum Lapidem."_



## Installation

Append contents from `evdev.lst` to `! variant` section of `/usr/share/X11/xkb/rules/evdev.lst`, and `evdev.xml` to it's correspondent `variantList` of  **BR** section from `/usr/share/X11/xkb/rules/evdev.xml`.

Then finally append `vitriol.xkb` to `/usr/share/X11/xkb/symbols/br` file.

> Also you can perform installation with `make install`.



## Basic usage steps

1.  Installs using **Makefile**;
2.  Open your system configurations and goto Language/keyboard definitions;
3.  Change your keyboard mapping to **Portuguese (Brazil, Esoteric)**;
4.  Press **Alt Gr.** + **Shift** + **;** to print **∴**



[](ASSETS)

[ico-codacy ]: https://img.shields.io/codacy/grade/b002e2f9f0ad4ffb9ec5676789918b61?logo=codacy&logoColor=green&style=flat-square
[ico-styleci]: https://github.styleci.io/repos/278512720/shield?branch=master
[ico-version]: https://img.shields.io/github/v/tag/jmurowaniecki/vitriol?sort=semver&style=flat-square
[ico-codecli]: https://api.codeclimate.com/v1/badges/bb01325f8a84fc9fba31/maintainability
[url-codacy ]: https://www.codacy.com/app/jmurowaniecki/vitriol
[url-styleci]: https://github.styleci.io/repos/278512720
[url-codecli]: https://codeclimate.com/github/jmurowaniecki/vitriol/maintainability

[keyboard.png]: ./doc/assets/keyboard.png
