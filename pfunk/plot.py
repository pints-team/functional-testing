#
# Shared plotting code.
#
# This file is part of Pints Functional Testing.
#  Copyright (c) 2017-2018, University of Oxford.
#  For licensing information, see the LICENSE file distributed with the Pints
#  functional testing software package.
#
from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals

import os
import logging
import numpy as np
import matplotlib.pyplot as plt

import pfunk

def variable(results, variable, title, ylabel):
    """
    Creates and returns a default plot for a variable vs commits.
    """
    fig = plt.figure(figsize=(11, 4.5))
    plt.suptitle(title + ' : ' + pfunk.date())

    r = 0.3

    plt.subplot(1, 2, 1)
    plt.ylabel(ylabel)
    plt.xlabel('Commit')
    fig.autofmt_xdate()
    x, y, u, m, s = pfunk.gather_statistics_per_commit(results, variable)
    xlookup = dict(zip(u, np.arange(len(u))))
    x = np.array([xlookup[i] for i in x], dtype=float)
    x += np.random.uniform(-r, r, x.shape)
    plt.plot(u, m, 'ko-', alpha=0.5)
    plt.plot(x, y, 'x', alpha=0.75)
    try:
        y = np.array(y)
        ymax = np.max(y[np.isfinite(y)])
    except ValueError:
        ymax = 1

    plt.subplot(1, 2, 2)
    plt.ylabel(ylabel)
    plt.xlabel('Commit')
    fig.autofmt_xdate()
    x, y, u, m, s = pfunk.gather_statistics_per_commit(
        results, variable, remove_outliers=True)
    x = np.array([xlookup[i] for i in x], dtype=float)
    x += np.random.uniform(-r, r, x.shape)
    plt.plot(u, m, 'ko-', alpha=0.5)
    plt.plot(x, y, 'x', alpha=0.75)
    y = np.array(y)
    try:
        y = np.array(y)
        ymax = max(ymax, np.max(y[np.isfinite(y)]))
    except ValueError:
        pass

    if ymax > 1000:
        plt.subplots_adjust(0.1, 0.16, 0.99, 0.92, 0.2, 0)
    else:
        plt.subplots_adjust(0.07, 0.16, 0.99, 0.92, 0.15, 0)

    return fig