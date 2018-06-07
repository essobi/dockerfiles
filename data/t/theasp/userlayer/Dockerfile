FROM ubuntu:18.04  
ARG http_proxy  
MAINTAINER Andrew Phillips <theasp@gmail.com>  
RUN set -ex; \  
apt-get update -q; \  
apt-get install -q -y supervisor sudo openssh-client gettext-base  
ENV USER_NAME="user" \  
USER_UID="1000" \  
USER_GID="1000" \  
USER_HOME="/home/user" \  
USER_SHELL="/bin/bash" \  
USER_GECOS="Unknown User" \  
ENABLE_SUPERVISOR="true" \  
ENABLE_SUDO="true" \  
DEBUG=false  
ENTRYPOINT ["/app/entrypoint.sh"]  
COPY app/ userlayer.sh /app/  

