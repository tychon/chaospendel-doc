
.PHONY: charts all clean

DOCS := Dokumentation.pdf Herleitung_standalone.pdf

# this is a phony target
all: $(DOCS)

charts:
	make -C charts/

%.pdf: %.tex charts
	pdflatex $*.tex

clean:
	make -C charts/ clean
	rm -f *.pdf *.aux *.log

