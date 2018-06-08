#  
# Debian9 (stretch) + apache 2.6  
#  
# Ideas were taken from https://hub.docker.com/r/josefcs/debian-
apache/~/dockerfile/  
#  
# Pull base image  
FROM debian:stretch  
  
# From https://hub.docker.com/_/debian/  
# Set utf8 support by default  
ENV LANG=C.UTF-8  
# Create _shibd uid.gid before package install so we can control the numeric
value of uid:gid  
RUN \  
groupadd _shibd --gid 799 && \  
useradd _shibd --uid 799 \--gid 799 \  
\--home /var/log/shibboleth --shell /bin/false  
# Make apt-get commands temporarily non-interactive  
# Solution from https://github.com/phusion/baseimage-docker/issues/58  
# Update apt cache to use fastest local mirror  
RUN \  
export DEBIAN_FRONTEND=noninteractive && \  
export DEBCONF_NONINTERACTIVE_SEEN=true && \  
apt-get update && \  
apt-get install -y apt-utils less nano emacs-nox curl apache2 libapache2-mod-
shib2 && \  
apt-get clean  
  
# Enable directory colors:  
RUN \  
sed -i "s/^# export LS/export LS/g" /root/.bashrc && \  
sed -i "s/^# eval/eval/g" /root/.bashrc && \  
sed -i "s/^# alias l/alias l/g" /root/.bashrc  
  
# Fix error that occurs with directory colors enabled  
ENV SHELL /bin/bash  
  
# Enable apache modules, disabling mpm_event because of mod_shib  
# Add apache user to _shibd  
RUN \  
a2dismod mpm_event && \  
a2enmod proxy && \  
a2enmod proxy_http && \  
a2enmod authn_core && \  
a2enmod alias && \  
a2enmod headers && \  
a2enmod authz_core && \  
a2enmod authz_host && \  
a2enmod authz_user && \  
a2enmod dir && \  
a2enmod env && \  
a2enmod mime && \  
a2enmod reqtimeout && \  
a2enmod rewrite && \  
a2enmod deflate && \  
a2enmod ssl && \  
a2enmod proxy_ajp && \  
a2enmod mpm_worker && \  
a2enmod shib2 && \  
adduser www-data _shibd  
  
# Pipe apache logging to stout/stderr  
RUN ln -sf /dev/stdout /var/log/apache2/access.log && \  
ln -sf /dev/stderr /var/log/apache2/error.log  
  
VOLUME [ "/etc/apache2", "/etc/shibboleth", "/var/log/apache2",
"/var/log/shibboleth" ]  
  
# Force start of container to also also autostart apache  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

