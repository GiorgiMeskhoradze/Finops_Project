terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "6.17.0"
    }
  }
}
resource "aws_ecr_repository" "account-service" {
  name = "${var.project_name}/account-service"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }

  tags = {
    Name        = "${var.project_name}-account-service"
    Environment = var.environment
  }
}

resource "aws_ecr_repository" "transaction_service" {
  name                 = "${var.project_name}/transaction-service"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }

  tags = {
    Name        = "${var.project_name}-transaction-service"
    Environment = var.environment
  }
}

resource "aws_ecr_lifecycle_policy" "account_service_policy" {
  repository = aws_ecr_repository.account-service.name
  policy     = jsonencode({
    rules = [{
      rulePriority = 1
      description = "Keep only last 5 images"
      selection = {
        tagStatus = "any"
        countType = "imageCountMoreThan"
        countNumber = 5
      }
      action = {
        type = "expire"
      }
    }]
  })
}

resource "aws_ecr_lifecycle_policy" "transaction_service_policy" {
  repository = aws_ecr_repository.transaction_service.name
  policy     = jsonencode({
    rules = [{
      rulePriority = 1
      description = "Keep only last 5 images"
      selection = {
        tagStatus = "any"
        countType = "imageCountMoreThan"
        countNumber = 5
      }
      action = {
        type = "expire"
      }
    }]
  })
}