#FROM quay.io/sameersbn/ubuntu:14.04.20151023  
#FROM gliderlabs/alpine:3.2  
FROM alpine:3.2  
MAINTAINER Junior Xu "ayijun@gmail.com"  
# http://blog.kontena.io/building-minimal-docker-image-for-rails/  
RUN apk --update add ruby ruby-bundler ruby-irb ruby-json ruby-rake \  
ruby-bigdecimal ruby-io-console libstdc++ sqlite-libs openssl && \  
rm /var/cache/apk/*  
  
ENV MAILCATCHER_VERSION=0.6.2  
# https://github.com/gliderlabs/docker-
alpine/blob/master/docs/usage.md#virtual-packages  
RUN apk --update add --virtual build-dependencies build-base ruby-dev openssl-
dev sqlite-dev && \  
gem install --no-document mailcatcher -v ${MAILCATCHER_VERSION} && \  
apk del build-dependencies && \  
rm /var/cache/apk/*  
  
# smtp port / webserver port  
EXPOSE 1025 1080  
CMD ["mailcatcher", "-f", "--ip=0.0.0.0"]  

