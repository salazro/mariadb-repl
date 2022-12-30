######################################################

MariaDB Multi Master DB replication to a Slave Server
######################################################

- This project setup a mariadb multi master replication to a single slave node, using AWS and RHEL9 Linux OS.

- The terraform file builds the EC2 compute host with security group rules for SSH and mysql port 3306/tcp.

- The terraform scripts also automatically creates the hosts file needed for Ansible.

- I also created a simple python scripts to cleanup the hosts file after every destroy command and update after every apply command on terraform which
is totally optional.

- Master1 and Master ansible yaml files can be run simutalenously.

- Slave ansible yaml file MUST be run after the Master 1 and Master2 scripts are executed due to dependencies.
