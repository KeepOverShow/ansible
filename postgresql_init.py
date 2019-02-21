#!/usr/bin/python
# -*- encoding: utf-8 -*-
import json
import subprocess
import sys
import getopt

variables = ['is_Master','is_Slave']

def run(cmd,ignore_error=False):
    ret = subprocess.call(cmd,shell=True)
    if not ignore_error and ret != 0:
        sys.exit('Exec command: %s error, return value: %s' % (cmd, str(ret)))
    return ret

#def prepare(hosts):
#    if run("ansible --version", ignore_error=True):
#        run("yum install -y ./ansible_rpms/*")
#    run("rm -rf /root/.ssh/")
#    run("cat /dev/zero | ssh-keygen -q -N ''")
#    for i in hosts:
#        run("ssh-copy-id -i /root/.ssh/id_rsa root@" + i)
def install(order):
    if order == "yes":
        run("ansible-playbook -i hosts -s postgresql.yml -vv")
    else:
        pass

if __name__ == "__main__":
    print "Install postgresql?(yes or not)"
    ord = raw_input()
    install(ord)

