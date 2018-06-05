# Copyright (C) 2015 Bitergia  
# GPLv3 License  
FROM node:0.10-slim  
MAINTAINER Bitergia <fiware-testing@bitergia.com>  
  
ENV WILMA_HOME /opt/fi-ware-pep-proxy  
ENV WILMA_USER pepproxy  
ENV GIT_REV_WILMA 4.3  
ENV GIT_URL_WILMA https://github.com/ging/fi-ware-pep-proxy.git  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN adduser --disabled-password --gecos "${WILMA_USER}" ${WILMA_USER}  
  
# install APT dependencies  
RUN apt-get update && \  
apt-get -y install --no-install-recommends \  
netcat curl \  
git ca-certificates \  
python \  
make gcc build-essential \  
&& \  
# download and install PEP Wilma (service starts Automatically)  
git clone ${GIT_URL_WILMA} ${WILMA_HOME} && \  
cd ${WILMA_HOME} && \  
git checkout ${GIT_REV_WILMA} && \  
npm install && \  
# Install forever to make PEP run at Startup  
npm install forever --global && \  
# remove unneeded packages  
apt-get -y purge build-essential gcc make && \  
apt-get -y autoremove --purge && \  
apt-get clean && \  
find /var/lib/apt/lists -type f -delete && \  
rm -rf /root/.npm /root/.node-gyp  
  
WORKDIR ${WILMA_HOME}  
  
# Configure PEP proxy  
COPY config.js ${WILMA_HOME}/config.js  
COPY azf.patch ${WILMA_HOME}/lib/azf.patch  
RUN git apply -v ${WILMA_HOME}/lib/azf.patch  
  
# Add script to retrieve token automatically  
COPY auth-token.sh /usr/local/bin/auth-token.sh  
RUN chmod 755 /usr/local/bin/auth-token.sh  
  
# Retrieve domain  
COPY docker-entrypoint.sh /  
ADD https://raw.githubusercontent.com/Bitergia/docker/master/utils/entrypoint-
common.sh /  
RUN chmod 755 /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
### Exposed ports  
# - Wilma PEP  
EXPOSE 1026  

