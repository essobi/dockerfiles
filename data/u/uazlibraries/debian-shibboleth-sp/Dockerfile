#  
# Debian9 (stretch) + shibboleth 2.6  
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
useradd _shibd --uid 799 --gid 799 \  
\--home /var/log/shibboleth --shell /bin/false  
  
# Make apt-get commands temporarily non-interactive  
# Solution from https://github.com/phusion/baseimage-docker/issues/58  
# Update apt cache to use fastest local mirror  
RUN \  
export DEBIAN_FRONTEND=noninteractive && \  
export DEBCONF_NONINTERACTIVE_SEEN=true && \  
apt-get update && \  
apt-get install -y procps apt-utils less nano emacs-nox curl shibboleth-
sp2-utils && \  
apt-get clean  
  
# Enable directory colors:  
RUN \  
sed -i "s/^# export LS/export LS/g" /root/.bashrc && \  
sed -i "s/^# eval/eval/g" /root/.bashrc && \  
sed -i "s/^# alias l/alias l/g" /root/.bashrc  
  
# Fix error that occurs with directory colors enabled  
ENV SHELL /bin/bash  
  
# Make sure _shibd:_shibd permissions on directories we might tmp mount  
RUN \  
chown -R _shibd:_shibd /var/cache/shibboleth && \  
chown -R _shibd:_shibd /var/log/shibboleth && \  
mkdir -p /run/shibboleth && \  
chown -R _shibd:_shibd /run/shibboleth  
  
VOLUME [ "/etc/shibboleth", "/run/shibboleth", "/var/log/shibboleth" ]  
  
# Autostart shibboleth  
CMD ["/usr/sbin/shibd", "-F", "-f", "-c", "/etc/shibboleth/shibboleth2.xml",
"-u", "_shibd", "-g", "_shibd"]  

