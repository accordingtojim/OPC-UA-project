programName = 'create_opcua_client_2'

# Create Test Client Machine 2:

from re import T
from opcua import Client, ua
import time

from opcua.ua.uaprotocol_auto import VariableAttributes
import numpy as np
from opcua.ua.uaerrors import UaError, BadTimeout, BadNoSubscription, BadSessionClosed
from opcua.common.connection import SecureConnection

test = ['ns=2;s=AW24-T4', 'PMC_VEL_I__X2']
if ('GAIN' in test[1]) or ('VEL' in test[1]):
    print('ok')
#print(test1[1])
# print(test2)
# test3 = np.append(test2,test1[1])
# print (test3)