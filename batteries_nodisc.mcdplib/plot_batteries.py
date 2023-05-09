#!/usr/bin/env python3
from typing import cast

from mcdp_ipython_utils import plot_all_directions, solve_combinations, SolveQueryMultiple
from mcdp_library import MCDPLibrary
from mcdp_posets_algebra import frac_linspace
from reprep import Report
from zuper_commons.text import ThingName


def go() -> None:
    combinations = SolveQueryMultiple(
        {"capacity": (frac_linspace(50, 3000, 10), "Wh"), "missions": (1000, "[]")}
    )
    result_like = dict(maintenance="dimensionless", cost="USD", mass="kg")
    what_to_plot_res = result_like
    what_to_plot_fun = dict(capacity="Wh", missions="[]")

    lib = MCDPLibrary()
    lib.add_search_dir(".")
    si, ndp = lib.load_ndp(cast(ThingName, "batteries")).split()

    data = solve_combinations(ndp, combinations, result_like)

    r = Report()

    plot_all_directions(
        r,
        queries=data.queries,
        results=data.results,
        what_to_plot_res=what_to_plot_res,
        what_to_plot_fun=what_to_plot_fun,
    )
    r.to_html("out/batteries-c1.html")


def go2() -> None:
    model_name = cast(ThingName, "batteries_squash")
    combinations = SolveQueryMultiple(
        {"capacity": (frac_linspace(50, 3000, 10), "Wh"), "missions": (1000, "[]")}
    )
    result_like = dict(cost="USD", mass="kg")
    what_to_plot_res = result_like
    what_to_plot_fun = dict(capacity="Wh", missions="[]")

    lib = MCDPLibrary()
    lib.add_search_dir(".")
    si, ndp = lib.load_ndp(model_name).split()

    data = solve_combinations(ndp, combinations, result_like)

    r = Report()

    plot_all_directions(
        r,
        queries=data.queries,
        results=data.results,
        what_to_plot_res=what_to_plot_res,
        what_to_plot_fun=what_to_plot_fun,
    )
    r.to_html("out/batteries_squash-c2.html")


if __name__ == "__main__":
    go()
    go2()
