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
  - Install our plugins/dependencies:
    - `npm install`
- To run the project locally:
  - Run `sls wsgi serve`
- To deploy the project:
  - Setup your aws credentials - guide [here](slss.io/aws-creds-setup)
  - Run `sls deploy`