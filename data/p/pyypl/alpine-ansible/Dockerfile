FROM alpine:latest  
  
# install ansible  
RUN apk add --update \  
ansible \  
py-pip \  
&& pip install boto3 \  
&& rm -rf /var/cache/apk/*  

