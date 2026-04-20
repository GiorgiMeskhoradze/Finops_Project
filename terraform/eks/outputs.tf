output "cluster_endpoint" {
  value = aws_eks_cluster.eks_main_cluster.endpoint
}

output "cluster_name" {
  value = aws_eks_cluster.eks_main_cluster.name
}

output "cluster_certificate_authority" {
  value = aws_eks_cluster.eks_main_cluster.certificate_authority[0].data
}

output "node_group_role_arn" {
  value = aws_iam_role.eks_node_role.arn
}