terraform {
  backend "s3" {
    bucket         = "my-terraform-backend-for-learning"
    key            = "dev/terraform.tfstate"
    region         = "eu-central-1"
    dynamodb_table = "terraform-lock"
    encrypt        = true
  }
}