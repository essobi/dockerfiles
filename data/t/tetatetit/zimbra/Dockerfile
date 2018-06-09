#################################################################  
# Dockerfile to build Zimbra Collaboration 8.6 container images  
# Based on Ubuntu 14.04  
# Created by Jorge de la Cruz  
#################################################################  
FROM ubuntu:xenial  
MAINTAINER Serhiy Berezin <zimbra@tetatet.it>  
  
RUN \  
mkdir -p /var/lib/resolvconf && touch /var/lib/resolvconf/linkified && \  
apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y upgrade &&
DEBIAN_FRONTEND=noninteractive apt-get -y install \  
wget \  
openssh-client \  
bind9 \  
bind9utils \  
bind9-doc \  
dnsutils \  
libidn11 \  
libpcre3 \  
libgmp10 \  
libexpat1 \  
libstdc++6 \  
libperl5.22 \  
libaio1 \  
netcat-openbsd \  
pax \  
resolvconf \  
sqlite3 \  
sudo \  
sysstat \  
unzip \  
dialog \  
apt-utils \  
lsb-release \  
rsyslog \  
openssh-server \  
cron \  
vim \  
mc  
  
#VOLUME ["/opt/zimbra"]  
  
EXPOSE 22 25 465 587 110 143 993 995 80 443 8080 8443 7071  
  
COPY opt /opt/  
  
##Install the Zimbra Collaboration #  
  
RUN \  
sed "s/-u/-4 -u/g" /etc/default/bind9 > /etc/default/bind9.new \  
&& mv /etc/default/bind9.new /etc/default/bind9  
  
RUN \  
rm -rf /opt/zimbra \  
&& wget
https://files.zimbra.com/downloads/8.7.11_GA/zcs-8.7.11_GA_1854.UBUNTU16_64.20170531151956.tgz
\  
&& tar xzvf zcs-*.tgz && rm zcs-*.tgz  
  
RUN \  
cd zcs-* \  
&& /bin/bash -c '\  
hostname() { echo zimbra.localdomain; }; \  
export -f hostname; \  
echo "127.0.0.1 `hostname`" >> /etc/hosts; \  
echo -e "y\ny\ny\ny\ny\nn\ny\ny\ny\ny\ny\ny\ny\ny\ny\n" | ./install.sh -s \  
' \  
&& rm -rf /zcs-* \  
&& ln -s /opt/zimbra/common/lib/jvm/openjdk-1.8.0_144-zimbra /opt/zimbra/java  
  
CMD ["/bin/bash", "/opt/start.sh", "-d"]  

