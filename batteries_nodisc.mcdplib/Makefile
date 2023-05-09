outd=out-Makefile

all:
	./generate_batteries.py

	mcdp-solve --out out --imp batteries "<0.5 MJ, 1000 []>"

	./plot_batteries.py

	mcdp-plot --out $(outd) Battery_NiCad
	mcdp-plot --out $(outd) batteries_squash
	mcdp-plot --out $(outd) batteries


clean:
	rm -rf out-memo_disk $(outd) _cached

realclean:
	rm -f bat_*.mcdp batteries.mcdp summary.txt


solve2:
	mcdp-solve --out $(outd) --plot --imp Battery_NiCad  "<0.6 MJ, 1000 []>"
