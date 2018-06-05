FROM docker.io/1and1internet/ubuntu-16:latest  
ARG DEBIAN_FRONTEND=noninteractive  
COPY files /  
RUN \  
apt-get update && \  
apt-get -o Dpkg::Options::=--force-confdef -y install gettext-base amavisd-new
spamassassin clamav clamav-daemon libauthen-sasl-perl libdbi-perl libnet-dns-
perl libmail-dkim-perl libnet-ldap-perl libsnmp-perl libmail-spf-perl pyzor
razor arj bzip2 cabextract cpio file gzip lhasa nomarch pax unrar-free unzip
zip zoo lzop p7zip rpm altermime ripole lrzip rsyslog && \  
adduser clamav amavis && \  
adduser amavis clamav && \  
apt-get -y clean && \  
mkdir /var/run/clamav/ && \  
chown clamav:clamav /var/run/clamav/ && \  
sed -i -e 's/AllowSupplementaryGroups false/AllowSupplementaryGroups true/g'
/etc/clamav/clamd.conf && \  
sed -i -e 's/Foreground false/Foreground true/g' /etc/clamav/clamd.conf && \  
chmod 0444 /etc/logrotate.d/logrotate && \  
chmod +x /usr/sbin/updater.sh /usr/local/bin/logrotated.sh && \  
chown -R debian-spamd:debian-spamd /etc/spamassassin/ && \  
chown -R debian-spamd:debian-spamd /var/lib/spamassassin/ && \  
rm -rf /var/lib/apt/lists/* && \  
chmod -R 0755 /hooks  
ENV DOMAIN=example.com \  
ENABLE_RAZOR_AND_PYZOR=0 \  
SMTP_IP=127.0.0.1  
EXPOSE 10024  

