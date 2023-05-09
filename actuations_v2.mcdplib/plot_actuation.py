#!/usr/bin/env python3
from typing import List

from mcdp_ipython_utils import NAME2UNIT, plot_all_directions, solve_queries, SolveQueriesResult, SolveQuery
from mcdp_library import MCDPLibrary
from mcdp_posets_algebra import frac_linspace
from reprep import Report
from zuper_commons.fs import FilePath
from zuper_commons.text import ThingName


def go() -> None:
    queries: List[SolveQuery] = []

    n = 10
    lifts = frac_linspace(0, 10, n)

    for (lift,) in zip(lifts):
        q = {"lift": (lift, "N")}
        queries.append(SolveQuery(q))

    result_like = dict(power="W", cost="$")

    what_to_plot_res = result_like

    what_to_plot_fun = dict(lift="N")

    for model_name in ["actuation_a1", "actuation_a2", "actuation_a3", "actuation"]:
        fn = "out/%s.html" % model_name
        go_(model_name, queries, result_like, what_to_plot_res, what_to_plot_fun, fn)


def go_(
    model_name: str,
    queries: list[SolveQuery],
    result_like: NAME2UNIT,
    what_to_plot_res: NAME2UNIT,
    what_to_plot_fun: NAME2UNIT,
    fn: FilePath,
):
    lib = MCDPLibrary()
    lib.add_search_dir(".")
    si, ndp = lib.load_ndp(ThingName(model_name)).split()

    data: SolveQueriesResult = solve_queries(ndp, queries, result_like)

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
