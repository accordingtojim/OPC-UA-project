# -*- coding: UTF-8 -*-

# Author: Roberto Patrizi
# Last update: February 15th, 2022

# OPC UA Client (synchronized)


programName = 'client_opcua_sync'

from my_library import *

from opcua import Client, ua
import concurrent.futures
from opcua.ua.uaprotocol_auto import VariableAttributes

from opcua.ua.uaerrors import UaError, BadTimeout, BadNoSubscription, BadSessionClosed
from opcua.common.connection import SecureConnection

import signal
import atexit
import sys
import os

'''
def build_opc_tree(node):
    nodeClass = node.get_node_class()
    print('\n#--------------------------------------------------------------#')
    print('\nnode', node, 'has class', nodeClass)

    children  = node.get_children()
    print('\tchildren of node', node, '=', len(children))
    print('\t', children)
    # node_list.append([node, nodeClass, child_ref, childClass])
    h = 0
    for child in children:
        child_ref = client.get_node(child)
        childClass = child_ref.get_node_class()
        print('\t', h, '- child', child_ref, 'has class', childClass)
        node_list.append([node, nodeClass, child_ref, childClass])
        h = h + 1
        if childClass == ua.NodeClass.Object:
            build_opc_tree(child_ref)

    return
'''


# setting conditions for abnormal termination
# either by CTRL+C or KILL from command line
class abnormTerm():
    def kill(sig, frame):
        print('\n**** program killed!!!')
        print('**** connections will be closed')
        print('**** and program terminated')
        # client.disconnect()
        # quit()
        sys.exit(0)

    def keyboard(sig, frame):
        print(' n**** program ended by CTRL+C!!!')
        print('**** connections will be closed')
        print('**** and program terminated')
        # client.disconnect()
        # quit()
        sys.exit(0)


atexit.register(abnormTerm.keyboard)
signal.signal(signal.SIGTERM, abnormTerm.keyboard)
signal.signal(signal.SIGINT, abnormTerm.keyboard)

atexit.register(abnormTerm.kill)
signal.signal(signal.SIGTERM, abnormTerm.kill)
signal.signal(signal.SIGINT, abnormTerm.kill)

#-----------------------------------------------------------#
# connecting to am OPC-UA server
#-----------------------------------------------------------#

machines = ['FW-24', 'AW24-T4', 'JW-T2']

# url = "opc.tcp://192.168.1.68:59611"
url = "opc.tcp://192.168.0.53:59611"
client = Client(url)

client.set_user("admin")
client.set_password("admin")
client.connect()
print("Client Connected to server", url)

# getting root node of connected OPC server
root = client.get_root_node()
print("Root node is: ", str(root))

root_children = root.get_children()
print('children number = ', len(root_children))
print('root children are ', root_children)

# following list contains the whole tree of connected opcua server
# each element of the list has the following structure:
#   - parent node
#   - parent nodeClass
#   - node
#   - NodeClass

node_list = []
node_dict = {}

myBuildOpc = imtOpc(node_list, node_dict, machines, client)

myBuildOpc.build_opc_tree(root)

myBuildOpc.build_opc_dict()



# print('node_dict = ', node_dict)

# formatting as json the outDict data structure
#outJsonStr = json.dumps(node_dict, default = str, ensure_ascii=False)

# writing json datasets as input for web client
# with open(opcDir + '/opc_variables' + '.json', "w") as f:
#        f.write(outJsonStr)
#------------------------------------------------------------#
# building variables set in order to get variables values

j = 0
#print('\n#-----------------------------------------------#')
#print(' printing node_list list result\n')

variable_set = set()
for x in node_list:
    print('\t', j, '-', x)
    if x[3] == ua.NodeClass.Variable:
        if ';s=' in str(x[2]):
            variable_set.add(client.get_node(x[2]))
    j = j + 1
#print("variable set is :", variable_set)
print("node list : ", node_list)
h = 0
time_sleeping = 10
while True:
    print('\n#------------------------------------#')
    print('iteration', h)

    try:
        k = 0
        for x in variable_set:
            val = x.get_value()
            print(k, ' -', x, 'value =', val)
            k = k + 1

        time.sleep(time_sleeping)
        h = h + 1

    except TimeoutError as ex:
        print('Exception timeout error')
        print('Exception is:', ex)
        h = h + 1
        time.sleep(30)
        pass
    except (ua.UaError, BadNoSubscription, BadSessionClosed) as ex:
        print('Protocol error')
        print('Exception is:', ex)
        h = h + 1
        time.sleep(30)
        pass
    except ua.utils.SocketClosedException as ex:
        print('Exception ua.utils.SocketClosedExceptionoccured while trying to open client session')
        print('Exception occured while trying to open client session')
        h = h + 1
        time.sleep(30)
        pass

    except Exception as ex:
        print('Generic Exception occured')
        print('Exception is: ', ex)
        h = h + 1
        time.sleep(30)
        pass

    finally:
        client.disconnect()
