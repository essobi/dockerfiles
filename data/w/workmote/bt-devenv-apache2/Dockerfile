FROM workmote/base:latest  
  
# Version number for Bluetent's WorkMote's Docker DevEnv Image used for
apache2.  
LABEL com.workmote.they.bt.devenv-apache2.version="0.1"  
# Maintainer for Bluetent's WorkMote's Docker DevEnv Image used for apache2.  
LABEL com.workmote.they.bt.devenv-apache2.maintainer="Daniel Dalgo
<dalguete@gmail.com>"  
# Purpose of anything here installed for Bluetent's WorkMote's Docker DevEnv
Image used for apache2.  
LABEL com.workmote.they.bt.devenv-apache2.purpose="web"  
# Application name here installed for Bluetent's WorkMote's Docker DevEnv
Image used for apache2.  
LABEL com.workmote.they.bt.devenv-apache2.app="apache2"  
  
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
EXPOSE 80 443  
# 01  
# Web Server Configs.  
COPY 01-web-server-configs/apache2-init /usr/local/bin/  
COPY 01-web-server-configs/php-fpm-init /usr/local/bin/  
COPY 01-web-server-configs/solr-integration-init /usr/local/bin/  
COPY 01-web-server-configs/ /tmp/01-web-server-configs/  
RUN /tmp/01-web-server-configs/web-server-configs.sh \  
&& rm -r /tmp/01-web-server-configs/  
  
# 02  
# Enable SSL.  
COPY 02-enable-ssl/ /tmp/02-enable-ssl/  
RUN /tmp/02-enable-ssl/enable-ssl.sh \  
&& rm -r /tmp/02-enable-ssl/  
  
# 03  
# Install Ioncube.  
COPY 03-ioncube/ioncube-iface-init /usr/local/bin/  
COPY 03-ioncube/ /tmp/03-ioncube/  
RUN /tmp/03-ioncube/ioncube.sh \  
&& rm -r /tmp/03-ioncube/  
  
# 04  
# Install Composer.  
COPY 04-composer/ /tmp/04-composer/  
RUN /tmp/04-composer/composer.sh \  
&& rm -r /tmp/04-composer/  
  
# 05  
# Install Drush.  
COPY 05-drush/ /tmp/05-drush/  
RUN /tmp/05-drush/drush.sh \  
&& rm -r /tmp/05-drush/  
  
# 06  
# Install General Utility Tools.  
COPY 06-utility-tools/ /tmp/06-utility-tools/  
RUN /tmp/06-utility-tools/utility-tools.sh \  
&& rm -r /tmp/06-utility-tools/  
  
# 07  
# Install Bluetent tools.  
COPY 07-bt-tools/ /tmp/07-bt-tools/  
RUN /tmp/07-bt-tools/bt-tools.sh \  
&& rm -r /tmp/07-bt-tools/  
  
# 08  
# Kick off scripts scripts.  
COPY 08-kick-off/kick-off /usr/local/bin/  
COPY 08-kick-off/my-bindfs-mounts /etc/default/  
  
# 09  
# Set the main processes for supervisor to run. The reason of containers using
this image.  
COPY 09-supervisor/ /etc/supervisor/conf.d/  
  
# 10  
# Perform some final processes.  
COPY 10-finally/ /tmp/10-finally/  
RUN /tmp/10-finally/finally.sh \  
&& rm -r /tmp/10-finally/  
  
# 11  
# Setup the user to use to trigger any process inside this contained.  
ARG CustomUsername="workmote"  
USER ${CustomUsername}

