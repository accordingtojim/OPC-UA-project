programName = 'create_opcua_client_2'

# Create Test Client Machine 2:
from platform import node
from re import S
from openpyxl import workbook
from openpyxl.workbook import Workbook
from openpyxl.reader.excel import load_workbook
import openpyxl

from opcua import Client, ua
import time
from opcua.ua.uaprotocol_auto import VariableAttributes

from opcua.ua.uaerrors import UaError, BadTimeout, BadNoSubscription, BadSessionClosed
from opcua.common.connection import SecureConnection
#from my_library import *
#-----------------------------------------------------------#
# connecting to am OPC-UA server
#-----------------------------------------------------------#

url = "opc.tcp://192.168.0.53:59611"
# url = "opc.tcp://192.168.100.96:4840"
client = Client(url)
client.set_user("admin")
client.set_password("admin")
client.connect()
print("Client Connected to server OK")
#--------------------------------------------------------------------



#--------------------------------------------------------------------------

node = client.get_root_node()
print("Root node is: ", str(node))
# node = root
nodeClass = node.get_node_class()
print('\n#--------------------------------------------------------------#')
print('\nnode', node, 'has class', nodeClass)

node_list = []
node_dict = {}
iter = 0
children  = node.get_children()
print('\tchildren of node', node, '=', len(children))
print('\t', children)
h = 0
for child in children:
    child_ref = client.get_node(child)
    childClass = child_ref.get_node_class()
    print('\t', h, '- child', child_ref, 'has class', childClass)
    node_list.append([node, nodeClass, child_ref, childClass])
    if childClass == ua.NodeClass.Object:
        children = child_ref.get_children()
        print(children)
        for child in children:
            child_ref1 = client.get_node(child)
            childClass = child_ref1.get_node_class()
            print('\t', h, '- child', child_ref1, 'has class', childClass)
            node_list.append([node, nodeClass, child_ref1, childClass])  

        
#--------------------------------------------------------------------------

flag_string = False
i = 0
s = 2
try:
    client.set_user("admin")
    client.set_password("admin")
    client.connect()
    print("Client Connected to server OK")

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
    
   # children = node.get_children()
    #print("Children node are: ",str(children))
    #print("Children node are: ",children[1])
    #child_ref = client.get_node(children[1])
    #print("Child ref is : ",child_ref)
    #childClass = child_ref.get_node_class()
    #print("Child Class is : ",childClass)
    #print(str(childClass==ua.NodeClass.Object))


#------------------------------------------------------------------------

    
#-----------------------------------------------------------------------


    while True:
        counter=counter+1
        # print('#------------------------------------#')
        # print('#          starting while cycle      #')
        # print('#------------------------------------#')


       

        
        #print("NODE LIST IS : ", node_list)
        #print("NODE LIST 2 : ", str(node_list[2]))
        #node_ex=set()
        print('the node list is: ','\t',node_list)
        # for iter in node_list:
        #     #print('\n' , i , iter)
        #     i = i + 1
        # print("node list :", node_list )
        
        
#---------------------------start debug----------------------------------------#

        # node_ex = client.get_node(node_list[182][2])
        # sensor_value = node_ex.get_value()
        # sheet.cell(row = 1 , column = (182)).value = sensor_value
        # wb.save(filepath)
#---------------------------end debug------------------------------------------#
     

        
        #flag_string = True
           
        
        

        #print("node ex is:",str(node_ex))
        #set(node_ex)
        #print("Node value is :",node_ex.get_value())
        # getting root node of connected OPC server
       

        #objects = client.get_objects_node()
        #print("Objects node is: ", objects)


        #root_al = root.get_access_level()
        # print('\nroot access level = ', root_al)

        #ch = root.get_children()
        #print('\nroot children = ', ch)

        #node = client.get_node("ns=2;s=AW24-T4")
        #myNodeChild = node.get_children()
        #print("myNodeChild is: ", myNodeChild)
        #print("number of child nodes: ", len(myNodeChild))

        #time.sleep(1)
        

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
#-----------------------------------------------------------------------------------------------------------------------------------#

