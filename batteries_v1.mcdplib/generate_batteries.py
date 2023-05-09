#!/usr/bin/env python3

import string

template = """
mcdp {
    provides capacity [J]
    provides missions [dimensionless]

    requires mass     [g]
    requires cost     [$$]

    # Number of replacements
    requires maintenance [dimensionless]

    # Battery properties
    specific_energy = $specific_energy
    specific_cost = $specific_cost
    cycles = $cycles

    # Constraint between mass and capacity
    massc = provided capacity / specific_energy

    # How many times should it be replaced?
    num_replacements = ceil(provided missions / cycles)
    required maintenance >= num_replacements

    # Cost is proportional to number of replacements
    costc = (provided capacity / specific_cost) * num_replacements

    required cost >= approx(costc, 1 USD)
    required mass >= approx(massc, 10 g)
}
"""

types = {
    "NCA": dict(
        desc="Lithium nickel cobalt aluminum oxide",
        specific_energy="220 Wh/kg",
        specific_cost="",
        cycles="1500",
    ),
    "NMC": dict(
        desc="Lithium nickel manganese cobalt oxide",
        specific_energy="205 Wh/kg",
        specific_cost="",
        cycles="5000",
    ),
    "LCO": dict(
        desc="Lithium cobalt oxide", specific_energy="195 Wh/kg", specific_cost=" 2.84 Wh/$", cycles="750"
    ),
    "LiPo": dict(
        desc="Lithium polimer", specific_energy="150 Wh/kg", specific_cost=" 2.50 Wh/$", cycles="600"
    ),
    "LMO": dict(
        desc="Lithium manganese oxide ", specific_energy="150 Wh/kg", specific_cost=" 2.84 Wh/$", cycles="500"
    ),
    "NiMH": dict(
        desc="Nickel-metal hydride", specific_energy="100 Wh/kg", specific_cost=" 3.41 Wh/$", cycles="500"
    ),
    "LFP": dict(
        desc="Lithium iron phosphate", specific_energy=" 90 Wh/kg", specific_cost=" 1.50 Wh/$", cycles="1500"
    ),
    "NiH2": dict(
        desc="Nickel-hydrogen", specific_energy=" 45 Wh/kg", specific_cost="10.50 Wh/$", cycles="20000"
    ),
    "NiCad": dict(
        desc="Nickel-cadmium", specific_energy=" 30 Wh/kg", specific_cost=" 7.50 Wh/$", cycles="500"
    ),
    "SLA": dict(desc="Lead-acid", specific_energy=" 30 Wh/kg", specific_cost=" 7.00 Wh/$", cycles="500"),
}


def go() -> None:
    summary = ""

    good = []
    discarded = []
    for name, v in types.items():
        if not v["specific_cost"]:
            print("skipping %s because no specific cost" % name)
            discarded.append(name)
            continue

        v["cycles"] = "%s []" % v["cycles"]
        s2 = string.Template(template).substitute(v)

        print(s2)
        # ndp = parse_ndp(s2)
        model_name = "Battery_%s" % name
        fname = model_name + ".mcdp"
        with open(fname, "w") as f:
            f.write(s2)

        good.append(name)

        summary += "\n%10s %10s %10s %10s  %s" % (
            name,
            v["specific_energy"],
            v["specific_cost"],
            v["cycles"],
            v["desc"],
        )
    print(summary)
    with open("summary.txt", "w") as f:
        f.write(summary)
    ss = """
choose(
    %s
)
    """ % ",\n    ".join(
        "%8s: (load Battery_%s)" % (g, g) for g in good
    )
    with open("batteries.mcdp", "w") as f:
        f.write(ss)


if __name__ == "__main__":
    go()
