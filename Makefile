#
# λ::Makefile
#

TODAY  = $(shell date +'%Y%m%d%H%M%S')
TARGET?= /usr/share/X11/xkb
WARNING=Automatically generated on $(TODAY)

ifneq (,$(DESTDIR))
TARGET =$(DESTDIR)
endif

CMD = "\\e[1m%-10s\\e[0m%s\n"
STR = "\\e[0;2;3m%s\\e[0m\n"
HLP = sed -E 's/(`.*`)/\\e[1m\1\\e[0m/'

SOURCE= vitriol
SYMBOL= symbols/br
RULES = rules/evdev.lst \
	rules/evdev.xml \
	rules/evdev     \
	rules/base.lst  \
	rules/base.xml  \
	rules/base

FILES = $(RULES) \
	$(SYMBOL)

TARGETS = $(foreach destiny, $(FILES), $(wildcard $(TARGET)/$(destiny)))



DEFAULT: help
# For further information see `README.md`.
#̣


# Repository maintenance options:
backup:
	@\
	$(foreach    target, $(TARGETS), \
		cp $(target) $(target)_$(TODAY);)

build: # Build symbols.
	@\
	target=install/$(SYMBOL).xkb; \
	rm -Rf $${target}; \
	echo "// <$(SOURCE)>"""  >> $${target}; \
	echo "// $(WARNING)"""   >> $${target}; \
	cat install/symbols/vit* >> $${target}; \
	echo "\n// </$(SOURCE)>" >> $${target}

screenshots: \
	screenshot-vitriolas \
	screenshot-vitrioles \
	screenshot-vitriolic \
	screenshot-vitriolma
update: screenshots # Take screenshots from the keyboard layouts.

screenshot-%: # Take a screenshot from the keyboard layout
	@\
	layout="br($(*))"; \
	window="ptBR V.I.T.R.I.O.L. $(*)"; \
	assets=doc/assets/layout-$(*).png; \
	gkbd-keyboard-display -l "$${layout}" & screen="$$!"; sleep 1; \
	xdotool getactivewindow set_window --name "$${window}"; \
	gnome-screenshot --window --file "./$${assets}" --delay 1; \
	kill -9 "$${screen}"

extract: # Extract existing variants in environment…
	./install.py \
		update \
		--target=$(TARGET)

check: # Check environment…
	./install.py \
		check \
		--target=$(TARGET)

#
install: backup # Installs application.
	./install.py \
		install \
		--target=$(TARGET)

#
force: backup # Installs application.
	./install.py \
		install \
		--force \
		--target=$(TARGET)
#
help: # Shows this help.
	@\
	echo """"""""""""""""""""""""""" \
	$$(awk 'BEGIN {   FS=":.*?#"   } \
	/^(\w+:.*|)#/ {                  \
	gsub("^( : |)#( |)", """""""" ); \
	LEN=length($$2); COND=(LEN < 1); \
	FORMAT=(COND ? $(STR) : $(CMD)); \
	printf(FORMAT, $$1, """"""$$2 ); \
	}' $(MAKEFILE_LIST) | ($(HLP)))"


#
%:
	@:
