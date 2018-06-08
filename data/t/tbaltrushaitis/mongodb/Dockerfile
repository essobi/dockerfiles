##
================================================================================
##  
## Dockerized MongoDB: Dockerfile for building MongoDB Server image ##  
##
================================================================================
##  
## Based on ubuntu:16.04, installs MongoDB following the instructions from: ##  
## http://docs.mongodb.org/manual/tutorial/install-mongodb-on-ubuntu/ ##  
##
================================================================================
##  
  
## Source Image  
##
--------------------------------------------------------------------------------
##  
FROM ubuntu:16.04  
  
## Build-time metadata as defined at http://label-schema.org  
##
--------------------------------------------------------------------------------
##  
ARG BUILD_DATE  
ARG VCS_URL  
ARG VCS_REF  
ARG VERSION  
  
## Image Labels Metadata  
##
--------------------------------------------------------------------------------
##  
LABEL com.kevix.mongodb.maintainer.name="Kevix" \  
com.kevix.mongodb.maintainer.mail="kevix.ultra@gmail.com" \  
com.kevix.mongodb.description="Dockerized MongoDB Server" \  
com.kevix.mongodb.build-date=${BUILD_DATE} \  
com.kevix.mongodb.vcs-url=${VCS_URL} \  
com.kevix.mongodb.vcs-ref=${VCS_REF} \  
com.kevix.mongodb.dockerfile.version=${VERSION} \  
com.kevix.mongodb.is-production="true"  
  
## Environment Variables  
##
--------------------------------------------------------------------------------
##  
ENV SVC_MAJOR=${SVC_MAJOR:-3.4} \  
SVC_VERSION=${SVC_VERSION:-3.4.1} \  
SVC_PACKAGE=${SVC_PACKAGE:-mongodb-org} \  
SVC_DATA_DIR=${SVC_DATA_DIR:-/data/db} \  
SVC_USER=${SVC_USER:-mongod}  
  
## Copy/Create Files and Directories  
##
--------------------------------------------------------------------------------
##  
ADD docker-entrypoint.sh /entrypoint.sh  
  
RUN \  
mkdir -p ${SVC_DATA_DIR} \  
\  
## Create the MongoDB system user \  
##
--------------------------------------------------------------------------------
## \  
&& groupadd --system \  
\--force \  
${SVC_USER} \  
&& useradd --system \  
\--no-create-home \  
\--base-dir $(dirname ${SVC_DATA_DIR}) \  
\--gid ${SVC_USER} \  
\--shell /bin/bash \  
${SVC_USER} \  
\  
## Import MongoDB public GPG key used by the package management system \  
##
--------------------------------------------------------------------------------
## \  
&& set -ex \  
&& for key in \  
0C49F3730359A14518585931BC711F9BA15703C6 \  
7F0CEB10 \  
; do \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \  
\--recv "$key"; \  
done \  
\  
## Create a list of source files for MongoDB \  
##
--------------------------------------------------------------------------------
## \  
&& echo "deb [arch=amd64] http://repo.mongodb.org/apt/ubuntu $(cat /etc/lsb-
release | grep DISTRIB_CODENAME | cut -d= -f2)/${SVC_PACKAGE}/${SVC_MAJOR}
multiverse" \  
| tee /etc/apt/sources.list.d/${SVC_PACKAGE}-${SVC_MAJOR}-multiverse.list \  
&& echo "deb [arch=amd64] http://repo.mongodb.org/apt/ubuntu $(cat /etc/lsb-
release | grep DISTRIB_CODENAME | cut -d= -f2)/${SVC_PACKAGE}/${SVC_MAJOR}
Release" \  
| tee /etc/apt/sources.list.d/${SVC_PACKAGE}-${SVC_MAJOR}-10gen.list \  
\  
## Update sources and install MongoDB packages \  
##
--------------------------------------------------------------------------------
## \  
&& apt-get -q update \  
&& apt-get -yq install \  
\--no-install-recommends \  
${SVC_PACKAGE}=${SVC_VERSION} \  
${SVC_PACKAGE}-server=${SVC_VERSION} \  
${SVC_PACKAGE}-shell=${SVC_VERSION} \  
${SVC_PACKAGE}-mongos=${SVC_VERSION} \  
${SVC_PACKAGE}-tools=${SVC_VERSION} \  
curl \  
git \  
mc \  
telnet \  
wget \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& printf "\n\n DEPLOYED: ${SVC_PACKAGE}:${SVC_VERSION} \n\n"; # /**/ \  
\  
&& chown ${SVC_USER}:${SVC_USER} /entrypoint.sh ${SVC_DATA_DIR} \  
&& chmod a+x /entrypoint.sh \  
&& chmod 775 ${SVC_DATA_DIR}  
  
#VOLUME ${SVC_DATA_DIR}:${}  
#USER ${SVC_USER}  
  
## Expose port 27017 from the container to the host  
##
--------------------------------------------------------------------------------
##  
EXPOSE 28017:27017  
  
## Setup Service Entrypoint  
##
--------------------------------------------------------------------------------
##  
## ENTRYPOINT ["/usr/bin/mongod"];  
ENTRYPOINT ["/entrypoint.sh"];  
  
CMD ["mongod", "--dbpath", "/data/db"];  

