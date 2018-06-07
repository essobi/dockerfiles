# Etherpad-Lite Dockerfile  
#  
# https://github.com/ether/etherpad-docker  
#  
# Developed from a version by Evan Hazlett at https://github.com/arcus-
io/docker-etherpad  
#  
# Version 1.6.0  
# Use Docker's nodejs, which is based on ubuntu  
FROM node:4.4  
MAINTAINER Thiago Almeida <thiagoalmeidasa@gmail.com>  
  
ENV ETHERPAD_VERSION 1.6.0  
ENV PLUGINS ep_adminpads ep_markdown ep_webrtc
git+https://github.com/tykeal/ep_ldapauth.git  
  
  
# Get Etherpad-lite's other dependencies  
RUN set -x; \  
apt-get update \  
&& apt-get install -y --no-install-recommends \  
gzip git-core curl python libssl-dev pkg-config build-essential supervisor \  
&& rm -rf /var/lib/apt/lists/*  
  
# Setting up the workdir  
WORKDIR /opt/etherpad/  
  
# Grab the especific Git version  
RUN cd /opt && git clone https://github.com/ether/etherpad-lite.git \  
\--branch ${ETHERPAD_VERSION} etherpad  
  
# Install node dependencies  
RUN /opt/etherpad/bin/installDeps.sh  
  
# Install plugins  
RUN npm --silent install \  
$PLUGINS  
  
# Add conf files  
ADD supervisor.conf /etc/supervisor/supervisor.conf  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod 0755 /entrypoint.sh  
  
VOLUME ["/data"]  
  
EXPOSE 9001  
ENTRYPOINT ["/entrypoint.sh"]  

