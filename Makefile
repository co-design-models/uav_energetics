all:
	$(MAKE) -C actuations_v1.mcdplib
	$(MAKE) -C actuations_v2.mcdplib
	$(MAKE) -C batteries_nodisc.mcdplib
	$(MAKE) -C batteries_v1.mcdplib
	$(MAKE) -C droneA_v1.mcdplib
	$(MAKE) -C droneB_v1.mcdplib
	$(MAKE) -C droneC_cost_v1.mcdplib
	$(MAKE) -C droneD_complete_v1.mcdplib
	$(MAKE) -C droneD_complete_v2.mcdplib
	$(MAKE) -C libname2.mcdplib
	$(MAKE) -C mcdp_theory.mcdplib
	$(MAKE) -C pretty.mcdplib
clean:
	$(MAKE) -C actuations_v1.mcdplib clean
	$(MAKE) -C actuations_v2.mcdplib clean
	$(MAKE) -C batteries_nodisc.mcdplib clean
	$(MAKE) -C batteries_v1.mcdplib clean
	$(MAKE) -C droneA_v1.mcdplib clean
	$(MAKE) -C droneB_v1.mcdplib clean
	$(MAKE) -C droneC_cost_v1.mcdplib clean
	$(MAKE) -C droneD_complete_v1.mcdplib clean
	$(MAKE) -C droneD_complete_v2.mcdplib clean
	$(MAKE) -C libname2.mcdplib clean
	$(MAKE) -C mcdp_theory.mcdplib clean
	$(MAKE) -C pretty.mcdplib clean

