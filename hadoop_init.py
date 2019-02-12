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
def clear(order):
    if order == "yes":
        run("ansible-playbook -i hosts clear_playbook.yml -vv")
    else:
        pass


def run_playbook(MasterType,Secondary_Namenode=False):
    if MasterType == "Master":
        if Secondary_Namenode:
            print "Now is deploying secondary namenode"
            run("ansible-playbook -i hosts SecondaryMaster_playbook.yml -vv")
        else:
            print "Now is deploying Master node"
            run("ansible-playbook -i hosts Master_playbook.yml -vv")
    elif MasterType == "Slave":
        print ("Now is deploying Slave node")
        run("ansible-playbook -i hosts Slave_playbook.yml -vv")
    else:
        sys.exit("The type you enter is Wrong")



if __name__ == "__main__":
    print "Please enter the type of your deploying node (Master or Slave): "
    receive = raw_input()
    run_playbook(receive)
