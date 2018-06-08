# Use Base image python 3.6 version with alpine linux version 3.7  
FROM python:3.6-alpine3.7  
LABEL maintainer="Shivakumar Swamy B G <shivsks.1994@gmail.com>"  
  
# default ARG values  
ARG OPCUA_VERSION="0.95.1"  
# --no-cache: do not cache the package index  
# --virtual: cleanup packages  
RUN \  
# 'opcua' install dependencies  
apk add \--no-cache --virtual install_dependencies \  
g++ \  
libxml2-dev \  
libxslt-dev \  
# 'opcua' runtime dependencies  
&& apk add \--no-cache \  
libxml2 \  
libxslt \  
\  
# install 'opcua'  
&& pip3 install opcua==$OPCUA_VERSION \  
# cleanup 'install_dependencies'  
&& apk del install_dependencies

