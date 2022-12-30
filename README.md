################################################################################

MariaDB Multi Master DB Replication to a Slave Server With Prometheus & Grafana

################################################################################

- This project sets up a mariadb multi master replication to a single slave node, using on AWS ECS and Ubuntu.

- It also creates the Prometheus and Grafana service applications for monitoring

- This project is using default networking in AWS thus IP assignments are ever changhing everytime the infrastructure are destroyed.
Python scripts are included to automate generation of ansible inventory file and modification of playbooks to take into account new IPs/hostnames.

- Due to script dependencies, the "slave" playbook must be run after the master1 and master2 playbooks had been executed
