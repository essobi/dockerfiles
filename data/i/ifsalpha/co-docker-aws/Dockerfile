FROM node:latest  
  
RUN apt-get update && apt-get install -qq -y python-pip libpython-dev jq \  
&& curl -O https://bootstrap.pypa.io/get-pip.py && python get-pip.py \  
&& pip install -q awscli \--upgrade \  
&& aws configure set region eu-central-1  

