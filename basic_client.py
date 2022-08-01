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

class Node_AW:
        def __init__(self,node_name):
                self.machine_name = "ns=2;s=AW24-T4."
                self.node_name = node_name
                self.val = self.machine_name + node_name
                self.node = client.get_node(self.val)
        def print_val(self):
                valttt = self.node.get_value()
                print(self.node_name,'val =', valttt)
#---------------------------------------------------------------------------
class Node_JW:
        def __init__(self,node_name):
                self.machine_name = "ns=2;s=JW-T2."
                self.node_name = node_name
                self.val = self.machine_name + node_name
                self.node = client.get_node(self.val)
        def print_val(self):
                valttt = self.node.get_value()
                print(self.node_name, 'val =', valttt)
                
var1 = Node_AW('PMC_RAPID_X1')        #183201 CN1
var2 = Node_AW('PMC_SVNETPW[2]')        #183202 CN1
var3 = Node_AW('PMC_SVNETPW[3]')        #183201 CN2
var4 = Node_AW('PMC_SVNETPW[4]')        #183202 CN2
var5 = Node_AW('TEST1')                 #183203 CN1
var6 = Node_AW('TEST2')                 #183204 CN1
var7 = Node_AW('CN_MACHINING_START')
var8 = Node_AW('CN1_STATUS_OPERATION')
var9 = Node_AW('CN1_STATUS_MODE')
var10 = Node_AW('CN1_STATUS_EMERGENCY')
var11 = Node_AW('PMC_ACT_POW_X1')
var12 = Node_AW('PMC_ACT_POW_X2')
var13 = Node_AW('PMC_ACT_POW_Z1')
var14 = Node_AW('PMC_ACT_POW_Z2')
var15 = Node_AW('CN1_ACT_PRG_NUM')
var17 = Node_AW('CN1_PRG_COMMENT')
var18 = Node_AW('CN2_PRG_COMMENT')

var16 = Node_JW('PMC_ACT_POW_X1')
var19 = Node_JW('CN1_PRG_COMMENT')


try:
        client.set_user("admin")
        client.set_password("admin")
        client.connect()
        print("Client Connected to server OK")
        root = client.get_root_node()
        print("Root node is: ", str(root))
        objects = client.get_objects_node()
        print("Objects node is: ", objects)

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


while True:
        print('#------------------------------------#')
        print('#          starting while cycle      #')
        print('#------------------------------------#')
        print('AW24-T4 variables   ')
        #var1.print_val()        #ASSE 1 CN1
        #var2.print_val()        #ASSE 2 CN1
        #var5.print_val()       
        var9.print_val()        
        #var3.print_val()        
        #var17.print_val()
        #var8.print_val()
        #var9.print_val()
        var17.print_val()
        var18.print_val()
        
        print('JW-T2 variables   ')
        #var16.print_val()
        var19.print_val()
        # node_name = "ns=2;s=AW24-T4.PMC_ACT_POW_Z1"
        # node = client.get_node(node_name)
        # valttt = node.get_value()
        # print('val =', valttt)
        # var11.print_val()
        #var12.print_val()   
        #var13.print_val()
        #var14.print_val()
        #var15.print_val()
        
        #time.sleep(1)



