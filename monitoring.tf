provider "aws" {
  region     = "us-east-1"
  access_key = "your_access_key"
  secret_key = "your-secret_key"
}

resource "aws_security_group" "ec2" {
  name        = "mariadb-mysql"
  description = "Allow SSH and mysql traffic on EC2 instance"


  ingress {
    description      = "SSH for ec2"
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  ingress {
    description      = "mariadb/mysql"
    from_port        = 3306
    to_port          = 3306
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  ingress {
    description      = "grafana"
    from_port        = 3000
    to_port          = 3000
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  ingress {
    description      = "prometheus"
    from_port        = 9090
    to_port          = 9090
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  ingress {
    description      = "node-exporter"
    from_port        = 9100
    to_port          = 9100
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  tags = {
    Name = "ssh_ec2"
  }
}

resource "aws_instance" "mariadb" {
  # Ubuntu
  ami                    = "ami-0574da719dca65348"
  instance_type          = "t2.micro"
  key_name               = "your_key_name"
  vpc_security_group_ids = [aws_security_group.ec2.id]
  count                  = 3

  tags = {
    Name = "mariadbserver0${count.index}"
  }

  provisioner "local-exec" {
    command = "echo ${self.public_dns} mariadbserver0${count.index} >> ../../../../../git_projects/monitoring/hostnames"
  }

  provisioner "local-exec" {
    command = "echo ${self.public_ip} mariadbserver0${count.index} >> ../../../../../git_projects/monitoring/public_ip"
  }
}

resource "aws_instance" "prome" {
  # Ubuntu
  ami                    = "ami-0574da719dca65348"
  instance_type          = "t2.micro"
  key_name               = "your_key_name"
  vpc_security_group_ids = [aws_security_group.ec2.id]
  count                  = 1

  tags = {
    Name = "prometheus"
  }

  provisioner "local-exec" {
    command = "echo ${self.public_dns} prometheus >> ../../../../../git_projects/monitoring/hostnames"
  }

  provisioner "local-exec" {
    command = "echo ${self.public_ip} prometheus >> ../../../../../git_projects/monitoring/public_ip"
  }
}

resource "aws_instance" "grafana" {
  # Ubuntu
  ami                    = "ami-0574da719dca65348"
  instance_type          = "t2.micro"
  key_name               = "your_key_name"
  vpc_security_group_ids = [aws_security_group.ec2.id]
  count                  = 1

  tags = {
    Name = "grafana"
  }

  provisioner "local-exec" {
    command = "echo ${self.public_dns} grafana >> ../../../../../git_projects/monitoring/hostnames"
  }

  provisioner "local-exec" {
    command = "echo ${self.public_ip} grafana >> ../../../../../git_projects/monitoring/public_ip"
  }
}
