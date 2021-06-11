#
# λ::Makefile
#

PREFIX?= /bin
TARGET?= /usr/share/X11/xkb
SOURCE?= vitriol.xkb
NULL  ?= /dev/null

ifneq (,$(DESTDIR))
TARGET =$(DESTDIR)
endif

CMD = "\\e[1m%-10s\\e[0m%s\n"
STR = "\\e[0;2;3m%s\\e[0m\n"
HLP = sed -E 's/(`.*`)/\\e[1m\1\\e[0m/'

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



backup:
	@\
	$(foreach    target, $(TARGETS), \
		cp $(target) $(target)_$(shell date +'%Y%m%d%H%M%S');)

check: # Check environment…
	@\
	echo "Files..: " $(FILES); \
	echo "Targets: " $(TARGETS)

install-step1:
	@\
	grep -iq "\svitriol\s" $(TARGET)/rules/evdev.lst \
	&& echo -e "Already installed on \e[1m$(TARGET)/rules/evdev.lst\e[0m" \
	|| { \
		LST=$(TARGET)/rules/evdev.lst; \
		cat evdev.lst >> \
		""""$${LST}""""; \
		cp "$${LST}""""" $(TARGET)/rules/base.lst; \
	}

install-step2:
	@\
	grep -iq "vitriol" $(TARGET)/rules/evdev.xml \
	&& echo -e "Already installed on \e[1m$(TARGET)/rules/evdev.xml\e[0m" \
	|| { \
		PICK_SIZE=$$(cat $(TARGET)/rules/evdev.xml | wc -l); \
		PICK_LINE=$$(cat $(TARGET)/rules/evdev.xml | \
		grep '<name>br</name>' -A10 -n             | \
		grep '<variantList''>' | sed -E 's/^([0-9]*).*$$/\1/'); \
		PICK_LAST=$$((PICK_SIZE - PICK_LINE)); \
		PICK_INIT=$$(head $(TARGET)/rules/evdev.xml -n$$PICK_LINE); \
		PICK_DONE=$$(tail $(TARGET)/rules/evdev.xml -n$$PICK_LAST); \
		echo "$${PICK_INIT}\n$$(cat evdev.xml)\n$${PICK_DONE}" > evdev.tmp.xml; \
	}


install-step-3: evdev.tmp.xml
	@\
	XML="""""""""$(TARGET)/rules/evdev.xml"; \
	mv evdev.tmp.xml \
	""""$${XML}""""; \
	cp "$${XML}" $(TARGET)/rules/base.xml

install-step4:
	@\
	grep -iq "vitriol" $(TARGET)/$(SYMBOL) \
	&& echo -e "Already installed on \e[1m$(TARGET)/$(SYMBOL)\e[0m… Updating…"; \
	HEAD= \
	TAIL= \
	; Ouroboros() { \
	export HEAD=$$1;\
	export TAIL=$$2;\
	};Ouroboros $$(grep -n '<[|/]*vitriol>' $(TARGET)/$(SYMBOL) \
	| sed -E 's/([0-9]*):.*/\1/'); \
	HEAD=$$(($$HEAD -1)); \
	TAIL=$${TAIL:-0}; \
	TAIL=$$(($$(wc  -l $(TARGET)/$(SYMBOL) | cut -d' ' -f1) - $$TAIL)); \
	head $(TARGET)/$(SYMBOL) -n$${HEAD} > .head; \
	tail $(TARGET)/$(SYMBOL) -n$${TAIL} > .tail; \
	cat ./.head ./.tail > "$(TARGET)/$(SYMBOL)"; \
	cat $(SOURCE) >> $(TARGET)/$(SYMBOL)

install-steps: \
	backup \
	install-step1 \
	install-step2 \
	install-step3 \
	install-step4

#
install: install-steps clean # Installs application.


update: install-step4 clean # Update symbols.

#
screenshot: # Take a screenshot from the keyboard layout
	@\
	layout="br(vitriol)"""""""""; \
	window="ptBR V.I.T.R.I.O.L."; \
	assets=doc/assets/layout.png; \
	gkbd-keyboard-display -l $$layout & screen="$$!"; sleep 1; \
	xdotool search --name "\?" set_window --name "$${window}"; \
	gnome-screenshot --window --file "./$${assets}" --delay 1; \
	kill -9 "$${screen}"


#
help: # Shows this help.
	@\
	echo -e """"""""""""""""""""""""" \
	$$(awk 'BEGIN {   FS=":.*?#"   } \
	/^(\w+:.*|)#/ {                  \
	gsub("^( : |)#( |)", """""""" ); \
	LEN=length($$2); COND=(LEN < 1); \
	FORMAT=(COND ? $(STR) : $(CMD)); \
	printf(FORMAT, $$1, """"""$$2 ); \
	}' $(MAKEFILE_LIST) | ($(HLP)))"


#
clean: # Remove temporary files.
	@\
	rm -Rf .head .tail *.head *.tail *.tmp.xml


#
%:
	@:
