#!/usr/bin/env python3

from mcdp_ipython_utils import plot_all_directions, solve_combinations, SolveQueryMultiple
from mcdp_library import get_librarian
from mcdp_posets_algebra import frac_linspace
from reprep import Report

 
def go(lib):
    combinations = SolveQueryMultiple(
        {"capacity": (frac_linspace(50, 3000, 10), "Wh"), "missions": (1000, "[]")}
    )
    result_like = dict(maintenance="dimensionless", cost="USD", mass="kg")
    what_to_plot_res = result_like
    what_to_plot_fun = dict(capacity="Wh", missions="[]")

    si, ndp = lib.load_ndp("batteries").split()

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


def go2(lib):
    model_name = "batteries_squash"
    combinations = SolveQueryMultiple(
        {"capacity": (frac_linspace(50, 3000, 10), "Wh"), "missions": (1000, "[]")}
    )
    result_like = dict(cost="USD", mass="kg")
    what_to_plot_res = result_like
    what_to_plot_fun = dict(capacity="Wh", missions="[]")

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


def go0():
    librarian = get_librarian(main_dir="../..")
    lib0 = librarian.get_library_by_dir(".")
    go(lib0)
    go2(lib0)


if __name__ == "__main__":
    go0()
