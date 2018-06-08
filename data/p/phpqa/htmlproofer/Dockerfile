FROM ruby:alpine  
MAINTAINER Bart Reunes <metalarend@gmail.com>  
  
# Install Tini - https://github.com/krallin/tini  
RUN apk add --no-cache tini  
  
# Install HTMLProofer - https://github.com/gjtorikian/html-proofer  
RUN apk add --no-cache --virtual build-dependencies build-base libxml2-dev
libxslt-dev \  
&& apk add --no-cache libcurl \  
&& gem install html-proofer --no-document \  
&& apk del build-dependencies  
  
# Package container  
VOLUME ["/app"]  
WORKDIR "/app"  
ENTRYPOINT ["/sbin/tini", "--", "htmlproofer"]  
CMD ["--help"]  

