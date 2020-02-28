import whois_ip as whois  #for asn lookup
import iptables_job as iptables# for shell scripts
import os
import sys
def get_nic_list():
    interface_list=tuple()
    interface_list=tuple(os.listdir('/sys/class/net/'))
    print_nics(interface_list)
    return tuple(interface_list)
def print_nics(nictuple):
    print ("\nYour interface list:")
    for i in range(len(nictuple)):
        print("\t[{}]-->{}".format(i,nictuple[i]))

def ask_for_user():
    iplist=whois.query_whois(input("Enter  only as number 'AS9213=9213':"))
    if iplist != None:
        nc_tuple=get_nic_list()
        print("ip list for entered AS\n",iplist)
        usr_nic=input("Enter the nic number for iptables rule:")
        i_o_=input("DROP or ACCEPT?:")
        if i_o_=="DROP":
            print("Script will DROP all packets in ip list input and output ")
            selection=input("Y/N:")
            if selection=="Y":
                iptables.call_system_job(iplist,nc_tuple[int(usr_nic)],"DROP","OUTPUT")
                iptables.call_system_job(iplist, nc_tuple[int(usr_nic)], "DROP", "INPUT")
            else:
                print_nics("Exitting")
                exit(0)
        elif i_o_=="ACCEPT":
            print("Script will ACCEPT all packets from {} in ip list input and output ".format(nc_tuple[int(usr_nic)]))
            selection = input("Y/N:")
            if selection=="y".lower():
                iptables.call_system_job(iplist, nc_tuple[int(usr_nic)], "ACCEPT", "OUTPUT")
                iptables.call_system_job(iplist, nc_tuple[int(usr_nic)], "ACCEPT", "INPUT")
            else:
                print("Exitting")
                exit(0)
    else:
        raise Exception("whois error")
def _with_args_():
    pass

if __name__ == '__main__':
    if len(sys.argv)<2:
        ask_for_user()
    else:
        _with_args_()