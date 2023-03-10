import argparse
import socket
from datetime import datetime

    # RED    = '\33[31m'
    # GREEN  = '\33[32m'
    # YELLOW = '\33[33m'
    # BLUE   = '\33[34m'
    # VIOLET = '\33[35m'
    # BEIGE  = '\33[36m'
    # WHITE  = '\33[37m'
    # END      = '\33[0m'

def port_scan(host,port,timeout):
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host,port))
        if result == 0:
            return True
        else:
            return False
    except:
        return False
    

def main():
    parser = argparse.ArgumentParser(description='port Scan')
    parser.add_argument('host', help='target host')
    parser.add_argument('-p','--ports',nargs="+",type=int, help='ports to scan')
    parser.add_argument('-t','--timeout',type=int,default=5,help='connetcct timeout in seconds')
    parser.add_argument('-v','--verbose',help='verbose mode',default= False,type=bool)
    args = parser.parse_args()

    host = args.host
    ports = args.ports or range(1,65535)
    timeout = args.timeout
    verbose = args.verbose
    print(verbose)
    print("Scanning Host",host,"...")
    start_time = datetime.now()
    print("start time ", start_time)
    if verbose:
        
        for port in ports:
            if port_scan(host,port,timeout):
                print(f"port \33[33m {port} \33[0m \33[32mis open\33[0m")
    else:
        Open_ports = []
        for port in ports:
            if port_scan(host,port,timeout):
                Open_ports.append(port)
        for port in Open_ports:
            print("port \33[33m {port} \33[0m \33[32mis open\33[0m")

    print("Scanning finished in",datetime.now()-start_time)

if __name__ =="__main__":
    main()