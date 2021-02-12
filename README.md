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
  - Install our python dependencies:
    - `pip3 install -r requirements.txt`
- Create a file called `.env` in the root directory
  - Run the `get_access_token.py` file (`python3 get_access_token.py`)
  - Add the line it outputs that says `VENMO_ACCESS_TOKEN=123123...` to your .env file
- To run the project locally:
  - Run `sls wsgi serve`
- To deploy the project:
  - Setup your aws credentials - guide [here](https://slss.io/aws-creds-setup)
  - Run `sls deploy`