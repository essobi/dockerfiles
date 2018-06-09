FROM alpine:latest  
MAINTAINER yamazawa@supersoftware.co.jp  
  
ENV BUILD_PACKAGES build-base git autoconf automake  
  
RUN apk update && \  
apk upgrade && \  
apk add git openssh-client && \  
rm -rf /var/cache/apk/*  
  
COPY ./docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

