outd=out-Makefile

# all: plot
all:
	./generate_actuations.py
	mcdp-plot --out=$(outd) -d . actuation
	./plot_actuation.py

clean:
	rm -rf out out-memo_disk _cached

realclean:
	rm -rf actuation*.mcdp

# solve:
# 	mcdp-solve --out=out/solve1 --plot --imp -d . droneC "<0s, 0kg, 0W, 0 []>"
# 	#mcdp-solve --out=out/drone1/sb -d models/drone1 drone "<1 hour, 0kg>"
# 	DISABLE_CONTRACTS=1 python plot_droneC.py

# plot:
# 	mcdp-plot --out=out/actuation1 -d . actuation1
# 	mcdp-plot --out=out/drone -d . drone
