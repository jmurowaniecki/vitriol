# **V·I·T·R·I·O·L** <img align="right" src="https://img.shields.io/github/v/tag/jmurowaniecki/vitriol?sort=semver&style=flat-square" />

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

Esta biblioteca visa contribuir para os estudos e publicações não apenas dos casos citados acima, se você necessitar de um mapeamento específico e/ou tiver alguma ideia, dúvida, crítica ou sugestão sinta-se a vontade para contatar e/ou abrir uma issue, pull request ou até mesmo realizar um fork deste projeto.


> ¹ : Significa literalmente _"Visita Interiora Terrae, Rectificando, Invenies Occultum Lapidem."_

> ² : Não está completo, mas já é um _work-in-progress_.



## Instalação

Adicione o conteúdo do arquivo `evdev.lst` à seção `! variant` do arquivo `/usr/share/X11/xkb/rules/evdev.lst`, e ao `evdev.xml` para sua `variantList` correspondente na seção **BR** do arquivo `/usr/share/X11/xkb/rules/evdev.xml`.

Então finalmente adicione o arquivo `vitriol.xkb` ao seu arquivo de símbolos `/usr/share/X11/xkb/symbols/br`.

Após realizar a instalação é necessário reiniciar sua sessão X11 (fazer logout).

> Você também pode realizar esses procedimentos de forma automática com o comando `make install`.



## Primeiros passos

1.  Realize a instalação utilizando os passo do **Makefile**: `make install`;
2.  Abra as configurações do seu sistema e vá para **`Linguagem / Configuração de teclados`**;
3.  Selecione o mapeamento **Portuguese (Brazil, Esoteric)** desejado;
4.  Pressione **` Alt Gr. `** + **` Shift `** + **` ; `** para imprimir o caractere ' **` ∴ `** '.
5.  Saiba que eventuais atualizações do sistema sobreescreverão suas configurações, sendo necessário eventualmente repetir o processo de instalação.


> Se você e interessa em teclas customizadas e/ou impressas dê uma [olhada aqui][max-keyboard-url].
\
\
> Se você quer fazer um teclado customizado utilizando Arduino [isso aqui pode te ajudar][diy-with-arduino].
\
\
> Devido a erros renderizando os caracteres _Level 3, Super_ ou _Meta_ utilizando o programa `draw-key` de [gkbd-keyboard-drawing](https://github.com/GNOME/libgnomekbd/blob/master/libgnomekbd/gkbd-keyboard-drawing.c) algumas teclas e seus valores podem ter sido renderizadas e posicionadas manualmente no teclado de exemplo.



## Diversidade de gênero e termos juvélicos

Símbolo | Combinação de teclas | Identidade de gênero e/ou Orientação sexual
:------:|---------------------:|---------------------------------------------
 `♀` | ` Shift ` ` AltGr ` **` [ `** | Gênero **Feminino**
 `♂` | ` Shift ` ` AltGr ` **` ] `** | Gênero **Masculino**
 `⚧` | ` Shift ` ` AltGr ` **` ´ `** | Gênero **transgênero**
 `⚦` | ` AltGr ` **` = `** | Gênero **transgênero** **Masculino**
 `⚥` | ` AltGr ` ` Shift ` **` - `** | Gênero **bigênero**<br>Também chamado **bigender**, **Cis**, **intersex** representado por um símbolo masculino + feminino.
 `☿` | ` Shift ` ` AltGr ` **` ~ `** | Gênero **intersexo** ou **intergênero**
 `⊕` | ` Shift ` ` AltGr ` **` . `** | Gênero **ipsogênero**<br>_Pessoa que se identifica completamente - e pela vida inteira - com o **mesmo gênero** designado em sua nascença._
 `🞵` | ` Shift ` ` AltGr ` **` = `** | Gênero **não-binárie**
 `⚨` | ![][TODO] | Gênero **andrógine**<br>Ou também **transgênero** **Feminino**.
 `⚲` | ![][TODO] | Gênero **neutrois/gênero neutro**<br>Também chamada **genderless**, **sem gênero**
 `○` | ![][TODO] | Gênero **agênero**
 `⚩` | ![][TODO] | Gênero **aliagênero**<br>Também enquadrado como **não binário**.
 `⚴` | ![][TODO] | Gênero **neurogênero**
 `⚣` | ` AltGr ` **` ~ `** | **gay**
 `⚢` | ` AltGr ` **` ´ `** | **lésbica**
 `π`  | ` AltGr ` ` Shift ` **` P `** | **poliamorosa**
 `♠`  | ` AltGr ` **` P `** | **assexual**<br>Também interpretado como **arromântique/arromântico**.
 `☽︎☾︎` | ` AltGr ` **` 8 `** e, a seguir ` AltGr ` **` 0 `** | **bissexual**<br>Representado aqui por uma _`lua dupla`_.
 `⚤` | ![][TODO] | **bissexual**
 `ꉣ`  | ![][TODO] | **panssexual**
 `☀︎︎`  | ![][TODO] | **panssexual**
 `➴`  | ![][TODO] | **arromântique**

<!--
Símbolo|Combinação de teclas|Status do relacionamento
:-----:|:-----------:|---
` ⚯ ` | ![][TODO] | Namorando
` ⚭ ` | ![][TODO] | Casado
` ⚮ ` | ![][TODO] | Divorciado
-->

> Fontes e artigos:
[O que voce precisa saber sobre o i em lgbti no dia da visibilidade intersexual](https://www.grupodignidade.org.br/intersex-o-que-voce-precisa-saber-sobre-o-i-em-lgbti-no-dia-da-visibilidade-intersexual/),
[Categorias relacionadas a genero](https://orientando.org/categorias-relacionadas-a-genero/) e
[Gender symbols](http://www.cakeworld.info/transsexualism/gender-symbols).



[](ASSETS)

[ico-version]: https://img.shields.io/github/v/tag/jmurowaniecki/vitriol?sort=semver&style=flat-square

[keyboard.png]: ./doc/assets/layout.png

[max-keyboard-url]: https://www.maxkeyboard.com/
[diy-with-arduino]: https://www.makeuseof.com/tag/make-custom-shortcut-buttons-arduino/
[TODO]: https://img.shields.io/badge/atalho_de_teclas_-indefinido-violet?style=flat-square