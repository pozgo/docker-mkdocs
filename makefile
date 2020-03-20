PYTHON = python2
MKDOCS = mkdocs
SRC = $(wildcard *.m)
TAR = $(SRC:.m=.md)

mfiledir = docs/mfiles/splitter

$(info SRC is $(SRC))
$(info TAR is $(TAR))
$(info mfiledir is $(mfiledir))

.PHONY: all clean

all: $(TAR)

%.md: %.m matdoc.py matdocparser.py
	$(info $(@))
	$(info $(@D))
	mkdir -p $(mfiledir)
	$(PYTHON) ./matdoc.py "$(<)" > "$(mfiledir)/$(@)"

doc-serve: mkdocs.yml
	$(MKDOCS) serve

clean:
	rm -f $(TAR)
	rm -rf $(mfiledir)



