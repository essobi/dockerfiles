FROM alpine:latest  
MAINTAINER Yury Galustov <tnt9062@gmail.com>  
  
  
RUN apk --update add bash zip readline readline-dev libxml2 libxml2-dev
libxslt \  
libxslt-dev zlib zlib-dev ruby ruby-dev yaml yaml-dev libffi libffi-dev build-
base \  
ruby-irb ruby-json ruby-rake ruby-rdoc git ruby-io-console curl openssl  
  
RUN apk update && apk upgrade && rm -rf /var/cache/apk/*  
RUN mkdir /_site  
RUN mkdir /_scripts  
COPY aws_push.sh /_scripts  
  
RUN gem install bundler jekyll --no-document  

