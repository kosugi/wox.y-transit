
.PHONY: all clean test install

OBJDIR=./build

all: $(OBJDIR)/y-transit.wox

install: $(OBJDIR)/y-transit.wox
	@[ -d "$(WOX_PLUGIN_DIR)" ] || (echo "WOX_PLUGIN_DIR not defined or bad directory" && exit 1)
	mkdir -p $(WOX_PLUGIN_DIR)/y-transit
	rsync -r build/wox/ $(WOX_PLUGIN_DIR)/y-transit/

$(OBJDIR)/y-transit.wox: plugin.json main.py query.py wox.py $(OBJDIR)/icon.png
	mkdir -p $(OBJDIR)/wox
	cp plugin.json main.py query.py $(OBJDIR)/icon.png $(OBJDIR)/wox
	zip -j $@ $(OBJDIR)/wox/*

wox.py:
	wget https://raw.githubusercontent.com/Wox-launcher/Wox/master/JsonRPC/wox.py

$(OBJDIR)/icon.png: icon.svg
	@[ -d "$(OBJDIR)" ] || mkdir -p $(OBJDIR)
	convert -background None icon.svg $@

test:
	python -m unittest test_query

clean:
	rm -rf *.pyc $(OBJDIR)/* wox.py
