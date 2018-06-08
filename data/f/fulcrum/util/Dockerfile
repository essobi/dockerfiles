FROM mhart/alpine-node:6  
MAINTAINER IF Fulcrum "fulcrum@ifsight.net"  
RUN apk update && apk upgrade && \  
apk --no-cache add bash coreutils curl gettext jq && \  
mkdir /etc/periodic/01min /etc/periodic/05min /etc/periodic/10min  
  
ADD fulcrum /fulcrum  
ADD etc/crontabs/root /etc/crontabs/root  

