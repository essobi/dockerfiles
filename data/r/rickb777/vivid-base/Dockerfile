FROM ubuntu:15.04  
LABEL description="\  
Creates an Ubuntu instance that includes basic OS only. \  
By setting entrypoint to /sbin/init, it will start up Ubuntu as a headless \  
desktop. A single user called 'steve' is created for you to use. \  
The timezone is initialised to Europe/London. \  
The locale is initialised to en_GB.UTF-8."  
  
# A stevedore is an archaic term for a dock worker.  
MAINTAINER Rick Beton <rickb777@bitbucker.org>  
  
EXPOSE 22  
# These configuration files allow the container to be localized as needed.  
# (See 'build' script for an easy way to set these parameters.)  
COPY etc/default-locale /etc/default/locale  
COPY etc/profile-locale /etc/profile.d/locale.sh  
COPY etc/timezone /etc/timezone  
COPY etc/language /tmp/language  
COPY etc/country /tmp/country  
  
RUN export DEBIAN_FRONTEND=noninteractive; \  
apt-get update -y && \  
apt-get -y upgrade && \  
apt-get -y install language-pack-$(cat /tmp/language) locales  
  
# Headless timezone (equivalent to 'dpkg-reconfigure tzdata')  
RUN cp -vf /usr/share/zoneinfo/$(cat /etc/timezone) /etc/localtime  
  
RUN export DEBIAN_FRONTEND=noninteractive; \  
apt-get -y install --no-install-recommends \  
file tar arc zip gzip bzip2 unzip \  
avahi-utils avahi-daemon dialog \  
curl wget rsync telnet less nano lsof \  
dnsutils iputils-ping iputils-arping iputils-tracepath net-tools apt-utils \  
ntp sudo ssh ssh-askpass ca-certificates pwgen \  
python-setuptools python-dev software-properties-common  
  
# save a bit of space in the Docker image by deleting apt sources  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# We need the prime developer 'Steve' with a home directory, sudo permission
and no password  
RUN useradd -c "Steve E. Dore" -m steve -s /bin/bash; \  
usermod --append --groups adm,sudo steve; \  
passwd -d steve; \  
echo '. ~/.extra-bashrc' >> /home/steve/.bashrc  
  
USER steve  
WORKDIR /home/steve  
COPY etc/extra-bashrc .extra-bashrc  
USER root  
  
# To start the Docker image so that it behaves just like an Ubuntu server, use  
# --entrypoint /sbin/init  
# and put "splash" as the command-option.  

