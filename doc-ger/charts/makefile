
.PHONY: all clean

all: pendulumsketch.png circuit_dia.png network_dia.png mathsketch_dia.png

%_dia.png: %.dia
	dia -e $*_dia.png $*.dia

pendulumsketch.png: generatesketch.py ../../chaospendel/network/data_pendulum
	python generatesketch.py > pendulumsketch.svg
	convert -trim pendulumsketch.svg pendulumsketch.png

clean:
	rm -f *.png *.svg

