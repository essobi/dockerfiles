##################################################  
# Docker build file providing a generic scanner  
# docker image exposing different web app scanners  
# and a few system auditers in order to use the  
# image as a command line tool  
##################################################  
# Script uses following best practices  
# https://docs.docker.com/articles/dockerfile_best-practices  
############################################  
  
# Set the base image as debian  
FROM ubuntu:14.04  
MAINTAINER Kunal Singh <knlsingh394@gmail.com>  
ENV TERM linux  
LABEL version="1.0" description="Docker build file providing a generic scanner
docker image exposing different web app scanners and a few system auditers in
order to use the image as a command line tool"  
  
# Set the locale and other env vars  
RUN locale-gen en_US.UTF-8  
ENV LANG=en_US.UTF-8 \  
LANGUAGE=en_US:en \  
LC_ALL=en_US.UTF-8 \  
LYNIS_HOME=/opt/lynis\  
NIKTO_HOME=/opt/nikto \  
FISH_HOME=/opt/skipfish \  
SQLMAP_HOME=/opt/sqlmap \  
WAPITI_HOME=/opt/wapiti \  
ZAP_HOME=/opt/zap \  
NIKTO_VERSION=2.1.5 \  
ZAP_VERSION=2.5.0 \  
FISH_VERSION=2.10b \  
WAPITI_VERSION=2.3.0 \  
LYNIS_VERSION=2.2.0  
  
# Set environments for the scanners  
RUN echo "LYNIS_HOME=$LYNIS_HOME" >> /etc/environment && \  
echo "NIKTO_HOME=$NIKTO_HOME" >> /etc/environment && \  
echo "FISH_HOME=$FISH_HOME" >> /etc/environment && \  
echo "SQLMAP_HOME=$SQLMAP_HOME" >> /etc/environment && \  
echo "WAPITI_HOME=$WAPITI_HOME" >> /etc/environment && \  
echo "ZAP_HOME=$ZAP_HOME" >> /etc/environment && \  
mkdir $NIKTO_HOME && \  
mkdir $ZAP_HOME && \  
mkdir $FISH_HOME && \  
mkdir $WAPITI_HOME  
  
# Update and install dependencies  
# perl openssl libnet-ssleay-perl: Dependencies for Nikto  
# openjdk-7-jre: Java runtime for ZAP  
# wget: To download tools  
RUN apt-get update && \  
apt-get -y install git python \  
libnet-ssleay-perl openjdk-7-jre \  
openssl perl wget gcc tar make\  
libidn11-dev libssl-dev \  
libcrypto++-dev libpcre3-dev \  
libcurl4-openssl-dev libpcre3-dev \  
# Install nmap  
nmap \  
# python2.7 python2.7-dev python-requests \  
python-dev python-requests \  
python-ctypes python-beautifulsoup \  
\--fix-missing && \  
# Cleanup  
apt-get -y autoclean && \  
apt-get -y autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
# Install lynis  
RUN wget -q -O /tmp/lynis.tgz
http://cisofy.com/files/lynis-${LYNIS_VERSION}.tar.gz && \  
tar -xzf /tmp/lynis.tgz -C /opt && \  
chmod -R +x $LYNIS_HOME && \  
chmod -R 640 $LYNIS_HOME/include && \  
rm -rf /tmp/lynis.tgz  
  
# Install nikto  
RUN wget -q -O /tmp/nikto.tgz
http://www.cirt.net/nikto/nikto-${NIKTO_VERSION}.tar.gz && \  
tar --strip-components=1 -xzf /tmp/nikto.tgz -C $NIKTO_HOME && \  
chmod -R +x $NIKTO_HOME && \  
perl $NIKTO_HOME/nikto.pl -update && \  
perl $NIKTO_HOME/nikto.pl -Version && \  
rm -rf /tmp/nikto.tgz  
  
# Install skipfish  
RUN wget -q -O /tmp/skipfish.tgz https://storage.googleapis.com/google-code-
archive-downloads/v2/code.google.com/skipfish/skipfish-2.10b.tgz && \  
tar --strip-components=1 -xzf /tmp/skipfish.tgz -C $FISH_HOME && \  
chmod -R +x $FISH_HOME && \  
cd $FISH_HOME && \  
chmod -R +x $FISH_HOME && \  
sed -i '/SHOW_SPLASH/d' src/config.h && \  
make && \  
touch $FISH_HOME/output.wl && \  
rm -rf /tmp/skipfish.tgz  
  
# Install sqlmap  
RUN cd /opt && git clone https://github.com/sqlmapproject/sqlmap.git && \  
chmod -R +x $SQLMAP_HOME  
  
# Install wapiti  
RUN wget -q -O /tmp/wapiti.tgz
http://netcologne.dl.sourceforge.net/project/wapiti/wapiti/wapiti-${WAPITI_VERSION}/wapiti-${WAPITI_VERSION}.tar.gz
&& \  
tar --strip-components=1 -zxf /tmp/wapiti.tgz -C $WAPITI_HOME && \  
chmod -R +x $WAPITI_HOME && \  
rm -rf /tmp/wapiti.tgz  
  
# Install zap  
RUN wget -q -O /tmp/zap.tgz
https://github.com/zaproxy/zaproxy/releases/download/${ZAP_VERSION}/ZAP_${ZAP_VERSION}_Linux.tar.gz
&& \  
tar --strip-components=1 -xzf /tmp/zap.tgz -C $ZAP_HOME && \  
chmod -R +x $ZAP_HOME && \  
/bin/bash $ZAP_HOME/zap.sh -version && \  
rm -rf /tmp/zap.tgz  
  
VOLUME $FISH_HOME  
COPY zap-aggressive-scan-policy.policy /root/.ZAP/policies/zap-aggressive-
scan-policy.policy  
COPY scan.sh /root/scan.sh  
RUN chmod +x /root/scan.sh  
  
ENTRYPOINT ["/bin/bash", "/root/scan.sh"]  

