import socket
import sys
m_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
m_socket.settimeout(5)

host = socket.gethostbyname('bungabet.ug')#'104.16.140.23'
open_ports = []



try:
    for port in range(80,85):
        print('----Checking :...host..['+host+']-----for status of port ---['+str(port)+']....')
        if m_socket.connect_ex((host,port)) == 0 :
            print('--- port..['+str(port)+'].... is open')
            open_ports.append(port)
        else :
            print('--- port..['+str(port)+'].... is Closed')
except KeyboardInterrupt:
    print('You presses CTRL+C')
    sys.exit()
        
        
    

print(open_ports)       
    
        
        
    
        


    



    

