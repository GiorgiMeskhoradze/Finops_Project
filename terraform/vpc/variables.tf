variable "vpc_cidr" {
  description = "CIDR block for VPC"
  type        = string
}

variable "private_subnets" {
  description = "Map of AZ to CIDR for private subnets"
  type        = map(string)
}

variable "public_subnets" {
  description = "Map of AZ to CIDR for public subnets"
  type        = map(string)
}

variable "environment" {
  description = "Environment name"
  type        = string
}

variable "project_name" {
  description = "Project name"
  type        = string
}