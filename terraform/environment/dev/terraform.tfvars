project_name = "finops"
environment  = "dev"
region       = "eu-central-1"

vpc_cidr = "10.0.0.0/16"

public_subnet_cidrs = {
  "eu-central-1a" = "10.0.101.0/24"
  "eu-central-1b" = "10.0.102.0/24"
}

private_subnet_cidrs = {
  "eu-central-1a" = "10.0.1.0/24"
  "eu-central-1b" = "10.0.2.0/24"
}

eks_instance_type = "c7i-flex.large"
eks_desired_size  = 2
eks_min_size      = 1
eks_max_size      = 3

ami                  = "ami-05852c5f195d545ea"
jenkins_instance_type = "c7i-flex.large"
key_name             = "myDevKey"
allowed_cidr         = "188.123.129.60/32"