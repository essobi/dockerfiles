FROM node:latest  
  
# Packages  
RUN apt-get update  
RUN apt-get install -y build-essential groff libssl-dev libffi-dev openssl zip
unzip python-dev python-pip vim less curl default-jre  
  
# AWS  
RUN pip install --upgrade cffi==1.2.1 awscli  
  
# Serverless  
ENV SERVERLESS serverless@1.27.2  
RUN yarn global add $SERVERLESS  
  
WORKDIR /opt/app  

