programName = 'create_opcua_client_2'

# Create Test Client Machine 2:
from asyncio.windows_events import NULL
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

#-------------------------------------------------------------
#CONNECTING TO AN OPC-UA SERVER
class Connection:
    def __init__(self,url):
        self.url = url
        self.client = Client(self.url)
        self.root = self.client.get_root_node()
    def set_usr_pwd(self,user, password):
        self.client.set_user(user)
        self.client.set_password(password)
        self.client.connect()
        print("Client Connected to server OK")
def build_opc_tree(node,client):
    nodeClass = node.get_node_class()
    children  = node.get_children()
    node_list = []
    for child in children:
        child_ref = client.get_node(child)
        childClass = child_ref.get_node_class()
        node_list.append([node, nodeClass, child_ref, childClass])
        if childClass == ua.NodeClass.Object:
            build_opc_tree(child_ref,client)
        return node_list

        
connection1 = Connection("opc.tcp://192.168.0.193:59611")
connection1.set_usr_pwd("admin", "admin")
print(build_opc_tree(connection1.root,connection1.client))
# #connection2 = Connection("opc.tcp://192.168.0.193:59611")
# print(connection1.root)
# print(connection1.client)

# #-------------------------------------------------------------
# wb = []
# #EXCEL SHEET MANAGEMENT

# class Sheet_ex:
#     def __init__(self,filepath,rows):
#         self.filepath = filepath
#         self.rows = rows
#         self.wb = Workbook()
#         #filepath = "C:/Users/jimmy.carradore/Documents/GitHub/OPC-UA-project/sample.xlsx"
#         self.wb = load_workbook(filepath)
#         self.sheet = self.wb.active
#         self.counter = 1
#         for i in range(1 , 1000):
#             for j in range (1, rows+1): 
#                 if self.sheet.cell(row = j , column = i).value == '':
#                     return
#                 else: self.sheet.cell(row = j , column = i).value = '' 
#         self.wb.save(filepath) 
#         self.wb.close()
# #ws = wb['test1']

# sheet_1 = Sheet_ex("C:/Users/jimmy.carradore/Documents/GitHub/OPC-UA-project/sample.xlsx",2)


    
# #-----------------------------------------------------------------------------
# #HANDLE PASSWORD AND USER
# def user_password(user,password)


# #--------------------------------------------------------------------------

# flag_string = False
# #debug

# clear_excel()
# s = 2
# i = 1
# try:
#     connection1.client.set_user("admin")
#     connection1.client.set_password("admin")
#     connection1.client.connect()
#     print("Client Connected to server OK")

# #--------------------------------------------------------------------------


#     while True:
#         counter=counter+1
#         s = s + 1
#         # print('#------------------------------------#')
#         # print('#          starting while cycle      #')
#         # print('#------------------------------------#')


#         node_list = []
#         node_dict = {}
#         counter = 1
        

#         build_opc_tree(root1)
#         if flag_string == False:
#             indexes = []
#             for j in range(0 ,len(node_list)-1):
#                 if '.' in str(client1.get_node(node_list[j][2])):
#                     list = str(client1.get_node(node_list[j][2])).split(".")
#                     #debug
#                     if 'AW24-T4' in list[0]:
#                         if ('ALARM' in list[1]) or  ('OPERATOR'in list[1]):
#                             print(list[1])
#                             continue    
#                         else:
#                             indexes.append(j)
#                         sheet.cell(row = 1 , column = i).value = str(list[1])
#                         i = i + 1
#                         wb.save(filepath)
#                 #print(list_deb)
#         #print(indexes)       
#         flag_string = True

#         #print(len(node_list))
#         s = 2
#         for j in indexes:
#             node_ex = client1.get_node(node_list[j][2])
#             sensor_value = node_ex.get_value()
#             sheet.cell(row = s , column = counter).value = sensor_value
#             counter = counter + 1
#         wb.save(filepath) 
        

# except ua.utils.SocketClosedException as ex:
#     print('Exception ua.utils.SocketClosedExceptionoccured while trying to open client session')
#     print('Exception occured while trying to open client session')

# except TimeoutError as ex:
#     print('Exception timeout error')
#     print('Exception is:', ex)

# except (UaError,  BadTimeout, BadNoSubscription, BadSessionClosed) as ex:
#     print('Protocol error')
#     print('Exception is:', ex)

# except Exception as ex:
#     print('Generic Exception occured')
#     print('Exception is: ', ex)
# #-----------------------------------------------------------------------------------------------------------------------------------#
