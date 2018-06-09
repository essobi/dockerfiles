# Ref: https://github.com/gliderlabs/docker-alpine/issues/53  
FROM ruby:2.3.1-alpine  
  
RUN apk add --update \  
build-base \  
libxml2-dev \  
libxslt-dev \  
postgresql-dev \  
&& rm -rf /var/cache/apk/*  
  
# Use libxml2, libxslt a packages from alpine for building nokogiri  
RUN bundle config build.nokogiri --use-system-libraries  

