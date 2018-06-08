FROM ruby:2.3-alpine  
  
RUN apk add --no-cache build-base \  
&& apk add --no-cache --virtual .nokogiri-deps \  
libxml2 \  
libxslt \  
&& gem install nokogiri \  
&& apk del build-base  

