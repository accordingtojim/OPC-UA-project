programName = 'create_opcua_client_2'

# Create Test Client Machine 2:

from platform import node
from re import T
from opcua import Client, ua
import time

from opcua.ua.uaprotocol_auto import VariableAttributes
import numpy as np
from opcua.ua.uaerrors import UaError, BadTimeout, BadNoSubscription, BadSessionClosed
from opcua.common.connection import SecureConnection
node_list = []
def test(par1):
    node_list.append(par1)

test('giorgio1')
node_list1 = node_list
print(node_list1)
test('giorgio2')
node_list2 = node_list
print(node_list2)


