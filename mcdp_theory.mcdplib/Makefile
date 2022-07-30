outd=out-Makefile

all:
	DISABLE_CONTRACTS=1 ./plot_batteries_choice.py  -c rparmake
	DISABLE_CONTRACTS=1 ./plot_drone.py  -c rparmake

	# will fail
	# $(MAKE) pics

clean:
	rm -rf $(outd) out-* _cached


pics: pics1 pics2 pics3


pics3:
	mcdp-plot -D .. --out $(outd)/batteries2_min_cost batteries2_min_cost

pics2:
	mcdp-plot -D .. --out $(outd)/drone_pretty drone_pretty
	mcdp-plot -D .. --out $(outd)/actuation Actuation
	mcdp-plot -D .. --out $(outd)/drone1 drone1


pics1:
	mcdp-plot --out $(outd)/Battery_LCO Battery_LCO
