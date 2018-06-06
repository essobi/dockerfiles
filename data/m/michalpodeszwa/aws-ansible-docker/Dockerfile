FROM python:2-alpine  
  
RUN apk update  
  
RUN apk add gcc musl-dev libffi-dev openssl-dev docker bash rsync openssh
apache2-utils  
  
RUN pip install boto boto3 botocore awscli markupsafe ansible docker-py
docker-compose  
  
RUN ln -s /usr/local/bin/python /usr/bin/python  
  
VOLUME ~/.aws  
VOLUME /project  
  
WORKDIR /project  

