FROM alpine:3.6  
MAINTAINER Technosoft2000 <technosoft2000@gmx.net>  
LABEL image.base.version="3.6-3" \  
image.base.description="Docker image for Alpine based docker images by
Technosoft2000" \  
image.base.date="2017-10-30" \  
url.base.docker="https://hub.docker.com/r/technosoft2000/alpine-base" \  
url.base.github="https://github.com/Technosoft2000/docker-alpine-base" \  
url.base.support="https://cytec.us/forum"  
  
# Set basic environment settings  
ENV \  
# - VERSION: the docker image version (corresponds to the above LABEL
image.version)  
VERSION="1.0.0" \  
  
# - TERM: the name of a terminal information file from /lib/terminfo,  
# this file instructs terminal programs how to achieve things such as
displaying color.  
TERM="xterm" \  
  
# - LANG, LANGUAGE, LC_ALL: language dependent settings (Default: de_DE.UTF-8)  
LANG="de_DE.UTF-8" \  
LANGUAGE="de_DE:de" \  
LC_ALL="de_DE.UTF-8" \  
  
# - SET_CONTAINER_TIMEZONE: set this environment variable to true to set
timezone on container startup  
SET_CONTAINER_TIMEZONE="false" \  
  
# - CONTAINER_TIMEZONE: UTC, Default container timezone as found under the
directory /usr/share/zoneinfo/  
CONTAINER_TIMEZONE="UTC" \  
  
# - PKG_*: the needed applications for installation  
GOSU_VERSION="1.10" \  
PKG_BASE="bash tzdata git coreutils shadow tree"  
RUN \  
# update the package list  
apk -U upgrade && \  
  
# install gosu from https://github.com/tianon/gosu  
# https://github.com/tianon/gosu/blob/master/INSTALL.md  
set -ex; \  
\  
apk add \--no-cache --virtual .gosu-deps \  
dpkg \  
gnupg \  
openssl \  
; \  
\  
dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')"; \  
wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch";
\  
wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc";
\  
\  
# verify the signature  
export GNUPGHOME="$(mktemp -d)"; \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4; \  
gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu; \  
#HINT: deactivated at the moment because it results in 'No such file ...'
error  
#rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc; \  
\  
chmod +x /usr/local/bin/gosu; \  
# verify that the binary works  
gosu nobody true; \  
\  
apk del .gosu-deps; \  
  
# install the needed applications  
apk -U add \--no-cache $PKG_BASE && \  
  
# create init folder  
mkdir -p /init && \  
  
# cleanup temporary files  
rm -rf /tmp/* && \  
rm -rf /var/cache/apk/*  
  
# copy files to the image (info.txt and scripts)  
COPY *.txt /init/  
COPY *.sh /init/  
  
# start.sh will download the latest version of the APP and run it.  
RUN chmod u+x /init/start.sh  
  
# launch the start.sh  
CMD ["/bin/bash", "-c", "/init/start.sh"]  

