variable "project_name" {
  description = "Project name"
  type        = string
}

variable "environment" {
  description = "Environment name"
  type        = string
}

variable "region" {
  description = "AWS region for deploy"
  type        = string
}

variable "vpc_cidr" {
  description = "VPC CIDR"
  type        = string
}

variable "public_subnet_cidrs" {
  description = "Public Subnet CIDRS Mapped to Availability Zones"
  type        = map(string)
}

variable "private_subnet_cidrs" {
  description = "Private Subnet CIDRS Mapped to Availability Zones"
  type        = map(string)
}

variable "eks_instance_type" {
  description = "EC2 instance type for EKS nodes"
  type        = string
}

variable "eks_desired_size" {
  description = "Desired number of worker nodes"
  type        = number
}

variable "eks_min_size" {
  description = "Minimum number of worker nodes"
  type        = number
}

variable "eks_max_size" {
  description = "Maximum number of worker nodes"
  type        = number
}

variable "ami" {
  description = "AMI ID for Jenkins EC2"
  type        = string
}

variable "jenkins_instance_type" {
  description = "EC2 instance type for Jenkins"
  type        = string
}

variable "key_name" {
  description = "EC2 key pair name for SSH"
  type        = string
}

variable "allowed_cidr" {
  description = "Your IP to allow SSH and Jenkins UI access"
  type        = string
}