resource "aws_lambda_function" "spotify_analysis" {
  filename =  "../payload.zip"
  function_name = "spotify_analysis"
  handler = "spotify_analzyer.lambda_handler"
  role = "${aws_iam_role.lambda_execution_role.arn}"
  runtime = "python3.9"
  timeout = "300"

  environment {
    variables = {
      SPOTIPY_CLIENT_ID = var.TF_VAR_SPOTIPY_CLIENT_ID,
      SPOTIPY_CLIENT_SECRET = var.TF_VAR_SPOTIPY_CLIENT_SECRET
      SPOTIPY_REDIRECT_URI = var.TF_VAR_SPOTIPY_REDIRECT_URI 
    }
  }
}