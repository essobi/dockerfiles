FROM workmote/base:latest  
  
# Version number for Bluetent's WorkMote's Docker DevEnv Image used for mysql.  
LABEL com.workmote.they.bt.devenv-mysql.version="0.1"  
# Maintainer for Bluetent's WorkMote's Docker DevEnv Image used for mysql.  
LABEL com.workmote.they.bt.devenv-mysql.maintainer="Daniel Dalgo
<dalguete@gmail.com>"  
# Purpose of anything here installed for Bluetent's WorkMote's Docker DevEnv
Image used for mysql.  
LABEL com.workmote.they.bt.devenv-mysql.purpose="db"  
# Application name here installed for Bluetent's WorkMote's Docker DevEnv
Image used for mysql.  
LABEL com.workmote.they.bt.devenv-mysql.app="mysql"  
  
# To avoid having errors like "unable to initialize frontend: Dialog" when
packages  
# are upgraded/installed.  
ARG DEBIAN_FRONTEND=noninteractive  
  
# Start everything as the expected (generally) root user, so there won't be  
# installation problems in case base image has set USER to something
different.  
USER root  
  
# 00  
# Load debconf selections for packages to be installed.  
COPY 00-packages-defaults/ /tmp/00-packages-defaults/  
RUN /tmp/00-packages-defaults/packages-defaults.sh \  
&& rm -r /tmp/00-packages-defaults/  
  
# 01  
# Packages installation.  
COPY 01-packages-installation/ /tmp/01-packages-installation/  
RUN /tmp/01-packages-installation/packages-installation.sh \  
&& rm -r /tmp/01-packages-installation/  
EXPOSE 3306  
# 02  
# DB Server Tune Ups.  
COPY 02-db-server-configs/mysqld-init /usr/local/bin/  
COPY 02-db-server-configs/apache2-init /usr/local/bin/  
COPY 02-db-server-configs/ /tmp/02-db-server-configs/  
RUN /tmp/02-db-server-configs/db-server-configs.sh \  
&& rm -r /tmp/02-db-server-configs/  
  
# 03  
# Install phpMyAdmin.  
COPY 03-phpmyadmin/ /tmp/03-phpmyadmin/  
RUN /tmp/03-phpmyadmin/phpmyadmin.sh \  
&& rm -r /tmp/03-phpmyadmin/  
EXPOSE 80 443  
# 04  
# Kick off scripts scripts.  
COPY 04-kick-off/kick-off /usr/local/bin/  
COPY 04-kick-off/my-bindfs-mounts /etc/default/  
  
# 05  
# Set the main processes for supervisor to run. The reason of containers using
this image.  
COPY 05-supervisor/ /etc/supervisor/conf.d/  
  
# 06  
# Perform some final processes.  
COPY 06-finally/ /tmp/06-finally/  
RUN /tmp/06-finally/finally.sh \  
&& rm -r /tmp/06-finally/  
  
# 07  
# Setup the user to use to trigger any process inside this contained.  
ARG CustomUsername="workmote"  
USER ${CustomUsername}

