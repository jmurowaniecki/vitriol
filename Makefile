#
# λ::Makefile
#
# For further information see `README.md`.

PREFIX?= /bin
TARGET?= /usr/share/X11/xkb
SOURCE?= vitriol.xkb
NULL  ?= /dev/null
VIMRC  = ~/.vimrc

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

TARGETS = $(foreach target, $(FILES), $(wildcard $(TARGET)/$(target)))



DEFAULT: help



backup:
	@\
	$(foreach    target, $(TARGETS), \
		cp $(target) $(target)_$(shell date +'%Y%m%d%H%M%S');)


#
install: backup # Installs application.
	@\
	LST=$(TARGET)/rules/evdev.lst; \
	cat $(SOURCE) >> $(TARGET)/$(SYMBOL); \
	cat evdev.lst >> \
	""""$(LST)"""""";\
	cp  $(LST)"""""" $(TARGET)/rules/base.lst

	@\
	PICK_SIZE=$$(cat $(TARGET)/rules/evdev.xml | wc -l); \
	PICK_LINE=$$(cat $(TARGET)/rules/evdev.xml | \
	grep '<name>br</name>' -A10 -n             | \
	grep '<variantList''>' | sed -E 's/^([0-9]*).*$$/\1/'); \
	PICK_LAST=$$((PICK_SIZE - PICK_LINE)); \
	PICK_INIT=$$(head $(TARGET)/rules/evdev.xml -n$$PICK_LINE); \
	PICK_DONE=$$(tail $(TARGET)/rules/evdev.xml -n$$PICK_LAST); \
	echo "$${PICK_INIT}\n$$(cat evdev.xml)\n$${PICK_DONE}" > evdev.tmp.xml

	@\
	XML=$(TARGET)/rules/evdev.xml; \
	mv evdev.tmp.xml  $(XML) ;     \
		cp $(XML) $(TARGET)/rules/base.xml


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
