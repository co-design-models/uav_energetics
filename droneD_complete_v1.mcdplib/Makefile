outd=out-Makefile

all:
	mcdp-plot --out $(outd) -d . market

clean:
	rm -rf $(outd)  _cached out-memo_disk


bug:
	rm -f _cached/market*.cached
	mcdp-plot --out $(outd)  -d . market_flatten
bug2:
	rm -f _cached/test*.cached
	mcdp-plot --out $(outd)  -d . test
