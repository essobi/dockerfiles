FROM ubuntu:16.04  
MAINTAINER Robin Ostlund <me@robinostlund.name>  
  
  
##################################################################  
# avoid debconf and initrd  
ENV DEBIAN_FRONTEND noninteractive  
ENV INITRD No  
ENV LETSENCRYPT_HOME=/opt/letsencrypt  
ENV LETSENCRYPT_VERSION=latest  
  
##################################################################  
# create folders  
RUN mkdir -p /root/bin  
RUN mkdir -p /root/haproxy  
  
##################################################################  
# install packages  
RUN apt-get update  
RUN apt-get -y upgrade  
  
# basic requirements  
RUN apt-get -y install apt-utils supervisor software-properties-common wget
openssl cron git rsyslog curl lsof  
  
# install repositorys  
RUN add-apt-repository -y ppa:vbernat/haproxy-1.8 && \  
add-apt-repository -y ppa:certbot/certbot  
  
# install haproxy and letsencrypt and configure rsyslog  
RUN apt-get update && \  
apt-get install -y haproxy hatop && \  
  
# fix container bug for syslog, by disabling: emerg and imklog  
sed -i 's/\$KLogPermitNonKernelFacility/#$KLogPermitNonKernelFacility/g'
/etc/rsyslog.conf && \  
sed -i "s|\\*.emerg|\\#\\*.emerg|" /etc/rsyslog.conf && \  
sed -i 's/$ModLoad imklog/#$ModLoad imklog/' /etc/rsyslog.conf && \  
  
# enable rsyslog logging for haproxy  
rm -f /etc/rsyslog.d/49-haproxy.conf && \  
echo "\$AddUnixListenSocket /var/lib/haproxy/dev/log" >
/etc/rsyslog.d/49-haproxy.conf && \  
echo "local0.=info /data/var/log/haproxy/haproxy_info.log" >>
/etc/rsyslog.d/49-haproxy.conf && \  
echo "& stop" >> /etc/rsyslog.d/49-haproxy.conf && \  
echo "local0.notice /data/var/log/haproxy/haproxy_notice.log" >>
/etc/rsyslog.d/49-haproxy.conf && \  
echo "& stop" >> /etc/rsyslog.d/49-haproxy.conf && \  
  
# change path for haproxy logrotate  
sed -i
's/\/var\/log\/haproxy.log/\/data\/var\/log\/haproxy\/haproxy_\\*.log/g'
/etc/logrotate.d/haproxy && \  
# cleanup  
rm -f /etc/haproxy/haproxy.cfg && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/* && \  
  
# configure hatop  
echo "#!/bin/bash" > /usr/local/bin/hatop && \  
echo "/usr/bin/hatop -s /run/haproxy/admin.sock" >> /usr/local/bin/hatop && \  
chmod 755 /usr/local/bin/hatop && \  
  
# install letsencrypt  
wget -O /etc/ssl/certs/lets-encrypt-x3-cross-signed.pem
https://letsencrypt.org/certs/lets-encrypt-x3-cross-signed.pem.txt && \  
wget -O /etc/ssl/certs/letsencryptauthorityx3.pem
https://letsencrypt.org/certs/letsencryptauthorityx3.pem.txt && \  
mkdir -p $LETSENCRYPT_HOME && \  
cd $LETSENCRYPT_HOME && \  
git clone https://github.com/letsencrypt/letsencrypt && \  
if [ "${LETSENCRYPT_VERSION}" != "latest" ]; \  
then cd letsencrypt && git checkout tags/v${LETSENCRYPT_VERSION} ; \  
fi && \  
/opt/letsencrypt/letsencrypt/letsencrypt-auto --no-self-upgrade --help  
  
##################################################################  
# copy files  
COPY supervisord/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY scripts/* /usr/local/bin/  
COPY haproxy /root/haproxy  
RUN chmod +x /usr/local/bin/*  
  
##################################################################  
# ports  
EXPOSE 80  
EXPOSE 443  
  
##################################################################  
# volumes  
VOLUME /data  
  
##################################################################  
# specify healthcheck script  
HEALTHCHECK CMD /usr/local/bin/healthcheck.sh || exit 1  
  
CMD ["supervisord"]  

