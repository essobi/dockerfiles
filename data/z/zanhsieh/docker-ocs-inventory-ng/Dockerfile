FROM centos:6  
MAINTAINER Ming Hsieh <zanhsieh@gmail.com>  
  
RUN yum -y install epel-release ;\  
rpm -Uvh https://mirror.webtatic.com/yum/el6/latest.rpm ;\  
yum -y update ;\  
yum -y install tar gzip make httpd mysql mysql-server php56w php56w-mysql
php56w-gd php56w-pecl-memcache php56w-snmp php56w-xmlrpc php56w-pspell
php56w-mbstring php56w-pecl-zip python-pip perl-XML-Simple perl-Compress-Zlib
perl-DBI perl-DBD-MySQL perl-Apache-DBI perl-Net-IP perl-SOAP-Lite mod_perl;\  
yum clean all  
  
ADD OCSNG_UNIX_SERVER-2.2.1.tar.gz /tmp/  
ADD s6-2.3.0.0-linux-amd64-bin.tar.gz /  
WORKDIR /tmp/OCSNG_UNIX_SERVER-2.2.1/Apache  
RUN perl Makefile.PL ;\  
make ;\  
make install ;\  
cp -R blib/lib/Apache /usr/local/share/perl5/ ;\  
cp /tmp/OCSNG_UNIX_SERVER-2.2.1/etc/logrotate.d/ocsinventory-server
/etc/logrotate.d/ ;\  
mkdir -p /etc/ocsinventory-server/{plugins,perl} ;\  
mkdir -p /usr/share/ocsinventory-reports  
  
WORKDIR /tmp/OCSNG_UNIX_SERVER-2.2.1  
RUN cp -R ocsreports /usr/share/ocsinventory-reports/ ;\  
chown root:apache -R /usr/share/ocsinventory-reports/ocsreports ;\  
mkdir -p /var/lib/ocsinventory-reports/{download,ipd,logs,scripts,snmp} ;\  
chown root:apache -R /var/lib/ocsinventory-
reports/{download,ipd,logs,scripts,snmp} ;\  
cp binutils/ipdiscover-util.pl /usr/share/ocsinventory-
reports/ocsreports/ipdiscover-util.pl ;\  
chown root:apache /usr/share/ocsinventory-reports/ocsreports/ipdiscover-
util.pl ;\  
chmod 755 /usr/share/ocsinventory-reports/ocsreports/ipdiscover-util.pl  
  
COPY rootfs /  
COPY *.conf /etc/httpd/conf.d/  
COPY dbconfig.inc.php /usr/share/ocsinventory-reports/ocsreports/  
COPY init_db.sh ocsweb.sql /tmp/  
RUN chmod +w /usr/share/ocsinventory-reports/ocsreports/dbconfig.inc.php ;\  
chmod +x /tmp/init_db.sh; \  
/tmp/init_db.sh; \  
rm -fR /tmp/OCSNG_UNIX_SERVER-2.2.1  
  
EXPOSE 80 3306  
VOLUME ["/var/lib/mysql", "/var/log"]  
  
ENTRYPOINT ["/usr/local/bin/init"]  

