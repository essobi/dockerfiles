  
FROM alpine:latest  
  
MAINTAINER Bodo Schulz <bodo@boone-schulz.de>  
  
LABEL version="1703-01"  
  
ENV TERM=xterm  
  
#
---------------------------------------------------------------------------------------  
  
RUN \  
apk --quiet --no-cache update && \  
apk --quiet --no-cache upgrade && \  
apk --quiet --no-cache add \  
build-base \  
bind-tools \  
drill \  
ruby-dev \  
ruby-io-console \  
ruby-rdoc && \  
gem install --no-rdoc --no-ri \  
json \  
rest-client \  
dalli \  
beaneater \  
rufus-scheduler && \  
apk del --purge \  
build-base \  
supervisor \  
bash \  
nano \  
curl \  
ca-certificates \  
ruby-dev \  
ruby-io-console \  
tree && \  
rm -rf /var/cache/apk/*  
  
CMD /bin/sh  
  
#
---------------------------------------------------------------------------------------  

