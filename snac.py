from scapy.all import ARP , Ether , srp

def scan(ip):
    arp_req = ARP(pdat=ip)
    brdcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    abro = brdcast/arp_req
    res = srp(abro,timeout=5,verbose=fales)[0]
    print(res)
    lst = []
    for elment in res:
        clint = ("ip":elment[1].psrc,"mac":elment[1.hwsrc])
        lst.append(clint)
        print ("ip /t/t/t/t mac")
        print ("___________________________")
        for i in lst:
            print ("{} /t/t/t/t {} ".format(i["IP"].i["mac"]))
            
ip = input()
scan(ip)
