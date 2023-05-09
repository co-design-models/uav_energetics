outd=out-Makefile


all: plot-battery-choice plot-drone

	# will fail
	$(MAKE) pics
plot-battery-choice:  
	env -u MCDP_TEST_LIBRARIES_EXCLUDE ./plot_batteries_choice.py  -c make

plot-drone:  
	env -u MCDP_TEST_LIBRARIES_EXCLUDE ./plot_drone.py  -c rparmake



clean:
	rm -rf $(outd) _cached out-*



pics: pics1 pics2 pics3


pics3:
	mcdp-plot -D .. --out $(outd)/batteries2_min_cost batteries2_min_cost

pics2:
	mcdp-plot -D .. --out $(outd)/drone_pretty drone_pretty
	mcdp-plot -D .. --out $(outd)/actuation Actuation
	mcdp-plot -D .. --out $(outd)/drone1 drone1


pics1:
	mcdp-plot --out $(outd)/Battery_LCO Battery_LCO
