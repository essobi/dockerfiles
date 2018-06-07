FROM alpine:latest  
MAINTAINER Roberto Aguilar <roberto.c.aguilar@gmail.com>  
  
RUN apk update && \  
apk add build-base ca-certificates curl libffi-dev openssl ruby ruby-dev rsync
tar  
  
RUN curl -O https://rubygems.org/downloads/rubygems-update-2.6.8.gem && \  
gem install --local rubygems-update-2.6.8.gem --no-rdoc --no-ri && \  
update_rubygems --no-document && \  
gem install fpm --no-rdoc --no-ri  
  
CMD ["/bin/sh"]  

