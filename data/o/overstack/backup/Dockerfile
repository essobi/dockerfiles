FROM alpine:3.2  
MAINTAINER SHS <shs@overstack.ru>  
ENV BACKUP_VERSION 4.2  
RUN apk update && \  
apk upgrade && \  
apk add tar gzip ca-certificates build-base ruby-dev ruby-nokogiri mysql-
client && \  
echo 'gem: --no-rdoc --no-ri' >> "$HOME/.gemrc" && \  
gem install backup && \  
rm -rf /var/cache/apk/* /usr/local/src/* /tmp/* /usr/share/ri/*  

