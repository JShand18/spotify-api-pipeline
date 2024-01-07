provider "aws" {
  region     = var.aws_region
  access_key = var.TF_VAR_ACCESS_KEY
  secret_key = var.TF_VAR_SECRET_KEY
}