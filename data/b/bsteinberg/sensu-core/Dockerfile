################################################################################  
# Dockerfile to build dockerized Sensu Core server image  
#  
# Based on: debian:jessie  
#  
# Created On: Nov 10, 2015  
# Author: Baruch Steinberg <baruch.steinberg@gmail.com>  
#  
# Description:  
#
------------------------------------------------------------------------------  
# Image include the following services/applications:  
# -  
################################################################################  
  
## Set the base image  
FROM debian:jessie  
  
## File maintainer  
MAINTAINER Baruch Steinberg <baruch.steinberg@gmail.com>  
  
###############################################################################  
#  
# INSTALLATION  
#  
################################################################################  
ENV DEBIAN_FRONTEND noninteractive  
  
WORKDIR /tmp  
  
ENV SENSU_MAJOR_VERSION 0.21  
ENV SENSU_MINOR_VERSION 0-2  
  
## Install dependencies: curl, ca-certificates  
##
-----------------------------------------------------------------------------  
RUN apt-get update \  
&& apt-get -y install curl ca-certificates --no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
## Install Sensu Core Repository  
##
-----------------------------------------------------------------------------  
RUN curl -sSLo /tmp/pubkey.gpg http://repositories.sensuapp.org/apt/pubkey.gpg
\  
&& apt-key add pubkey.gpg \  
&& echo "deb http://repositories.sensuapp.org/apt sensu main" >
/etc/apt/sources.list.d/sensu.list \  
&& apt-get update  
  
## Install Sensu Core  
##
-----------------------------------------------------------------------------  
RUN apt-get update \  
&& apt-get -y install sensu=${SENSU_MAJOR_VERSION}.${SENSU_MINOR_VERSION} \  
&& rm -rf /var/lib/apt/lists/*  
  
## Install Supervisord  
##
-----------------------------------------------------------------------------  
RUN apt-get update \  
&& apt-get install -y supervisor \  
&& rm -rf /var/lib/apt/lists/*  
  
################################################################################  
#  
# CONFIGURATION  
#  
################################################################################  
  
## Create Sensu Core configuration file  
##
-----------------------------------------------------------------------------  
#COPY config/sensu-config.json /etc/sensu/config.json  
COPY config/rabbitmq.json /etc/sensu/conf.d/rabbitmq.json  
COPY config/redis.json /etc/sensu/conf.d/redis.json  
COPY config/api.json /etc/sensu/conf.d/api.json  
RUN rm -f /etc/sensu/config.json.example  
  
## Generate required environment variables  
##
-----------------------------------------------------------------------------  
ENV RUNTIME_INSTALL ''  
ENV LOG_LEVEL warn  
ENV EMBEDDED_RUBY true  
ENV CONFIG_FILE /etc/sensu/config.json  
ENV CONFIG_DIR /etc/sensu/conf.d  
ENV CHECK_DIR /etc/sensu/check.d  
ENV EXTENSION_DIR /etc/sensu/extensions  
ENV PLUGINS_DIR /etc/sensu/plugins  
ENV HANDLERS_DIR /etc/sensu/handlers  
ENV LOG_DIR /var/log/sensu  
ENV LOG_LEVEL info  
ENV PID_DIR /var/run/sensu  
  
## Setup permissions  
##
-----------------------------------------------------------------------------  
RUN chown -R sensu:sensu /etc/sensu  
  
## Configure Supervisord  
##
-----------------------------------------------------------------------------  
RUN mkdir -p /etc/supervisor/conf.d/  
RUN mkdir -p /var/log/supervisor  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
################################################################################  
#  
# RUN  
#  
################################################################################  
WORKDIR /  
  
## Expose ports  
##
-----------------------------------------------------------------------------  
EXPOSE 4567  
  
CMD ["/usr/bin/supervisord"]  

