locals {
  envs = { for tuple in regexall("(.*)=(.*)", file("../.env")) : tuple[0] => sensitive(tuple[1]) }
}

variable "db_password" {
  description = "Password for Redshift master DB user"
  type        = string
  default     = "Jshandy18"
}

variable "s3_bucket" {
  description = "Bucket name for S3"
  type        = string
  default     = "spotify-analysis-bucket"
}

variable "TF_VAR_SPOTIPY_CLIENT_ID" {
  type = string
}

variable "TF_VAR_SPOTIPY_CLIENT_SECRET" {
  type = string
}

variable "TF_VAR_SPOTIPY_REDIRECT_URI" {
  type    = string
  default = "http://localhost:3000"
}

variable "TF_VAR_ACCESS_KEY" {
  type = string
}

variable "TF_VAR_SECRET_KEY" {
  type = string
}

variable "aws_region" {
  description = "Region for AWS"
  type        = string
  default     = "us-east-2"
}
