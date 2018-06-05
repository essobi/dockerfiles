FROM ruby:2.3-alpine  
  
# https://github.com/gliderlabs/docker-alpine/issues/53#issuecomment-125671731  
RUN apk --update add --virtual build-dependencies build-base libxml2-dev
libxslt-dev  
RUN apk add --update libcurl \  
&& gem install nokogiri html-proofer --no-ri --no-rdoc \  
&& apk del build-dependencies  
  
CMD ["htmlproofer","--help"]  

