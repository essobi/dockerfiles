#  
# Base docker image to support other nzb-suite containers related  
#  
# Based on alpine  
#  
FROM alpine:latest  
MAINTAINER Bas van Reeuwijk <bas@reeuwijk.net>  
  
LABEL Description="Base image for other nzb-suite containers" Version="1.0"  
  
# User sabnzbd is common user for all child containers  
# UID corresponds to UID of host OS  
ENV SABNZBD_UID 1034  
ENV PYTHONIOENCODING="UTF-8"  
# Create SABNzb user and add to group users  
RUN adduser -s /bin/bash -u $SABNZBD_UID -D sabnzbd  
  
# Install base python environment  
RUN apk add --update --no-cache ca-certificates \  
openssl openssl-dev unzip unrar p7zip bash wget git \  
build-base dbus dbus-dev python2-dev dbus-glib dbus-glib-dev \  
py2-pip python2-dev automake autoconf \  
&& pip install --upgrade pip \  
&& pip install pyopenssl six cryptography enum34 cffi  
  
# Put all programs under /opt and configuration under /config  
RUN mkdir /opt && chmod 777 /opt  
  

