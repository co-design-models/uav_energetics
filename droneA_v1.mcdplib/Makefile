outd=out-Makefile

all: solve plot

clean:
	rm -rf $(outd) _cached

solve:
	mcdp-solve --out $(outd)/solve1 --plot --imp -d . Drone "<0s, 0kg, 0W>"
	#mcdp-solve --out=out/drone1/sb -d models/drone1 drone "<1 hour, 0kg>"


plot:
	mcdp-plot --out $(outd) -d . Actuation
	mcdp-plot --out $(outd) -d . Drone
