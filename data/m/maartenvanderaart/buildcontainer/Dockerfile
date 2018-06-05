FROM maven:3.5.2-alpine  
LABEL maintainer "maarten@buttonbasher.org"  
LABEL version="1.4"  
COPY files/*.py /usr/local/bin/  
RUN apk add --no-cache python py-pip  
RUN pip install boto3 awscli  

