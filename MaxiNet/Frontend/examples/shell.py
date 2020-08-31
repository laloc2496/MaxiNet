#!/usr/bin/python3

#
# This example shows how to use MaxiNet's CommandLineInterface (CLI).
# Using the CLI, commands can be run interactively at emulated hosts.
# Thanks to our build-in py command you can dynamically change the
# topology.
#

from MaxiNet.Frontend import maxinet
from MaxiNet.tools import FatTree

topo = FatTree(2, 10, 0.1)
cluster = maxinet.Cluster(ip="192.168.1.191", port=9090)

exp = maxinet.Experiment(cluster, topo)
exp.setup()

exp.CLI(locals(), globals())


exp.stop()
