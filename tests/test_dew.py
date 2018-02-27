# -*- coding: utf-8 -*-
"""
EDD DEW TO DiTTo Conversion

Created on Mon Aug 20 20:18:01 2017

@author: Abilash Thakallapelli

Developed based on EDD DEW Version V10.62.0
"""

from __future__ import absolute_import, division, print_function
from builtins import super, range, zip, round, map

import os
from ditto.readers.dew.read import reader
from ditto.store import Store
from ditto.writers.opendss.write import writer


def test_dew_reader_writer():
    # TODO: Remove hardcoded paths
    dew_models_dir = os.path.abspath(os.path.join('../ditto/readers/DEW/Models'))
    dew_database_dir = os.path.abspath(os.path.join('../ditto/readers/DEW/DataBase'))

    modelfile = 'IEEE-13.dew' #IEEE 13Bus System

    # database read
    databasename = 'DataBase.xlsx'
    inputfile = open(os.path.join(dew_models_dir, modelfile), 'r')
    databasepath = os.path.join(dew_database_dir, databasename)
    m = Store()
    reader = reader()
    reader.parse(m, inputfile, databasepath)
    writer = writer(linecodes_flag=True, output_path=os.path.abspath('../ditto/readers/DEW/Models/IEEE_13_node_output/'))
    writer.write(m, verbose=True)