import argparse
import socket
from datetime import datetime

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
    args = parser.parse_args()

    host = args.host
    ports = args.ports or range(1,65535)
    timeout = args.timeout

    print("Scanning Host",host,"...")
    start_time = datetime.now()
    print("start time ", start_time)
    for port in ports:
        if port_scan(host,port,timeout):
            print("port",port,"is open")
    

    print("Scanning finished in",datetime.now()-start_time)

if __name__ =="__main__":
    main()