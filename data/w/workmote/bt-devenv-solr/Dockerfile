FROM workmote/base:latest  
  
# Version number for Bluetent's WorkMote's Docker DevEnv Image used for solr.  
LABEL com.workmote.they.bt.devenv-solr.version="0.1"  
# Maintainer for Bluetent's WorkMote's Docker DevEnv Image used for solr.  
LABEL com.workmote.they.bt.devenv-solr.maintainer="Daniel Dalgo
<dalguete@gmail.com>"  
# Purpose of anything here installed for Bluetent's WorkMote's Docker DevEnv
Image used for solr.  
LABEL com.workmote.they.bt.devenv-solr.purpose="search"  
# Application name here installed for Bluetent's WorkMote's Docker DevEnv
Image used for solr.  
LABEL com.workmote.they.bt.devenv-solr.app="solr"  
  
# To avoid having errors like "unable to initialize frontend: Dialog" when
packages  
# are upgraded/installed.  
ARG DEBIAN_FRONTEND=noninteractive  
  
# Start everything as the expected (generally) root user, so there won't be  
# installation problems in case base image has set USER to something
different.  
USER root  
  
# 00  
# Packages installation.  
COPY 00-packages-installation/ /tmp/00-packages-installation/  
RUN /tmp/00-packages-installation/packages-installation.sh \  
&& rm -r /tmp/00-packages-installation/  
  
# 01  
# Solr Server Configs.  
COPY 01-solr-server-configs/solrd-init /usr/local/bin/  
COPY 01-solr-server-configs/ /tmp/01-solr-server-configs/  
RUN /tmp/01-solr-server-configs/solr-server-configs.sh \  
&& rm -r /tmp/01-solr-server-configs/  
EXPOSE 8983  
# 02  
# Kick off scripts scripts.  
COPY 02-kick-off/kick-off /usr/local/bin/  
COPY 02-kick-off/my-bindfs-mounts /etc/default/  
  
# 03  
# Set the main processes for supervisor to run. The reason of containers using
this image.  
COPY 03-supervisor/ /etc/supervisor/conf.d/  
  
# 04  
# Perform some final processes.  
COPY 04-finally/ /tmp/04-finally/  
RUN /tmp/04-finally/finally.sh \  
&& rm -r /tmp/04-finally/  
  
# 05  
# Setup the user to use to trigger any process inside this contained.  
ARG CustomUsername="workmote"  
USER ${CustomUsername}

