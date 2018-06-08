FROM gliderlabs/alpine:3.2  
MAINTAINER Adam Greene <adam.greene@gmail.com>  
  
RUN apk add --update \  
py-pip \  
groff \  
less \  
&& pip install awscli==1.10.21 \  
&& rm -rf /var/cache/apk/*  
  
WORKDIR /aws  
  
ENTRYPOINT ["aws"]  

