programName = 'create_opcua_client_2'

# Create Test Client Machine 2:

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

def get_values(self, nodes):
      
 nodes = [node.nodeid for node in nodes]
 results = self.uaclient.get_attributes(nodes, ua.AttributeIds.Value)
 return [result.Value.Value for result in results]


try:
    client.set_user("admin")
    client.set_password("admin")
    client.connect()
    print("Client Connected to server OK")
    # Client has a few methods to get proxy to UA nodes that should always be in address space such as Root or Objects
    root = client.get_root_node()
    print("Objects node is: ", root)

    # Node objects have methods to read and write node attributes as well as browse or populate address space
    print("Children of root are: ", root.get_children())
    

    # client.connect_socket()
    # cfs = client.connect_and_find_servers()
    # print("Client Socket Connected to server OK")
    # print("we got:", cfs)

    # uri = "FANUCOPC.SERVER.0"
    # idx = client.get_namespace_index(uri)
    # print('idx = ', idx)

    # client.create_session()
    # print("Client Session created")

    # client.activate_session(username='admin', password='admin', certificate=None)
    # print("Client Session activated")

    while True:
        print('#------------------------------------#')
        print('#          starting while cycle      #')
        print('#------------------------------------#')
        # getting root node of connected OPC server
        
        #root = client.get_root_node()
        #print("Root node is: ", str(root))

        #objects = client.get_objects_node()
        #print("Objects node is: ", objects)

        #node_name = "ns=2;s=AW24-T4"
        #node = client.get_node(node_name)
        #print('\nparent node =', node)

        
        node = client.get_node( "ns=2;s=AW24-T4.PMC_PULSECODE_TEMP_X1")
        print('\nnode =', node)
        val = node.get_value()
        print('val =', val)

        #root_al = root.get_access_level()
        # print('\nroot access level = ', root_al)

        ch = root.get_children()
        print('\nroot children = ', ch)   
        time.sleep(1)

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