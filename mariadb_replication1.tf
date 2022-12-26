provider "aws" {
  region     = "us-east-1"
  access_key = "your_access_key"
  secret_key = "your_secret_key"
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

resource "aws_instance" "myec2" {
  ami                    = "ami-08e637cea2f053dfa"
  instance_type          = "t2.micro"
  key_name               = "AWSkey"
  vpc_security_group_ids = [aws_security_group.ec2.id]
  count                  = 3

  tags = {
    Name = "mariadb-server-0${count.index}"
  }

  provisioner "local-exec" {
    # Added this line to auto create my ansible host file when testing with AWS setup
    command = "echo ${self.public_dns} >> ../../ansible/playbooks/mysql-rhel9/hosts"
  }
}

