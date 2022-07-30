outd=out-Makefile

all: solve plot

clean:
	rm -rf $(outd) _cached

solve:
	mcdp-solve --out $(outd)/solve1 --plot --imp -d . drone "<0s, 0kg, 0W>"

plot:
	mcdp-plot --out $(outd) -d . Actuation
	mcdp-plot --out $(outd) -d . Drone
