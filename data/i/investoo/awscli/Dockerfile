FROM mhart/alpine-node:6  
MAINTAINER <www.investoogroup.com>  
  
RUN apk update && apk add \  
bash \  
curl \  
zip \  
py-pip && \  
pip install --upgrade pip awscli s3cmd && \  
mkdir ~/.aws  

