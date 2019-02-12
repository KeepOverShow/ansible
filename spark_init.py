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

def run_playbook(target):
    if target == "spark":
            print "Now is deploying secondary namenode"
            run("ansible-playbook -i hosts spark_playbook.yml -vv")
    else:
        sys.exit("The type you enter is Wrong")



if __name__ == "__main__":
    print "Please enter the type of your deploying node (default spark): "
    receive = raw_input()
    run_playbook(receive)

