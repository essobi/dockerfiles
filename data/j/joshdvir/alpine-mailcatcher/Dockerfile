FROM alpine:3.2  
MAINTAINER Shuky Dvir <shuky@devops.co.il>  
  
RUN apk add --update \  
ruby \  
ruby-dev \  
ruby-io-console \  
ruby-json \  
ruby-bigdecimal \  
bash \  
sqlite \  
sqlite-dev \  
openssl-dev \  
build-base \  
&& gem install mailcatcher json --no-rdoc --no-ri \  
&& apk del --update build-base openssl-dev ruby-dev \  
&& apk add --update libstdc++ \  
&& rm -rf /var/cache/apk/*  
  
# smtp port  
EXPOSE 1025  
# webserver port  
EXPOSE 1080  
  
CMD ["mailcatcher", "-f", "--ip=0.0.0.0"]

