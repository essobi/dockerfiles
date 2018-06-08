FROM alpine:3.5  
RUN apk add --update \  
bash \  
gnupg \  
jq \  
py-pip \  
&& rm -rf /var/cache/apk/*  
  
RUN pip install awscli  

