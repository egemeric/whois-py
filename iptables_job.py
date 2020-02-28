import os
def system_job(interface_sys,ip,mode,i_o): #bad interface_sys call
    if mode=="DROP" and i_o=="INPUT":
        os.system("sudo /sbin/iptables -I INPUT -i "+ interface_sys +" -s "+ ip +" -j DROP")
    elif mode=="ACCEPT" and i_o=="INPUT":
        os.system("sudo /sbin/iptables -I INPUT -i " + interface_sys + " -s " + ip + " -j ACCEPT")
    elif mode=="DROP" and i_o=="OUTPUT":
        os.system("sudo /sbin/iptables -I OUTPUT -s " + ip + " -j DROP")
    elif mode=="ACCEPT" and i_o=="OUTPUT":
        os.system("sudo /sbin/iptables -I OUTPUT -s " + ip + " -j ACCEPT")
    else:
        print("mode error")
def call_system_job(iplist,interface_sys,mode,i_o):
    i = len(iplist)
    for ip in iplist:
        system_job(interface_sys,ip,mode,i_o)
        i=i-1
        print("wait until to 0 ->({})".format(i))


