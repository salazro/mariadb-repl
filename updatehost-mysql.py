import os
import re

global datas
datas=['[master1]']
with open('../ansible/playbooks/mysql-rhel9/hosts','r') as fin:
  n_lines=0
  for line in fin:
    n_lines += 1
    if n_lines==2:
        datas.append(line.strip())
        datas.append('[master2]')
    elif n_lines==3:
        datas.append(line.strip())
        datas.append('[slave]')
    elif n_lines==4:
        datas.append(line.strip())
        break
    

for data in datas:
  #print(data)
  os.system("echo " + data + " >> ../ansible/playbooks/mysql-rhel9/hosts")


with open('/mnt/c/Users/rdsal/git_projects/mariadb-repl/master1_redhat.yaml','r') as f:
  content = f.read()
  new_content=re.sub('ec2.*com',datas[1],content)
with open('/mnt/c/Users/rdsal/git_projects/mariadb-repl/master1_redhat.yaml','w') as fo:
  fo.write(new_content)
with open('/mnt/c/Users/rdsal/git_projects/mariadb-repl/master2_redhat.yaml','r') as f:
  content = f.read()
  new_content=re.sub('ec2.*com',datas[3],content)
with open('/mnt/c/Users/rdsal/git_projects/mariadb-repl/master2_redhat.yaml','w') as fo:
  fo.write(new_content)

with open('/mnt/c/Users/rdsal/git_projects/mariadb-repl/slave_redhat.yaml','r') as f:
  content = f.read()
  new_content=re.sub('ec2.*com',datas[5],content)
with open('/mnt/c/Users/rdsal/git_projects/mariadb-repl/slave_redhat.yaml','w') as fo:
  fo.write(new_content)
