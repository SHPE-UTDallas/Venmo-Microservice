# Venmo-Microservice

A Microservice to help automate the processing of our member's dues. 

Planned Tech Stack:
- Serverless (AWS Lambda, API Gateway)
- DynamoDB
- Flask
- Venmo-API

Prerequisites:
- Install Node.js
  - Verify you have node.js (v12 or higher) installed `node -v`
- Install serverless
  - `npm install -g serverless`
  - Check it is installed with `serverless -v`
- Clone the project
  - Install our plugins/dependencies for serverless (IaC utility):
    - `npm install`
    - If you want to be able to develop locally instead of deploying to aws to test code install dynamodb: `sls dynamodb install`
  - Install our python dependencies:
    - `pip3 install -r requirements.txt`
- Create a file called `.env` in the root directory
  - Run the `get_access_token.py` file (`python3 get_access_token.py`)
  - Add the line it outputs that says `VENMO_ACCESS_TOKEN=123123...` to your .env file
- To run the project locally:
  - Make sure you're installed dynamodb locally (`sls dynamodb install`)
  - Start dynamodb in one terminal window/tab: `sls dynamodb start`
  - Run `sls wsgi serve` in a seperate terminal window/tab
  - Checkout this guide [here](dynamodb.md) for more info on dynamodb local and a useful GUI tool to view your local database
- To deploy the project:
  - Setup your aws credentials - guide [here](https://slss.io/aws-creds-setup)
  - Run `sls deploy`
<br/>
<br/>

### Note: in order to deploy to aws/run this locally you may need to install [Docker](https://www.docker.com/) as well (I'm pretty sure we use it for deploying but not 100% sure - I already had it installed prior to setting this up)
