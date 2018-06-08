FROM alpine:3.4  
MAINTAINER Christian Inzinger <christian@inz.io>  
  
RUN echo 'gem: --no-rdoc --no-ri' >/etc/gemrc  
RUN apk --update add \  
ca-certificates \  
ruby \  
ruby-bundler \  
# Clean APK cache  
&& rm -rf /var/cache/apk/*  

