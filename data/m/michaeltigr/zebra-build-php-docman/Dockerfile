FROM michaeltigr/zebra-php-base:latest  
  
LABEL maintainer "Michael Molchanov <mmolchanov@adyax.com>"  
  
USER root  
  
# Install docman.  
RUN apk add --update --no-cache ruby ruby-dev \  
&& rm -rf /var/cache/apk/* \  
&& gem install --no-ri --no-rdoc -v 0.0.97 docman  

