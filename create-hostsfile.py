import os
import re

global datas, ips
datas={}
with open('hostnames','r') as fin:
  for line in fin:
    new_value=re.search(('ec2.*com'),line)
    new_value=new_value.group(0)
    new_value=new_value.strip()
    new_key=re.search(('(?<=\s).*'),line)
    new_key=new_key.group(0)
    new_key=new_key.strip()
    datas[new_key]=new_value
    os.system("echo ["+new_key+"] >> hosts")
    os.system("echo "+new_value+" >> hosts")


with open('/mnt/c/Users/rdsal/git_projects/monitoring/master1.yaml','r') as f:
  content = f.read()
  new_content=re.sub('ec2.*com',datas['mariadbserver00'],content)
with open('/mnt/c/Users/rdsal/git_projects/monitoring/master1.yaml','w') as fo:
  fo.write(new_content)
with open('/mnt/c/Users/rdsal/git_projects/monitoring/master2.yaml','r') as f:
  content = f.read()
  new_content=re.sub('ec2.*com',datas['mariadbserver01'],content)
with open('/mnt/c/Users/rdsal/git_projects/monitoring/master2.yaml','w') as fo:
  fo.write(new_content)
with open('/mnt/c/Users/rdsal/git_projects/monitoring/slave.yaml','r') as f:
  content = f.read()
  new_content=re.sub('ec2.*com',datas['mariadbserver02'],content)
with open('/mnt/c/Users/rdsal/git_projects/monitoring/slave.yaml','w') as fo:
  fo.write(new_content)

ips={}
with open('public_ip','r') as fin:
  for line in fin:
    new_value=re.search(('([0-9]{1,3}[\\.]){3}[0-9]{1,3}'),line)
    new_value=new_value.group(0)
    new_value=new_value.strip()
    new_key=re.search(('(?<=\s).*'),line)
    new_key=new_key.group(0)
    new_key=new_key.strip()
    ips[new_key]=new_value


os.system('cp /mnt/c/Users/rdsal/git_projects/monitoring/prometheus_template.yml /mnt/c/Users/rdsal/git_projects/monitoring/prometheus.yml')

with open('/mnt/c/Users/rdsal/git_projects/monitoring/prometheus.yml','r') as f:
  content = f.read()
  new_content=re.sub('mariadbserver00',ips['mariadbserver00'],content)
with open('/mnt/c/Users/rdsal/git_projects/monitoring/prometheus.yml','w') as fo:
  fo.write(new_content)

with open('/mnt/c/Users/rdsal/git_projects/monitoring/prometheus.yml','r') as f:
  content = f.read()
  new_content=re.sub('mariadbserver01',ips['mariadbserver01'],content)
with open('/mnt/c/Users/rdsal/git_projects/monitoring/prometheus.yml','w') as fo:
  fo.write(new_content)

with open('/mnt/c/Users/rdsal/git_projects/monitoring/prometheus.yml','r') as f:
  content = f.read()
  new_content=re.sub('mariadbserver02',ips['mariadbserver02'],content)
with open('/mnt/c/Users/rdsal/git_projects/monitoring/prometheus.yml','w') as fo:
  fo.write(new_content)

with open('/mnt/c/Users/rdsal/git_projects/monitoring/prometheus.yml','r') as f:
  content = f.read()
  new_content=re.sub('grafana',ips['grafana'],content)
with open('/mnt/c/Users/rdsal/git_projects/monitoring/prometheus.yml','w') as fo:
  fo.write(new_content)