import os
import socket
def get_dns_to_ip(domain_name):#unused for now
    return (socket.gethostbyname(str(domain_name)))
def query_whois(as_number):
    ip_list=list()
    try:
        ip_list=os.popen("whois -h whois.radb.net '!gas"+str(int(as_number))+"'").read() #get ip list from sheel with whois
        return (parse_output(ip_list))
    except:
        print("Error(invalid as number)")
def parse_output(ip_list):
    try:
        ip_list=ip_list.split(" ")
        ip_list[1]=ip_list[1].split("\n")
        ip_list[len(ip_list)-1]=ip_list[len(ip_list)-1].split("\n")
        ip_list.append(ip_list[1][len(ip_list[1])-1])
        ip_list.append(ip_list[len(ip_list)-2][0])
        del ip_list[0:2]
        del ip_list[len(ip_list)-3]
        return ip_list
    except:
        print("An error occurred when parsing the data(As number can be invalid)")

