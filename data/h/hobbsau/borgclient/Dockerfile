#Borgbackup Dockerfile  
FROM alpine:edge  
MAINTAINER Adrian Hobbs <adrianhobbs@gmail.com>  
ENV PACKAGE "borgbackup openssh-client"  
# Install package using --no-cache to update index and remove unwanted files  
RUN apk add --no-cache --upgrade apk-tools && \  
apk upgrade && \  
apk add $PACKAGE && \  
# Fix for borgbackup 1.1.5
http://borgbackup.readthedocs.io/en/stable/changes.html#version-1-1-5-2018-04-01  
python3 -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
pip3 install --upgrade pip setuptools && \  
if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \  
if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python;
fi && \  
rm -r /root/.cache && \  
pip3 install msgpack-python==0.4.8 && \  
rm -rf /var/cache/apk/* && \  
mkdir /cache  
  
ENV BORG_CACHE_DIR /cache  
WORKDIR /tmp  
  
ENTRYPOINT ["/usr/bin/borg"]  
  

