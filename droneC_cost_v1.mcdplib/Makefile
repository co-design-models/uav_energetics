outd=out-Makefile

all: solve


clean:
	rm -rf $(outd) out-memo_disk _cached

solve:
	mcdp-solve --out $(outd) --plot --imp -d . -D .. droneC "<0s, 0kg, 0W, 0 []>"
	#mcdp-solve --out=out/drone1/sb -d models/drone1 drone "<1 hour, 0kg>"
	DISABLE_CONTRACTS=1 ./plot_droneC.py

# plot:
# 	mcdp-plot --out=out/actuation1 -d . actuation1
# 	mcdp-plot --out=out/drone -d . drone
