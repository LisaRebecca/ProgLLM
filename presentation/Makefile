SLIDES_TEX = talk.tex
SLIDES_PDF = talk.pdf

THEME_DIR = _template/beamerthemefau

I2BEAMER_DIR = _template/i2beamer
I2BEAMER_TEX = $(wildcard $(I2BEAMER_DIR)/*.tex) $(wildcard $(I2BEAMER_DIR)/*.sty)

TMP_DIR = _tmp

TRASH_FILES = *.aux *.log *.nav *.out *.snm *.toc *.lst *.vrb *.off *.fdb_latexmk
FLS_FILE = $(patsubst %.pdf,%.fls,$(SLIDES_PDF))

.DEFAULT_GOAL := all

#===================================

.PHONY: all
all: $(SLIDES_PDF)

$(SLIDES_PDF): $(SLIDES_TEX) $(I2BEAMER_TEX)
	@rm -rf $(TMP_DIR) && mkdir -p $(TMP_DIR)
	TEXINPUTS="$(THEME_DIR):$(I2BEAMER_DIR):" pdflatex -wide -halt-on-error -file-line-error $<
	@rm -rf $(TMP_DIR) && mkdir -p $(TMP_DIR)
	TEXINPUTS="$(THEME_DIR):$(I2BEAMER_DIR):" pdflatex -wide -halt-on-error -file-line-error $<

#===================================

.PHONY: distclean
distclean: clean
	rm -f $(SLIDES_PDF)

.PHONY: clean
clean:
	rm -f $(TRASH_FILES)
	rm -f $(FLS_FILE)
	rm -rf $(TMP_DIR)
