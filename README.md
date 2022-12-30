######################################################

MariaDB Multi Master DB Replication to a Slave Server

######################################################

- This project sets up a mariadb multi master replication to a single slave node, using on AWS ECS and RHEL9 Linux OS.

- The terraform file builds the EC2 compute host with security group rules for SSH and mysql port 3306/tcp.

- This project is using default networking in AWS thus IP assignments are ever changhing everytime the infrastructure are destroyed.
Python scripts are included to automate generation of ansible inventory file and modification of playbooks to take into account new IPs/hostnames.

- Due to script dependencies, the "slave" playbook must be run after the master1 and master2 playbooks had been executed
