import os
import re

global datas
datas=[]
with open('/mnt/c/Users/rdsal/git_projects/mariadb-repl/hosts','r') as fin:
  n_lines=0
  for line in fin:
    n_lines += 1
    if n_lines==1:
        datas.append(line.strip())
        datas.append('[master2]')
    elif n_lines==2:
        datas.append(line.strip())
        datas.append('[slave]')
    elif n_lines==3:
        datas.append(line.strip())
        break
    
os.system("echo [master1] > /mnt/c/Users/rdsal/git_projects/mariadb-repl/hosts")
for data in datas:
  #print(data)
  os.system("echo " + data + " >> /mnt/c/Users/rdsal/git_projects/mariadb-repl/hosts")


with open('/mnt/c/Users/rdsal/git_projects/mariadb-repl/master1_redhat.yaml','r') as f:
  content = f.read()
  new_content=re.sub('ec2.*com',datas[0],content)
with open('/mnt/c/Users/rdsal/git_projects/mariadb-repl/master1_redhat.yaml','w') as fo:
  fo.write(new_content)
with open('/mnt/c/Users/rdsal/git_projects/mariadb-repl/master2_redhat.yaml','r') as f:
  content = f.read()
  new_content=re.sub('ec2.*com',datas[2],content)
with open('/mnt/c/Users/rdsal/git_projects/mariadb-repl/master2_redhat.yaml','w') as fo:
  fo.write(new_content)

with open('/mnt/c/Users/rdsal/git_projects/mariadb-repl/slave_redhat.yaml','r') as f:
  content = f.read()
  new_content=re.sub('ec2.*com',datas[4],content)
with open('/mnt/c/Users/rdsal/git_projects/mariadb-repl/slave_redhat.yaml','w') as fo:
  fo.write(new_content)
