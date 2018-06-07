FROM alpine:3.6  
MAINTAINER Sebastien LANGOUREAUX (linuxworkgroup@hotmail.com)  
  
COPY /scripts /scripts  
  
RUN \  
apk add --update python2 py-setuptools tar gzip sed curl bash openssl &&\  
mkdir /harbor &&\  
curl -sL https://github.com/vmware/harbor/releases/download/v1.2.0/harbor-
online-installer-v1.2.0.tgz \  
| tar -zx -C "/" &&\  
chmod -R +x /scripts &&\  
rm -rf /var/cache/apk/*  
  
WORKDIR /harbor  
  
VOLUME "/harbor/data"  
  
CMD "/scripts/harbor-setupwrapper.sh"

