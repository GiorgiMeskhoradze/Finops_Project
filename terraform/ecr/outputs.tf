output "account_service_url" {
  value = aws_ecr_repository.account-service.repository_url
}

output "transaction_service_url" {
  value = aws_ecr_repository.transaction_service.repository_url
}