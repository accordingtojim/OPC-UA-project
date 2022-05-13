programName = 'create_opcua_client_2'

# Create Test Client Machine 2:
from openpyxl import workbook
from openpyxl.workbook import Workbook
from openpyxl.reader.excel import load_workbook
import openpyxl
from opcua import Client, ua
import time

from opcua.ua.uaprotocol_auto import VariableAttributes

from opcua.ua.uaerrors import UaError, BadTimeout, BadNoSubscription, BadSessionClosed
from opcua.common.connection import SecureConnection

#-----------------------------------------------------------#
# connecting to am OPC-UA server
#-----------------------------------------------------------#

url = "opc.tcp://192.168.0.53:59611"
# url = "opc.tcp://192.168.100.96:4840"
client = Client(url)

try:
    #set connection
    client.set_user("admin")
    client.set_password("admin")
    client.connect()
    print("Client Connected to server OK")
    #-----------------------------------------------------------#
    # browsing nodes om OPC-UA server
    #-----------------------------------------------------------#
    # getting root node of connected OPC server
    root = client.get_root_node()
    print("Root node is: ", str(root))
    ch = root.get_children()
    print('\nroot children = ', ch)

# first case: parent node is known
    object_nodeID = "ns=2;i=86"
    param = client.get_node(object_nodeID)
    print('node param = ', param)
    #print('param node class is: ', param.get_node_class())

    param_children = param.get_children()
    print('param children  = ', param_children)

# then it is possible to ask for values using
# nodeIDs found by get_children() method
# neing sure all the nodes found are variables

    while True:
        print('#-------------------------------------#')
        for x in param_children:
            try:
                dn = x.get_display_name()                    
                bn = x.get_browse_name()
                val = x.get_value()
                print('display_name =', dn)
                print(bn, ' has value ', val)
            except ua.uaerrors._auto.BadWaitingForInitialData:
            #pass
             time.sleep(20)


# following case is when we have a list
# of VariableAttributes
        # node_name = "ns=2;s=2:Pressure"
        # node = client.get_node(node_name)
        # print('node =', node)

        # val = node.get_value()
        # print('val =', val)
        # display_name = node.get_display_name()
        # print('display name =', display_name)
        # bn = node.get_browse_name()
        # print('browse name =', bn)

# varNodeToRead= client.get_node(nodeToRead)
# vall = varNodeToRead.get_data_value() # get value of node as a DataValue object

except ua.utils.SocketClosedException as ex:
    print('Exception ua.utils.SocketClosedExceptionoccured while trying to open client session')
    print('Exception occured while trying to open client session')

except TimeoutError as ex:
    print('Exception timeout error')
    print('Exception is:', ex)

except (UaError,  BadTimeout, BadNoSubscription, BadSessionClosed) as ex:
    print('Protocol error')
    print('Exception is:', ex)

except Exception as ex:
    print('Generic Exception occured')
    print('Exception is: ', ex)







#-----------------------------------------------------------#
# disconnecting to am OPC-UA server
#-----------------------------------------------------------#
client.disconnect()
print("Client Disconnected from server ", url)



#stack overflow full synchronous client / server example:
#https://stackoverflow.com/questions/55025311/opc-ua-client-to-server

#server example github:
#https://github.com/FreeOpcUa/python-opcua/blob/master/examples/server-example.py

#client example github:
#https://github.com/FreeOpcUa/python-opcua/blob/master/examples/client-example.py

