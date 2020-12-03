#!/usr/bin/env python

import sys
import socket as sk

def portscanner(portA, portB, IP):
    for port in range(int(portA), int(portB)):
        try:
            s=sk.socket(sk.AF_INET,sk.SOCK_STREAM)
            s.settimeout(1000)
            s.connect((str(IP),port))
            print ('%d:OPEN' % (port))
            s.close
        except: continue

if __name__ == '__main__':
    if (sys.argv[1] == '--h' or sys.argv[1] == '-h' or sys.argv[1] == '--help'):
        print('Portscanner usage:')
        print('python3 main.py portRangeStart portRangeEnd IPaddress')
        print(' ')
        print('-----------------------------------------------------')
        print('Timeout set to 1000ms.')
    elif len(sys.argv) != 4:
        print('[ERROR] Exactly three arguments required')
        print('[INFO] Terminating script.')
    else:
        print('Scanning ports from ' + sys.argv[1] + ' to ' + sys.argv[2] + ' from ' + sys.argv[3])
        portscanner(sys.argv[1], sys.argv[2], sys.argv[3])
