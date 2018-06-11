FROM ubuntu:16.04  
MAINTAINER James Kirkby <jkirkby91@gmail.com>  
  
# Set some environment vars  
ENV TERM xterm  
ENV DEBIAN_FRONTEND noninteractive  
ENV INITRD No  
ENV LANG en_GB.UTF-8  
ENV GOSU_VERSION 1.7  
# Surpress Upstart errors/warning  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -sf /bin/true /sbin/initctl  
  
# install some global stuff  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y --force-yes --fix-missing build-essential wget curl
fail2ban supervisor libgpg-error-dev libassuan-dev apt-transport-https ca-
certificates software-properties-common apparmor-utils libssl-dev nano
language-pack-en-base gettext-base && \  
apt-add-repository multiverse && \  
apt-get update && \  
apt-get autoremove -y && \  
apt-get clean && \  
apt-get autoclean && \  
echo -n > /var/lib/apt/extended_states && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /usr/share/man/?? && \  
rm -rf /usr/share/man/??_*  
  
# gosu  
RUN set -x \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true  
  
# Set timezone  
RUN echo "Europe/London" > /etc/timezone && \  
dpkg-reconfigure -f noninteractive tzdata  
  
# Copy supervisor config to container  
COPY confs/apparmor/supervisord.conf /etc/apparmor.d/supervisord.conf  
  
# add apparmor  
COPY confs/apparmor/abstractions/gconv-amd64
/etc/apparmor.d/abstractions/gconv-amd64  
  
# add apparmor  
COPY confs/apparmor/networkmanager.conf /etc/apparmor.d/networkmanager.conf

