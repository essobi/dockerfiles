FROM alpine:3.3  
MAINTAINER Jeremy Wells <jemmyw@gmail.com>  
  
RUN apk update && apk upgrade  
  
RUN apk add python py-pip groff less \  
&& pip install --upgrade awscli \  
&& apk del py-pip \  
&& mkdir /app  
  
WORKDIR /app  
  
ENTRYPOINT ["/usr/bin/aws"]  

