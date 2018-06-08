FROM debian:jessie  
MAINTAINER Robbert Klarenbeek <robbertkl@renbeek.nl>  
  
# Install own scripts and common packages  
COPY bin /usr/bin  
RUN cleanupgrade  
RUN cleaninstall \  
ca-certificates \  
curl \  
entr \  
gettext-base \  
git \  
less \  
lsb-release \  
nano  
  
# Environment variables  
ENV TERM=xterm  

