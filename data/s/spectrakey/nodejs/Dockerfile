#  
# SpectraKey NodeJS Docker File  
# Builds a docker image to install NodeJS  
#  
FROM node:0.12.7-slim  
  
RUN apt-get update -y && apt-get install --no-install-recommends -y -q curl
python build-essential git ca-certificates  
  
# Install global npm dependencies  
RUN npm install -g \  
forever@0.14.2 \  
grunt-cli  

