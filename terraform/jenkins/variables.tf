variable "project_name" {
  description = "Project name"
  type        = string
}

variable "environment" {
  description = "Environment name"
  type        = string
}

variable "vpc_id" {
  description = "VPC ID"
  type        = string
}

variable "public_subnet_id" {
  description = "Public subnet ID for Jenkins"
  type        = string
}

variable "ami" {
  description = "AMI ID for Jenkins EC2"
  type        = string
}

variable "instance_type" {
  description = "EC2 instance type for Jenkins"
  type        = string
}

variable "key_name" {
  description = "EC2 key pair name for SSH"
  type        = string
}

variable "allowed_cidr" {
  description = "Your IP address to allow SSH and Jenkins UI access"
  type        = string
}