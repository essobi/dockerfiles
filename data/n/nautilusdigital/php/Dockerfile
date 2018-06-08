FROM php:7.1.8-alpine  
  
# Install AWS CLI  
RUN apk --no-cache update && \  
apk --no-cache add python py-pip py-setuptools ca-certificates groff less && \  
pip --no-cache-dir install awscli && \  
rm -rf /var/cache/apk/*  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer  
  
# Install development packages  
RUN apk add --no-cache --update bash curl git openssh jq && \  
rm -rf /var/cache/apk/*  

