# Minimal Ruby runtime environment  
#  
# We need to base this on Alpine Linux 3.1 docker image because we need to  
# base our Ruby distributions on Ruby version 2.1 rather than the latest  
# 2.2 version which has some incompatibilities with e.g. Volt.  
#  
FROM alpine:3.1  
MAINTAINER Anders Hansson <anders@programlabbet.se>  
  
# Install some handy utilities  
RUN apk add --update curl wget bash rsync  
  
# Install ruby and some build dependencies  
RUN apk add --update build-base ruby ruby-dev ruby-bundler  
  
# Add some additional XXX-dev packages  
RUN apk add --update libffi-dev zlib-dev libxml2-dev libxslt-dev  
  
# Use a native installation of nokigiri  
RUN gem install nokogiri -- --use-system-libraries  
RUN gem install nokogiri -v '1.6.6.4' \-- --use-system-libraries  
  
# Add gems to /usr/bin path and make them readily available  
# (for some reason the ruby-bundler don't get added automatically)  
RUN ln -sf /usr/lib/ruby/gems/2.1.0/bin/* /usr/bin/.  
  
# Clean APK cache  
RUN rm -rf /var/cache/apk/*  

