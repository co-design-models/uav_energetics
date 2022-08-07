#!/usr/bin/env python3
from typing import cast

import numpy as np

from mcdp_ipython_utils import plot_all_directions, solve_queries
from mcdp_library import MCDPLibrary
from reprep import Report
from zuper_commons.fs import FilePath
from zuper_commons.text import ThingName


def go():
    fn = cast(FilePath, "out/actuation_c1.html")

    model_name = ThingName("actuation")
    queries = []

    def add(q):
        queries.append(q)

    n = 10
    lifts = np.linspace(0, 10.0, n)

    for (lift,) in zip(lifts):
        q = {"lift": (lift, "N")}
        add(q)

    result_like = dict(power="W", cost="$")

    what_to_plot_res = result_like

    what_to_plot_fun = dict(lift="N")

    lib = MCDPLibrary()
    lib.add_search_dir(".")
    ndp = lib.load_ndp(model_name)

    data = solve_queries(ndp, queries, result_like)

    r = Report()

    plot_all_directions(
        r,
        queries=data["queries"],
        results=data["results"],
        what_to_plot_res=what_to_plot_res,
        what_to_plot_fun=what_to_plot_fun,
    )
    print("writing to %r" % fn)
    r.to_html(fn)


if __name__ == "__main__":
    # go()
    go()
