FROM python:3.6-alpine  
  
RUN apk add --update --no-cache \  
jq \  
curl \  
bash \  
git  
  
RUN curl https://raw.githubusercontent.com/apex/apex/master/install.sh | sh &&
apex upgrade  
RUN pip install awscli  
RUN pip install awscurl  

