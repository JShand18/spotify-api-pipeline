resource "aws_lambda_function" "spotify_analysis" {
  filename      = "../payload.zip"
  function_name = "spotify_analysis"
  handler       = "spotify_analyzer.lambda_handler"
  role          = aws_iam_role.lambda_execution_role.arn
  runtime       = "python3.10"
  timeout       = "300"

  environment {
    variables = {
      SPOTIPY_CLIENT_ID     = var.TF_VAR_SPOTIPY_CLIENT_ID,
      SPOTIPY_CLIENT_SECRET = var.TF_VAR_SPOTIPY_CLIENT_SECRET
      SPOTIPY_REDIRECT_URI  = var.TF_VAR_SPOTIPY_REDIRECT_URI

      # AWS_ACCESS_KEY = var.TF_VAR_ACCESS_KEY
      # AWS_SECRET_KEY = var.TF_VAR_SECRET_KEY
    }
  }
}