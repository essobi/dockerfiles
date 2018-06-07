FROM alpine:latest  
  
MAINTAINER Hamdi Laadhari <killerwolf06@gmail.com>  
  
RUN apk add --update php-cli php-gd php-json php-phar php-curl php-zip php-
openssl && \  
rm -rf /var/cache/apk/*  
  
COPY . /usr/src/nds  
WORKDIR /usr/src/nds  
RUN php composer.phar install --prefer-dist  
ADD run.sh /usr/local/bin/run.sh  
RUN chmod +x /usr/local/bin/run.sh  
CMD ["/usr/local/bin/run.sh"]

