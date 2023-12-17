variable "db_password" {
  description = "Password for Redshift master DB user"
  type        = string
  default     = "js18"
}

variable "s3_bucket" {
  description = "Bucket name for S3"
  type        = string
  default     = "spotify_analysis_bucket"
}

variable "TF_VAR_SPOTIPY_CLIENT_ID" {
  type = "string"
}

variable "TF_VAR_SPOTIPY_CLIENT_SECRET" {
  type = "string"
}

variable "TF_VAR_SPOTIPY_REDIRECT_URI" {
  type = "string"
}

variable "TF_VAR_ACCESS_KEY" {
  type = "string"
}

variable "TF_VAR_SECRET_KEY" {
  type = "string"
}

variable "aws_region" {
  description = "Region for AWS"
  type        = string
  default     = "us-east-2"
}