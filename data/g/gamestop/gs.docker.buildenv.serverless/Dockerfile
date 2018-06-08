FROM gamestop/gs.docker.buildenv.nodejs:7.0.0  
LABEL "MAINTAINER" "eapplicationarchitects@gamestop.com"  
  
RUN apt-get update && apt-get install -y jq  
  
RUN pip install 'boto3==1.5.21'  
  
RUN npm install -g serverless@1.25.0  

