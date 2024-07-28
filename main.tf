provider "aws" {
  region = "us-east-1"
}

resource "aws_security_group" "web_server" {
  name_prefix = "web-server-sg"

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "web_server" {
  ami           = "ami-12345678" # Replace with a valid AMI
  instance_type = "t2.micro"
  key_name      = "my-key"

  security_groups = [aws_security_group.web_server.name]

  tags = {
    Name = "WebServer"
  }
}
