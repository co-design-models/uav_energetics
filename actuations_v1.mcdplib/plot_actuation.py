#!/usr/bin/env python3
from typing import cast, Mapping

from mcdp_ipython_utils import plot_all_directions, solve_queries, SolveQuery, VALUE_UNIT
from mcdp_library import MCDPLibrary
from mcdp_posets_algebra import frac_linspace
from reprep import Report
from zuper_commons.text import ThingName


def go() -> None:
    fn = "out/actuation_c1.html"

    model_name = cast(ThingName, "actuation")
    queries: list[SolveQuery] = []

    def add(q_: Mapping[str, VALUE_UNIT]) -> None:
        queries.append(SolveQuery(q_))

    n = 10

    for lift in frac_linspace(0, 10, n):
        q = {"lift": (lift, "N")}
        add(q)

    result_like = dict(power="W", cost="$")

    what_to_plot_res = result_like

    what_to_plot_fun = dict(lift="N")

    lib = MCDPLibrary()
    lib.add_search_dir(".")
    si, ndp = lib.load_ndp(model_name).split()

    data = solve_queries(ndp, queries, result_like)

    r = Report()

    plot_all_directions(
        r,
        queries=data.queries,
        results=data.results,
        what_to_plot_res=what_to_plot_res,
        what_to_plot_fun=what_to_plot_fun,
    )
    print("writing to %r" % fn)
    r.to_html(fn)


if __name__ == "__main__":
    # go()
    go()
