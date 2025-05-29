# ![V·I·T·R·I·O·L][vitriol.png]
<img align="right" src="https://img.shields.io/github/v/tag/jmurowaniecki/vitriol?sort=semver&style=flat-square" />

<!-- by Ioxn Ioannes Vicarius Umbrae. -->

**V.I.T.R.I.O.L.¹** é um mapeamento simbólico para layouts de teclado baseados em X11 para todos aqueles que precisam de caracteres com simbologia astronômica, astrológica, alquímica, matemática e/ou de gênero diverso - **simbologia Juvélica²**.

Esta biblioteca visa contribuir com recursos de fácil e rápido acesso para estudos e publicações, não apenas para os casos mencionados acima. Se você precisar de um mapeamento específico e/ou tiver alguma ideia, dúvida, crítica ou sugestão, sinta-se à vontade para entrar em contato conosco e/ou abrir uma issue, pull request ou até mesmo fazer um fork deste projeto.

<small>
  ¹ : Significa literalmente <i><b>"Visita Interiora Terrae, Rectificando, Invenies Occultum Lapidem."</b> - visite o centro da Terra, retificando-se, você encontrará a pedra escondida</i>.

  ² : Não está completo (ainda), mas é um trabalho em andamento.
</small>



## Requisitos
Certifique-se de que seu sistema tenha o pacote `unicode` (da seção `utils`), `ttf-ancient-fonts` e Python v3 instalados e atualizados.

```sh
# Ubuntu
sudo apt update && \
sudo apt install unicode ttf-ancient-fonts python3

# Arch
yay -Syu unicode-emoji python3

# Alpine
apk add unicode-character-database python3
```


## Instalação

O processo de instalação automatizada pode ser executado usando os comandos `make install` ou executando o arquivo `install.py`. Certifique-se de ter os privilégios para alterar os arquivos de sistema (ou utilizar `sudo` para esse fim).


## Instalação Manual

Adicione o conteúdo do arquivo `evdev.lst` à seção `!variant` do arquivo `/usr/share/X11/xkb/rules/evdev.lst` e ao arquivo `evdev.xml` para a sua `variantList` correspondente na seção **BR** do arquivo `/usr/share/X11/xkb/rules/evdev.xml`.

Por fim, adicione o arquivo `install/symbols/br.xkb` (ou algum dos layouts específicos) ao seu arquivo de símbolos `/usr/share/X11/xkb/symbols/br`.

Após realizar a instalação, você **precisa** reiniciar sua sessão X11.


## Primeiros Passos

1. Execute a instalação seguindo os passos do **Makefile**: `make install`;
2. Abra as configurações do sistema e vá em **`Idioma / Configurações de Teclado`**;
3. Selecione o mapeamento **Português (Brasil, Esotérico)** desejado;
4. Para testar, pressione **` Alt Gr. `** + **` X `** para imprimir o caractere ' **` 🜏 `** '.

> Esteja ciente de que qualquer atualização do sistema poderá substituir suas configurações e que talvez seja necessário repetir o processo de instalação após atualizar o sistema.

## Mapeamentos

Devido à constante necessidade de utilização de símbolos esotéricos, astrológicos e juvélicos, bem como à extensão dos símbolos em uso, tornou-se necessário subdividir em mapeamentos individuais para atender às necessidades simbólicas do trabalho realizado.

### Layout Esotérico
![Mapped key layout][kbd-vitriol-es]

### Layout Matemático
![Mapped key layout][kbd-vitriol-ma]

### Layout Juvélico
![Mapped key layout][kbd-vitriol-ic]

### Layout Astrológico
![Mapped key layout][kbd-vitriol-as]


> Se você estiver interessado em teclas personalizadas e/ou impressas, dê uma olhada em [veja aqui][max-keyboard-url].

> Se você quiser criar um teclado personalizado usando Arduino [isso pode te ajudar][diy-with-arduino].

> Devido a erros na renderização dos caracteres _Level 3_, _Super_ ou _Meta_ usando o programa `draw-key` do [gkbd-keyboard-drawing](https://github.com/GNOME/libgnomekbd/blob/master/libgnomekbd/gkbd-keyboard-drawing.c), algumas teclas e seus valores podem ter sido renderizados e posicionados manualmente no teclado de exemplo.

> [Veja a tabela de termos Juvelic - WIP](doc/TERMOS-JUVELICOS.md)

> O layout QWERTY foi projetado no século XIX. Colemak é uma alternativa moderna aos layouts QWERTY e Dvorak, projetada para digitação eficiente e ergonômica em inglês. [Saiba mais sobre…](https://colemak.com/)

> [Saiba mais sobre o protocolo XKB.](https://www.x.org/releases/X11R7.7/doc/kbproto/xkbproto.html)

> Referência futura: https://shapecatcher.com/unicode/block/Gothic
[](ASSETS)

[ico-version     ]: https://img.shields.io/github/v/tag/jmurowaniecki/vitriol?sort=semver&style=flat-square
[vitriol.png     ]: ./doc/assets/background.png
[keyboard.png    ]: ./doc/assets/layout.png
[kbd-vitriol-as  ]: ./doc/assets/layout-vitriolas.png
[kbd-vitriol-es  ]: ./doc/assets/layout-vitrioles.png
[kbd-vitriol-ic  ]: ./doc/assets/layout-vitriolic.png
[kbd-vitriol-ma  ]: ./doc/assets/layout-vitriolma.png
[max-keyboard-url]: https://www.maxkeyboard.com/
[diy-with-arduino]: https://www.makeuseof.com/tag/make-custom-shortcut-buttons-arduino/
[TODO            ]: https://img.shields.io/badge/atalho_de_teclas_-indefinido-violet?style=flat-square
