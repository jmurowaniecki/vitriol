# ![V·I·T·R·I·O·L][vitriol.png] <img align="right" src="https://img.shields.io/github/v/tag/jmurowaniecki/vitriol?sort=semver&style=flat-square" />

![Leiaute de teclas mapeadas][keyboard.png]

<!--
@TODO: Review install process.
![](https://img.shields.io/badge/ubuntu-building-green?style=for-the-badge&logo=ubuntu)
![](https://img.shields.io/badge/arch-building-green?style=for-the-badge&logo=arch-linux)
![](https://img.shields.io/badge/debian-building-green?style=for-the-badge&logo=debian)
![](https://img.shields.io/badge/slackware-building-green?style=for-the-badge&logo=slackware)
![](https://img.shields.io/badge/linuxmint-failure-red?style=for-the-badge&logo=linuxmint)
![](https://img.shields.io/badge/popOS-failure-red?style=for-the-badge&logo=popOS)
-->

**V.I.T.R.I.O.L.¹** é um mapeamento simbólico para layouts de teclados baseados em sistemas X11 para todos aqueles que necessitam de caracteres com simbologia astronômica, astrológica, alquímica, matemática e/ou de **diversidade gênero e simbologia juvélica**².

Esta biblioteca visa contribuir com recursos de fácil e rápido acesso para os estudos e publicações, não apenas dos casos citados acima citados. se você necessitar de um mapeamento específico e/ou tiver alguma ideia, dúvida, crítica ou sugestão sinta-se a vontade para contatar e/ou abrir uma issue, pull request ou até mesmo realizar um fork deste projeto.


> ¹ : Significa literalmente _"Visita Interiora Terrae, Rectificando, Invenies Occultum Lapidem."_

> ² : Não está completo, mas já é um _work-in-progress_.



## Requisitos

Certifique-se de que seu sistema está com o pacote `unicode` (da seção `utils`) e `ttf-ancient-fonts` instalado e atualizado.

```sh
# Ubuntu
sudo apt update && sudo apt install unicode ttf-ancient-fonts

# Arch
yay -Syu unicode-emoji

# Alpine
apk add unicode-character-database
```



## Instalação

Adicione o conteúdo do arquivo `evdev.lst` à seção `! variant` do arquivo `/usr/share/X11/xkb/rules/evdev.lst`, e ao `evdev.xml` para sua `variantList` correspondente na seção **BR** do arquivo `/usr/share/X11/xkb/rules/evdev.xml`.

Então finalmente adicione o arquivo `vitriol.xkb` ao seu arquivo de símbolos `/usr/share/X11/xkb/symbols/br`.

Após realizar a instalação é necessário reiniciar sua sessão X11 (fazer logout).

> Você também pode realizar esses procedimentos de forma automática com o comando `make install`.



## Primeiros passos

1.  Realize a instalação utilizando os passo do **Makefile**: `make install`;
2.  Abra as configurações do seu sistema e vá para **`Linguagem / Configuração de teclados`**;
3.  Selecione o mapeamento **Portuguese (Brazil, Esoteric)** desejado;
4.  Para testar pressione **` Alt Gr. `** + **` X `** para imprimir o caractere ' **` 🜏 `** '.

>  Saiba que eventuais atualizações do sistema sobreescreverão suas configurações, sendo necessário eventualmente repetir o processo de instalação após a atualização do sistema.

## Mapeamentos

Devido a necessidade constante de utilização dos símbolos esotéricos, astrológicos e juvélicos, bem como a extensão dos símbolos em uso, tornou-se necessário subdividir em mapeamentos individuais para atender as necessidades simbólicas dos trabalhos realizados.

> Se você e interessa em teclas customizadas e/ou impressas dê uma [olhada aqui][max-keyboard-url].
\
\
> Se você quer fazer um teclado customizado utilizando Arduino [isso aqui pode te ajudar][diy-with-arduino].
\
\
> Devido a erros renderizando os caracteres _Level 3, Super_ ou _Meta_ utilizando o programa `draw-key` de [gkbd-keyboard-drawing](https://github.com/GNOME/libgnomekbd/blob/master/libgnomekbd/gkbd-keyboard-drawing.c) algumas teclas e seus valores podem ter sido renderizadas e posicionadas manualmente no teclado de exemplo.


- [TERMOS-JUVELICOS.md](doc/TERMOS-JUVELICOS.md)


> Fontes e artigos:
[O que voce precisa saber sobre o i em lgbti no dia da visibilidade intersexual](https://www.grupodignidade.org.br/intersex-o-que-voce-precisa-saber-sobre-o-i-em-lgbti-no-dia-da-visibilidade-intersexual/),
[Categorias relacionadas a genero](https://orientando.org/categorias-relacionadas-a-genero/) e
[Gender symbols](http://www.cakeworld.info/transsexualism/gender-symbols).

> O layout QWERTY foi projetado no século XIX. O Colemak é uma alternativa moderna aos layouts QWERTY e Dvorak, projetado para digitação por toque eficiente e ergonômica em inglês. [Veja mais sobre…](https://colemak.com/)



[](ASSETS)

[ico-version]: https://img.shields.io/github/v/tag/jmurowaniecki/vitriol?sort=semver&style=flat-square
[vitriol.png]: ./doc/assets/vitriol.png
[keyboard.png]: ./doc/assets/layout.png
[max-keyboard-url]: https://www.maxkeyboard.com/
[diy-with-arduino]: https://www.makeuseof.com/tag/make-custom-shortcut-buttons-arduino/
[TODO]: https://img.shields.io/badge/atalho_de_teclas_-indefinido-violet?style=flat-square