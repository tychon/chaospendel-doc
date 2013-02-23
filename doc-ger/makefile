
.PHONY: charts all clean

DOCS := Dokumentation.pdf Herleitung_standalone.pdf
SECDOCS := Simulation.tex Modell.tex
BIBL := Dokumentation.bbl

# this is a phony target
all: $(DOCS)

bibliography: $(BIBL)

charts:
	make -C charts/

%.bbl: %.bib
	rm -f $*.bbl
	pdflatex $*.tex # generate cite data in .aux file
	bibtex $*       # run bibtex to generate .bbl from .bib file

%.pdf: %.tex charts bibliography $(SECDOCS)
	pdflatex $*.tex
	pdflatex $*.tex

clean:
	make -C charts/ clean
	rm -f *.pdf *.aux *.log *.bbl *.blg

