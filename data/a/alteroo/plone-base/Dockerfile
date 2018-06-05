FROM ubuntu:12.04  
MAINTAINER David Bain <david@alteroo.com>  
  
# this file is inspired by https://github.com/ju55i/docker-
plone/blob/master/base/Dockerfile  
# it creates a base plone instance  
# it is meant to be overridden with a downstream docker file  
# customize to your needs by changing these variables  
ENV PASSWORD secret  
ENV MAJORVERSION 4.3  
ENV MINORVERSION 4.3.3  
ENV TARGETDIR /opt/plone  
ENV INSTANCENAME app  
ENV INSTANCEDIR $TARGETDIR/$INSTANCENAME  
  
# it is unlikely that you'll need to change these  
ENV BASEURL https://launchpad.net/plone  
ENV URLPATH $BASEURL/${MAJORVERSION}/${MINORVERSION}/+download/Plone-  
  
# prepare OS  
RUN apt-get update  
RUN apt-get install -y zip supervisor build-essential wget libssl-dev
libxml2-dev libxslt1-dev libbz2-dev zlib1g-dev python-setuptools python-dev
libjpeg62-dev libreadline-dev python-imaging wv poppler-utils  
  
RUN mkdir -p $TARGETDIR  
WORKDIR $INSTALLDIR  
  
# set plone user uid to 88  
RUN useradd plone -d $TARGETDIR -s /bin/bash -u 88  
RUN chown -R plone:plone $TARGETDIR  
  
# fetch and unpack unified installer  
USER plone  
WORKDIR /tmp  
RUN wget --no-check-certificate ${URLPATH}${MINORVERSION}-UnifiedInstaller.tgz  
RUN tar -xzf Plone-${MINORVERSION}-UnifiedInstaller.tgz  
  
# install as standalone  
WORKDIR Plone-${MINORVERSION}-UnifiedInstaller  
RUN ./install.sh --password=$PASSWORD standalone --target=$TARGETDIR
\--instance=$INSTANCENAME  
  
# Meant to be the base image for a Plone deployment, create containers from
this  

