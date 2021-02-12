# DynamoDB Local Utility

- Please ensure you're followed all the required steps in the [readme](README.md)
- To view the state of your local dynamodb database install `npm install -g dynamodb-admin`
- Set your local dynamodb endpoint as an environment variable `export DYNAMO_ENDPOINT=http://localhost:8000` (you might need to do this in git bash if you're on windows or look up the equivalent powershell/cmd command - I think it's something like `set ENV_VARIABLE_NAME "env variable value"`)
- Run dynamodb admin: `dynamodb-admin`
- Go to the link it outputs to see your database in web UI!