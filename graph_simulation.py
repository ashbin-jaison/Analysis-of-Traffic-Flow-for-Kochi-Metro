# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 12:36:31 2020

@author: ME
"""
import random
import numpy as np 
import networkx as nx

G = nx.MultiDiGraph()

entry_12_1 = [63972,5484,4815,3209,5410,14933,14738,6678,48031,12036,13880,14720,18785,24404,23921,36162,23471,16139,8072,17314,29225]


stations = ["ALVA","PNCU","CPPY","AATK","MUTT","KLMT","CCUV","PDPM","EDAP","CGPP","PARV","JLSD","KALR","LSSE","MGRD","MACE","ERSH","KVTR","EMKM","VYTA","TKDM"]
stations_alva = ["PNCU","CPPY","AATK","MUTT","KLMT","CCUV","PDPM","EDAP","CGPP","PARV","JLSD","KALR","LSSE","MGRD","MACE","ERSH","KVTR","EMKM","VYTA","TKDM"]
stations_pncu = ["ALVA","CPPY","AATK","MUTT","KLMT","CCUV","PDPM","EDAP","CGPP","PARV","JLSD","KALR","LSSE","MGRD","MACE","ERSH","KVTR","EMKM","VYTA","TKDM"]
stations_cppy = ["ALVA","PNCU","AATK","MUTT","KLMT","CCUV","PDPM","EDAP","CGPP","PARV","JLSD","KALR","LSSE","MGRD","MACE","ERSH","KVTR","EMKM","VYTA","TKDM"]
stations_aatk = ["ALVA","PNCU","CPPY","MUTT","KLMT","CCUV","PDPM","EDAP","CGPP","PARV","JLSD","KALR","LSSE","MGRD","MACE","ERSH","KVTR","EMKM","VYTA","TKDM"]
stations_mutt = ["ALVA","PNCU","CPPY","AATK","KLMT","CCUV","PDPM","EDAP","CGPP","PARV","JLSD","KALR","LSSE","MGRD","MACE","ERSH","KVTR","EMKM","VYTA","TKDM"]
stations_klmt = ["ALVA","PNCU","CPPY","AATK","MUTT","CCUV","PDPM","EDAP","CGPP","PARV","JLSD","KALR","LSSE","MGRD","MACE","ERSH","KVTR","EMKM","VYTA","TKDM"]
stations_ccuv = ["ALVA","PNCU","CPPY","AATK","MUTT","KLMT","PDPM","EDAP","CGPP","PARV","JLSD","KALR","LSSE","MGRD","MACE","ERSH","KVTR","EMKM","VYTA","TKDM"]
stations_pdpm = ["ALVA","PNCU","CPPY","AATK","MUTT","KLMT","CCUV","EDAP","CGPP","PARV","JLSD","KALR","LSSE","MGRD","MACE","ERSH","KVTR","EMKM","VYTA","TKDM"]
stations_edap = ["ALVA","PNCU","CPPY","AATK","MUTT","KLMT","CCUV","PDPM","CGPP","PARV","JLSD","KALR","LSSE","MGRD","MACE","ERSH","KVTR","EMKM","VYTA","TKDM"]
stations_cgpp = ["ALVA","PNCU","CPPY","AATK","MUTT","KLMT","CCUV","PDPM","EDAP","PARV","JLSD","KALR","LSSE","MGRD","MACE","ERSH","KVTR","EMKM","VYTA","TKDM"]
stations_parv = ["ALVA","PNCU","CPPY","AATK","MUTT","KLMT","CCUV","PDPM","EDAP","CGPP","JLSD","KALR","LSSE","MGRD","MACE","ERSH","KVTR","EMKM","VYTA","TKDM"]
stations_jlsd = ["ALVA","PNCU","CPPY","AATK","MUTT","KLMT","CCUV","PDPM","EDAP","CGPP","PARV","KALR","LSSE","MGRD","MACE","ERSH","KVTR","EMKM","VYTA","TKDM"]
stations_kalr = ["ALVA","PNCU","CPPY","AATK","MUTT","KLMT","CCUV","PDPM","EDAP","CGPP","PARV","JLSD","LSSE","MGRD","MACE","ERSH","KVTR","EMKM","VYTA","TKDM"]
stations_lsse = ["ALVA","PNCU","CPPY","AATK","MUTT","KLMT","CCUV","PDPM","EDAP","CGPP","PARV","JLSD","KALR","MGRD","MACE","ERSH","KVTR","EMKM","VYTA","TKDM"]
stations_mgrd = ["ALVA","PNCU","CPPY","AATK","MUTT","KLMT","CCUV","PDPM","EDAP","CGPP","PARV","JLSD","KALR","LSSE","MACE","ERSH","KVTR","EMKM","VYTA","TKDM"]
stations_mace = ["ALVA","PNCU","CPPY","AATK","MUTT","KLMT","CCUV","PDPM","EDAP","CGPP","PARV","JLSD","KALR","LSSE","MGRD","ERSH","KVTR","EMKM","VYTA","TKDM"]
stations_ersh = ["ALVA","PNCU","CPPY","AATK","MUTT","KLMT","CCUV","PDPM","EDAP","CGPP","PARV","JLSD","KALR","LSSE","MGRD","MACE","KVTR","EMKM","VYTA","TKDM"]
stations_kvtr = ["ALVA","PNCU","CPPY","AATK","MUTT","KLMT","CCUV","PDPM","EDAP","CGPP","PARV","JLSD","KALR","LSSE","MGRD","MACE","ERSH","EMKM","VYTA","TKDM"]
stations_emkm = ["ALVA","PNCU","CPPY","AATK","MUTT","KLMT","CCUV","PDPM","EDAP","CGPP","PARV","JLSD","KALR","LSSE","MGRD","MACE","ERSH","KVTR","VYTA","TKDM"]
stations_vyta = ["ALVA","PNCU","CPPY","AATK","MUTT","KLMT","CCUV","PDPM","EDAP","CGPP","PARV","JLSD","KALR","LSSE","MGRD","MACE","ERSH","KVTR","EMKM","TKDM"]
stations_tkdm = ["ALVA","PNCU","CPPY","AATK","MUTT","KLMT","CCUV","PDPM","EDAP","CGPP","PARV","JLSD","KALR","LSSE","MGRD","MACE","ERSH","KVTR","EMKM","VYTA"]



exit_12_1 = [44760,3572,3434,2553,4910,11411,9821,5943,100058,9609,13785,10509,13906,22216,30964,39010,22259,13121,5380,18885,18341]


weights = []
for i in entry_12_1:
    weights.append(i/sum(entry_12_1))

d = np.random.choice(stations,size=10000,p=weights)

weights_alva = []
for j in exit_12_1:
    weights_alva.append(j/(sum(exit_12_1)-exit_12_1[0]))
weights_alva.remove(weights_alva[0])

weights_pncu = []
for j in exit_12_1:
    weights_pncu.append(j/(sum(exit_12_1)-exit_12_1[1]))
weights_pncu.remove(weights_pncu[1])

weights_cppy = []
for j in exit_12_1:
    weights_cppy.append(j/(sum(exit_12_1)-exit_12_1[2]))
weights_cppy.remove(weights_cppy[2])

weights_aatk = []
for j in exit_12_1:
    weights_aatk.append(j/(sum(exit_12_1)-exit_12_1[3]))
weights_aatk.remove(weights_aatk[3])

weights_mutt = []
for j in exit_12_1:
    weights_mutt.append(j/(sum(exit_12_1)-exit_12_1[4]))
weights_mutt.remove(weights_mutt[4])

weights_klmt = []
for j in exit_12_1:
    weights_klmt.append(j/(sum(exit_12_1)-exit_12_1[5]))
weights_klmt.remove(weights_klmt[5])

weights_ccuv = []
for j in exit_12_1:
    weights_ccuv.append(j/(sum(exit_12_1)-exit_12_1[6]))
weights_ccuv.remove(weights_ccuv[6])

weights_pdpm = []
for j in exit_12_1:
    weights_pdpm.append(j/(sum(exit_12_1)-exit_12_1[7]))
weights_pdpm.remove(weights_pdpm[7])

weights_edap = []
for j in exit_12_1:
    weights_edap.append(j/(sum(exit_12_1)-exit_12_1[8]))
weights_edap.remove(weights_edap[8])

weights_cgpp = []
for j in exit_12_1:
    weights_cgpp.append(j/(sum(exit_12_1)-exit_12_1[9]))
weights_cgpp.remove(weights_cgpp[9])

weights_parv = []
for j in exit_12_1:
    weights_parv.append(j/(sum(exit_12_1)-exit_12_1[10]))
weights_parv.remove(weights_parv[10])

weights_jlsd = []
for j in exit_12_1:
    weights_jlsd.append(j/(sum(exit_12_1)-exit_12_1[11]))
weights_jlsd.remove(weights_jlsd[11])

weights_kalr = []
for j in exit_12_1:
    weights_kalr.append(j/(sum(exit_12_1)-exit_12_1[12]))
weights_kalr.remove(weights_kalr[12])

weights_twnh = []
for j in exit_12_1:
    weights_twnh.append(j/(sum(exit_12_1)-exit_12_1[13]))
weights_twnh.remove(weights_twnh[13])

weights_mgrd = []
for j in exit_12_1:
    weights_mgrd.append(j/(sum(exit_12_1)-exit_12_1[14]))
weights_mgrd.remove(weights_mgrd[14])

weights_mace = []
for j in exit_12_1:
    weights_mace.append(j/(sum(exit_12_1)-exit_12_1[15]))
weights_mace.remove(weights_mace[15])

weights_ersh = []
for j in exit_12_1:
    weights_ersh.append(j/(sum(exit_12_1)-exit_12_1[16]))
weights_ersh.remove(weights_ersh[16])

weights_kvtr = []
for j in exit_12_1:
    weights_kvtr.append(j/(sum(exit_12_1)-exit_12_1[17]))
weights_kvtr.remove(weights_kvtr[17])

weights_emkm = []
for j in exit_12_1:
    weights_emkm.append(j/(sum(exit_12_1)-exit_12_1[18]))
weights_emkm.remove(weights_emkm[18])

weights_vyta = []
for j in exit_12_1:
    weights_vyta.append(j/(sum(exit_12_1)-exit_12_1[19]))
weights_vyta.remove(weights_vyta[19])

weights_tkdm = []
for j in exit_12_1:
    weights_tkdm.append(j/(sum(exit_12_1)-exit_12_1[20]))
weights_tkdm.remove(weights_tkdm[20])


G.add_nodes_from(stations)
l = []
for i in d.tolist():
    if i=="ALVA":
        r = np.random.choice(stations_alva,1,p=weights_alva)
        l.append((i,r.tolist()[0]))
G.add_edges_from(l)

l = []
for i in d.tolist():
    if i=="PNCU":
        r = np.random.choice(stations_pncu,1,p=weights_pncu)
        l.append((i,r.tolist()[0]))
G.add_edges_from(l)

l = []
for i in d.tolist():
    if i=="CPPY":
        r = np.random.choice(stations_cppy,1,p=weights_cppy)
        l.append((i,r.tolist()[0]))
G.add_edges_from(l)

l = []
for i in d.tolist():
    if i=="AATK":
        r = np.random.choice(stations_aatk,1,p=weights_aatk)
        l.append((i,r.tolist()[0]))
G.add_edges_from(l)

l = []
for i in d.tolist():
    if i=="MUTT":
        r = np.random.choice(stations_cppy,1,p=weights_cppy)
        l.append((i,r.tolist()[0]))
G.add_edges_from(l)

l = []
for i in d.tolist():
    if i=="KLMT":
        r = np.random.choice(stations_klmt,1,p=weights_klmt)
        l.append((i,r.tolist()[0]))
G.add_edges_from(l)

l = []
for i in d.tolist():
    if i=="CCUV":
        r = np.random.choice(stations_ccuv,1,p=weights_ccuv)
        l.append((i,r.tolist()[0]))
G.add_edges_from(l)

l = []
for i in d.tolist():
    if i=="PDPM":
        r = np.random.choice(stations_pdpm,1,p=weights_pdpm)
        l.append((i,r.tolist()[0]))
G.add_edges_from(l)

l = []
for i in d.tolist():
    if i=="EDAP":
        r = np.random.choice(stations_edap,1,p=weights_edap)
        l.append((i,r.tolist()[0]))
G.add_edges_from(l)

l = []
for i in d.tolist():
    if i=="CGPP":
        r = np.random.choice(stations_cgpp,1,p=weights_cgpp)
        l.append((i,r.tolist()[0]))
G.add_edges_from(l)

l = []
for i in d.tolist():
    if i=="PARV":
        r = np.random.choice(stations_parv,1,p=weights_parv)
        l.append((i,r.tolist()[0]))
G.add_edges_from(l)

l = []
for i in d.tolist():
    if i=="JLSD":
        r = np.random.choice(stations_jlsd,1,p=weights_jlsd)
        l.append((i,r.tolist()[0]))
G.add_edges_from(l)

l = []
for i in d.tolist():
    if i=="KALR":
        r = np.random.choice(stations_kalr,1,p=weights_kalr)
        l.append((i,r.tolist()[0]))
G.add_edges_from(l)
l = []
for i in d.tolist():
    if i=="LSSE":
        r = np.random.choice(stations_lsse,1,p=weights_twnh)
        l.append((i,r.tolist()[0]))
G.add_edges_from(l)

l = []
for i in d.tolist():
    if i=="MGRD":
        r = np.random.choice(stations_mgrd,1,p=weights_mgrd)
        l.append((i,r.tolist()[0]))
G.add_edges_from(l)

l = []
for i in d.tolist():
    if i=="MACE":
        r = np.random.choice(stations_mace,1,p=weights_mace)
        l.append((i,r.tolist()[0]))
G.add_edges_from(l)

l = []
for i in d.tolist():
    if i=="ERSH":
        r = np.random.choice(stations_ersh,1,p=weights_ersh)
        l.append((i,r.tolist()[0]))
G.add_edges_from(l)

l = []
for i in d.tolist():
    if i=="KVTR":
        r = np.random.choice(stations_kvtr,1,p=weights_kvtr)
        l.append((i,r.tolist()[0]))
G.add_edges_from(l)

l = []
for i in d.tolist():
    if i=="EMKM":
        r = np.random.choice(stations_emkm,1,p=weights_emkm)
        l.append((i,r.tolist()[0]))
G.add_edges_from(l)

l = []
for i in d.tolist():
    if i=="VYTA":
        r = np.random.choice(stations_vyta,1,p=weights_vyta)
        l.append((i,r.tolist()[0]))
G.add_edges_from(l)

l = []
for i in d.tolist():
    if i=="TKDM":
        r = np.random.choice(stations_tkdm,1,p=weights_tkdm)
        l.append((i,r.tolist()[0]))
G.add_edges_from(l)

#nx.draw(G,with_label=True)
in_degree = nx.in_degree_centrality(G)
out_degree = nx.out_degree_centrality(G)
betweenness = nx.betweenness_centrality(G)

ranked_in_degree = list(reversed(sorted((value, node) for (node, value) in in_degree.items())))
ranked_out_degree = list(reversed(sorted((value, node) for (node, value) in out_degree.items())))
betweenness_ranked = list(reversed(sorted((value, node) for (node, value) in betweenness.items())))