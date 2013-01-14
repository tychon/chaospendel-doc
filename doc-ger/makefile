
.PHONY: charts all clean

DOCS := Dokumentation.pdf Herleitung_standalone.pdf
SECDOCS := Simulation.tex Modell.tex

# this is a phony target
all: $(DOCS)

charts:
	make -C charts/

%.pdf: %.tex charts $(SECDOCS)
	pdflatex $*.tex
	pdflatex $*.tex

clean:
	make -C charts/ clean
	rm -f *.pdf *.aux *.log *.bbl *.blg

