FROM ubuntu:xenial  
MAINTAINER Jan <jan@creativesandbox.de>  
ENV LC_ALL=C.UTF-8 LANG=C.UTF-8 LANGUAGE=C.UTF-8 \  
TERM=xterm DEBIAN_FRONTEND=noninteractive TINI_VERSION=v0.17.0 \  
BACKUPPC_VERSION=4.1.5 BACKUPPC_XS_VERSION=0.57 RSYNC_BPC_VERSION=3.0.9.12  
USER 0  
EXPOSE 22 80 8080  
  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
  
ENTRYPOINT ["/tini", "--"]  
  
CMD ["/usr/local/bin/startup.sh"]  
  
ADD root /  
  
#VOLUME ["/etc/backuppc", "/root/.ssh", "/var/lib/backuppc"]  
  
RUN echo "postfix postfix/main_mailer_type select 'Internet Site'" | debconf-
set-selections && \  
echo "postfix postfix/mailname string backuppc.diskstation.lan" | debconf-set-
selections && \  
echo LC_ALL=C.UTF-8 > /etc/default/locale && \  
addgroup --gid 112 backuppc && \  
adduser --uid 107 \--system \--home /var/lib/backuppc --gid 112 --disabled-
password --shell /bin/bash backuppc && \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y --no-install-recommends par2 tzdata openssh-server libio-
socket-inet6-perl postfix supervisor apache2 apache2-utils perl smbclient
rsync tar gcc zlib1g zlib1g-dev rrdtool git make perl-doc libarchive-zip-perl
libfile-listing-perl libxml-rss-perl libcgi-session-perl iputils-ping && \  
apt-get clean && \  
cd /usr/local/src/ && \  
ln -sf /usr/share/zoneinfo/Europe/Berlin /etc/localtime && \  
/etc/postfix/post-install meta_directory=/etc/postfix create-missing && \  
cp -f /etc/services /etc/resolv.conf /etc/nsswitch.conf /etc/host.conf
/etc/hosts /etc/passwd /var/spool/postfix/etc && \  
git clone https://github.com/backuppc/backuppc.git && \  
git clone https://github.com/backuppc/rsync-bpc.git && \  
git clone https://github.com/backuppc/backuppc-xs.git && \  
git -C backuppc checkout ${BACKUPPC_VERSION} && \  
git -C rsync-bpc checkout ${RSYNC_BPC_VERSION} && \  
git -C backuppc-xs checkout ${BACKUPPC_XS_VERSION} && \  
cd /usr/local/src/backuppc-xs && perl Makefile.PL && make && make test && make
install && cd .. && \  
cd /usr/local/src/rsync-bpc && ./configure && make && make install && cd .. &&
\  
cd /usr/local/src/backuppc && \  
./makeDist --nosyntaxCheck --releasedate "`date -u "+%d %b %Y"`" \--version
${BACKUPPC_VERSION}-git && \  
tar -zxf dist/BackupPC-${BACKUPPC_VERSION}-git.tar.gz && \  
cd BackupPC-${BACKUPPC_VERSION}-git && \  
./configure.pl --hostname=backuppc \  
\--batch \  
\--scgi-port=-1 \  
\--cgi-dir /var/www/cgi-bin/backuppc \  
\--data-dir /var/lib/backuppc \  
\--hostname backuppc \  
\--html-dir /var/www/html/backuppc \  
\--html-dir-url /backuppc \  
\--install-dir /usr/share/backuppc \  
\--config-dir /etc/backuppc \  
\--log-dir /var/log/backuppc && \  
cp httpd/BackupPC.conf /etc/apache2/conf-available/backuppc.conf && \  
sed -i "/deny\ from\ all/d" /etc/apache2/conf-available/backuppc.conf && \  
sed -i "/deny\,allow/d" /etc/apache2/conf-available/backuppc.conf && \  
sed -i "/allow\ from/d" /etc/apache2/conf-available/backuppc.conf && \  
sed -i "s/export APACHE_RUN_USER=www-data/export APACHE_RUN_USER=backuppc/"
/etc/apache2/envvars && \  
sed -i "s/export APACHE_RUN_GROUP=www-data/export APACHE_RUN_GROUP=backuppc/"
/etc/apache2/envvars && \  
sed -i 's/ErrorLog ${APACHE_LOG_DIR}\/error.log/ErrorLog \/proc\/self\/fd\/1/'
/etc/apache2/apache2.conf && \  
sed -i 's/CustomLog ${APACHE_LOG_DIR}\/access.log combined/CustomLog
\/proc\/self\/fd\/1 combined/' /etc/apache2/sites-enabled/000-default.conf &&
\  
a2enconf backuppc && \  
a2enmod cgid && \  
chmod u-s /var/www/cgi-bin/backuppc/BackupPC_Admin && \  
sed -i "s/$Conf{CgiAdminUserGroup}.*/$Conf{CgiAdminUserGroup} = 'backuppc';/"
/etc/backuppc/config.pl && \  
sed -i "s/$Conf{CgiAdminUsers}.*/$Conf{CgiAdminUsers} = 'backuppc';/"
/etc/backuppc/config.pl && \  
htpasswd -cb /etc/backuppc/BackupPC.users backuppc backuppc && \  
chown -R backuppc:backuppc /etc/backuppc && \  
cp -a /etc/backuppc/ /etc/backuppc.org/ && \  
rm -rf /usr/local/src/{backuppc,backuppc-xs,rsync-bpc} && \  
mkdir -p /root/.ssh/ /var/run/sshd/ && \  
chmod +x /usr/local/bin/startup.sh /usr/lib/nagios/plugins/check_backuppc
/tini

