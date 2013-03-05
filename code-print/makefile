APSOPTS := --left-title --left-footer --footer --line-numbers 1 --toc --file-align fill

all: numerical network

N := ../chaospendel/numerical
NUMERICALFILES := $N/main.hs $N/RungeKutta.hs $N/stats.awk $N/show.py

numerical: $(NUMERICALFILES)
	a2ps $(APSOPTS) $^ --output numerical.ps

N := ../chaospendel/network
NETWORKFILES := $N/makefile
NETWORKFILES += $N/memory_wrappers.h $N/memory_wrappers.c $N/integral.h $N/integral.c
NETWORKFILES += $N/x11draw.h $N/x11draw.c $N/markov_chain.h $N/markov_chain.c
NETWORKFILES += $N/common.h $N/common.c $N/uds_server.h $N/uds_server.c
NETWORKFILES += $N/uds_client.h $N/uds_client.c $N/protocol.h $N/protocol.c
NETWORKFILES += $N/projectreader.h $N/projectreader.c
NETWORKFILES += $N/reader.c $N/replay.c
NETWORKFILES += $N/testreader.c $N/rangetester.c $N/normalisation.c
NETWORKFILES += $N/tracker.c $N/markov_prediction.c
NETWORKFILES += $N/run.sh

network: $(NETWORKFILES)
	a2ps $(APSOPTS) $^ --output network.ps
