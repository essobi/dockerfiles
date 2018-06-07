FROM ruby:2.3.4-alpine3.4  
RUN apk add --no-cache \  
build-base \  
ruby-dev  
  
RUN gem install --no-ri --no-rdoc \  
daemons \  
eventmachine \  
faye \  
rack \  
thin  
  
RUN apk del build-base  
RUN rm -rf /tmp/* /var/lib/cache/apk/*  

