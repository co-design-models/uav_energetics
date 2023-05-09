#!/usr/bin/env python3
from decimal import Decimal
from typing import cast

import numpy as np

from mcdp_ipython_utils import plot_all_directions, solve_queries, SolveQuery
from mcdp_library import Librarian
from mcdp_posets import RLike
from reprep import Report
from zuper_commons import ZLogger
from zuper_commons.text import LibraryName, ThingName

logger = ZLogger(__name__)


def go() -> None:
    model_name = cast(ThingName, "droneC")
    queries: list[SolveQuery] = []

    def add(q_: dict[str, tuple[RLike, str]]) -> None:
        queries.append(SolveQuery(q_))

    n = 10
    endurance = np.linspace(1, 20, n)
    payload = np.linspace(5, 50, n)

    for endurance, payload in zip(endurance, payload):
        q = {
            "num_missions": (Decimal(1000), "[]"),
            "extra_power": (Decimal(5), "W"),
            "extra_payload": (Decimal.from_float(payload), "g"),
            "endurance": (Decimal.from_float(endurance), "minutes"),
        }
        add(q)

    result_like = dict(total_cost="CHF", total_mass="kg")
    what_to_plot_res = result_like
    what_to_plot_fun = dict(extra_payload="g", endurance="minutes")

    librarian = Librarian()
    librarian.find_libraries("..")
    lib = librarian.load_library(cast(LibraryName, "droneC_cost_v1"))
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
    fn = "out/droneC_c1.html"
    logger.info("writing to %r" % fn)
    r.to_html(fn)


if __name__ == "__main__":
    # go()
    go()
