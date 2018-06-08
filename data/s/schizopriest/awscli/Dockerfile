FROM alpine  
MAINTAINER Pascal Reeb <pascal at reeb dot io>  
  
RUN apk add --update \  
python \  
py-pip \  
ca-certificates  
RUN pip install awscli  
RUN rm -rf /var/cache/apk/*  

