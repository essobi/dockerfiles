# vim: ft=dockerfile syn=dockerfile fileencoding=utf-8 sw=2 ts=2 ai eol et si  
#  
# Dockerfile:  
# Debian Docker Base With Unsecure SSH Server for Continuous Integration  
#  
# (c) 2018 Laurent Vallar <val@zbla.net>, MIT license see LICENSE file.  
ARG DEB_DIST=stretch  
FROM "debian:${DEB_DIST}-slim"  
ARG DEB_DIST=stretch  
  
LABEL Description="Debian Docker Base With Unsecure SSH Server for Continuous
\  
Integration"  
  
# Configured account  
ARG DOCKER_USER=admin  
ARG DOCKER_USER_UID=1337  
ARG DOCKER_USER_GID=1337  
# Set some build environment variables  
ARG DEB_MIRROR_URL=http://deb.debian.org/debian  
ARG DEB_SECURITY_MIRROR_URL=http://security.debian.org  
ARG DEB_COMPONENTS="main"  
ARG DEB_PACKAGES="openssh-server sudo"  
# Tell debconf to run in non-interactive mode  
ENV DEBIAN_FRONTEND noninteractive  
  
# Set neutral language  
ENV LC_ALL C  
ENV LANG C  
  
# Fix TERM  
ENV TERM linux  
  
# Initialize minimal sources.list, update all & install OpenSSH server  
RUN echo "deb $DEB_MIRROR_URL $DEB_DIST $DEB_COMPONENTS" \  
> /etc/apt/sources.list && \  
echo "deb $DEB_SECURITY_MIRROR_URL $DEB_DIST/updates $DEB_COMPONENTS" \  
>> /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get -y dist-upgrade && \  
apt-get install --no-install-recommends -y $DEB_PACKAGES && \  
apt-get -y autoremove && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Set Timezone  
RUN echo "Etc/UTC" > /etc/timezone && dpkg-reconfigure -f noninteractive
tzdata  
  
# Cleanups  
RUN rm -rf /tmp/* /var/tmp/*  
  
# Create and configure DOCKER_USER with sudo access  
RUN groupadd -g ${DOCKER_USER_GID} ${DOCKER_USER} && \  
useradd -m ${DOCKER_USER} -u ${DOCKER_USER_UID} -g ${DOCKER_USER} \  
-s /bin/bash && ( echo "${DOCKER_USER}:${DOCKER_USER}" | chpasswd ) && \  
adduser ${DOCKER_USER} sudo  
  
# Allow SSH serveur connections  
EXPOSE 22  
# Create sshd privilege separation directory  
RUN install -o root -g root -m 0755 -d /run/sshd  
  
# Start ssh services.  
CMD ["/usr/sbin/sshd", "-4", "-D", "-o", "UseDNS=no", "-o", "UsePAM=no"]  

