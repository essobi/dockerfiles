FROM hashicorp/consul-template:alpine  
  
MAINTAINER itwye <itwye@qq.com>  
  
RUN apk update && apk add python  
  
ADD consul-template /consul-template  
  
ADD nginx /nginx  
  
RUN chown -R consul-template:consul-template /consul-template /nginx  
  
WORKDIR /nginx  

