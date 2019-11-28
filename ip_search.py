# -*- coding: cp949 -*-
import sys
import os
import os.path
import re

file_path = raw_input('File_Path : ')

# path
def abs_path():
    path = os.path.dirname(os.path.abspath(__file__))
    return (path)    

def ip_result(ip_list):
    with open("ip_list.log", "w") as f2:
        for result in ip_list:
            f2.write("%s\n" % result)

if __name__=="__main__":
    # IP regex
    ip_regex = re.compile(r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b')

# file_path = search file name
with open(file_path, "r") as f1:
    text = f1.read()

    ip_list = ip_regex.findall(text)
    ip_list = list(set(ip_list))
    ip_list.remove('255.255.255.0')
    ip_list.remove('0.0.0.0')
    ip_list.sort()
    print("Searching . . .")
    ip_result(ip_list)
    print("End")