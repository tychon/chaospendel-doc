
DOCS=Dokumentation.pdf Herleitung_standalone.pdf

# this is a phony target
all: $(DOCS)

%.pdf: %.tex charts/pendulumsketch.png
	pdflatex $*.tex

charts/pendulumsketch.png: ../network/data_pendulum
	cd charts ;\
	python generatesketch.py > pendulumsketch.svg ;\
	convert -trim pendulumsketch.svg pendulumsketch.png

