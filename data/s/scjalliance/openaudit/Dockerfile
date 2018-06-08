FROM ubuntu:trusty  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV OPT_MROOTPWD CorrectHorseBatteryStaple42  
  
# install all packages  
RUN echo "mysql-server mysql-server/root_password password $OPT_MROOTPWD" |
debconf-set-selections && \  
echo "mysql-server mysql-server/root_password_again password $OPT_MROOTPWD" |
debconf-set-selections && \  
apt-get update && apt-get install -y --no-install-recommends \  
apache2 \  
apache2-utils \  
ca-certificates \  
curl \  
ipmitool \  
libapache2-mod-php5 \  
libapache2-mod-proxy-html \  
librrd4 \  
libtime-modules-perl \  
logrotate \  
mysql-server \  
nmap \  
openssh-client \  
php5 \  
php5-cli \  
php5-ldap \  
php5-mcrypt \  
php5-mysql \  
php5-snmp \  
rrdtool \  
screen \  
smbclient \  
sshpass \  
wget \  
zip \  
&& \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# versions and variables  
EXPOSE 80  
ENV OAEVERSION 2.0.4  
ENV OAEDOWNLOAD http://dl-openaudit.opmantek.com/OAE-
Linux-x86_64-release_$OAEVERSION.run  
  
# fetch OAE installer from Opmantek server  
WORKDIR /tmp  
RUN curl "$OAEDOWNLOAD" -o /tmp/openaudit.run && \  
(test -f /tmp/openaudit.run || echo "[[[ FILE DOESN'T EXIST ]]]") && \  
chmod 755 /tmp/openaudit.run && \  
/tmp/openaudit.run \--check && \  
/tmp/openaudit.run \--noexec --keep && \  
rm /tmp/openaudit.run  
  
# setup mysql volume and ownership  
VOLUME /data/mysql  
CMD chown -Rf mysql: /data/mysql  
  
# install OAE  
RUN service mysql start && \  
cd /tmp/Open-AudIT* && \  
timeout -s9 5m ./installer && \  
service mysql stop  
  
# move distribution data out of the way (run.sh will move them back if
necessary)  
RUN mv /var/lib/mysql /var/lib/mysql-dist && \  
mv /usr/local/omk/conf /usr/local/omk/conf-dist  
  
# give nmap setgid as requested by OAE  
RUN chmod g+s $(which nmap)  
  
# enable php5 modules  
RUN php5enmod mcrypt  
  
# setup run.sh, which is our container init  
WORKDIR /usr/local/omk  
COPY run.sh run.sh  
RUN chmod 755 run.sh  
CMD ["./run.sh"]  

