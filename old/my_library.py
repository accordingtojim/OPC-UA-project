# this class contains methods useful for handling log activities
#---------------------------------------------------------------------#
#                python overall library importing                     #
#---------------------------------------------------------------------#

# from typing_extensions import Self
from email import header
from multiprocessing.sharedctypes import Value
# from Conformed import *

import datetime
import time
import csv
import glob
import os
import sys
import itertools
import subprocess
from socket import *
from functools import reduce

from opcua import Client, ua
from opcua.ua.uaprotocol_auto import VariableAttributes
from opcua.ua.uaerrors import UaError, BadTimeout, BadNoSubscription, BadSessionClosed
from opcua.common.connection import SecureConnection

import logging
from logging import *
import logging.handlers

import re
import copy as cp
import random as Random
import json
from typing import Iterable

from opcua import Client, ua
from opcua.ua.uaprotocol_auto import VariableAttributes
from opcua.ua.uaerrors import UaError, BadTimeout, BadNoSubscription, BadSessionClosed
from opcua.common.connection import SecureConnection

#------------------------------------------#
# importing sql module classes
#------------------------------------------#
# from pyspark.sql import SparkSession
# from pyspark.sql import *
# from pyspark.sql import functions as F
# from pyspark.sql.types import *
# from pyspark.sql.window import Window as W

#----------------------------------#

class imtOpc():
    def __init__(self, node_list, node_dict, machines, client):
        self.node_list = node_list
        self.node_dict = node_dict
        self.machines = machines
        self.client = client
        return

    def build_opc_tree(self, node):
        nodeClass = node.get_node_class()
        print('\n#--------------------------------------------------------------#')
        print('\nnode', node, 'has class', nodeClass)

        children  = node.get_children()
        #print('\tchildren of node', node, '=', len(children))
        #print('\t', children)
        h = 0
        for child in children:
            child_ref = self.client.get_node(child)
            childClass = child_ref.get_node_class()
            #print('\t', h, '- child', child_ref, 'has class', childClass)
            self.node_list.append([node, nodeClass, child_ref, childClass])
            h = h + 1
            if childClass == ua.NodeClass.Object:
                self.build_opc_tree(child_ref)

        return

    def build_opc_dict(self):
        print('\n#------------------------------------------#')
        print('#    building OPC variables by machineID       #')
        for y in self.machines:
            h = 0
            variables = []
            for x in self.node_list:
                pos = None
                pos = re.search(y, str(x[2]))
                if pos is not None and x[3] == ua.NodeClass.Variable:
                    i0 = re.search(y, str(x[2])).span()[1] + 1
                    print(h, ' - ', y, ' - ', str(x[2])[i0:])
                    variables.append([str(x[2])[i0:], x[2]])
                    h = h + 1
            self.node_dict.update({y:variables})

        return

