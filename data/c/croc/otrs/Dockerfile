FROM debian  
  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get install -y curl less postfix cron libdbd-odbc-perl libauthen-ntlm-perl
libxml-libxml-perl libxml-libxslt-perl libpdf-api2-simple-perl libyaml-
libyaml-perl libencode-hanextra-perl libjson-xs-perl libmail-imapclient-perl
libtemplate-perl libtemplate-perl libtext-csv-xs-perl libapache2-mod-perl2
libdbd-pg-perl libnet-dns-perl libnet-ldap-perl libio-socket-ssl-perl libpdf-
api2-perl libsoap-lite-perl libgd-text-perl libgd-graph-perl libapache-dbi-
perl libarchive-zip-perl libcrypt-eksblowfish-perl libcrypt-ssleay-perl
libdbd-mysql-perl libdatetime-perl apache2 libapache2-mod-perl2  
RUN curl -o /tmp/otrs.tar.gz http://ftp.otrs.org/pub/otrs/otrs-latest.tar.gz
&& \  
tar xzf /tmp/otrs.tar.gz -C /opt && \  
ln -s /opt/otrs-* /opt/otrs && \  
echo "Checking installed plugins..." && /opt/otrs/bin/otrs.CheckModules.pl &&
\  
groupadd otrs && useradd -d /opt/otrs -g www-data otrs && \  
ln -s /opt/otrs/scripts/apache2-httpd.include.conf /etc/apache2/sites-
available/otrs.conf && \  
echo "enable apache module perl" && a2enmod perl && \  
echo "enable apache site otrs" && a2ensite otrs && \  
echo "enable apache module headers" && a2enmod headers && \  
# echo "enable apache module version" && a2enmod version && \  
echo "enable apache module deflate" && a2enmod deflate && \  
echo "enable apache module filter" && a2enmod filter && \  
/opt/otrs/bin/otrs.SetPermissions.pl --web-group=www-data && \  
sed -i 's@#use DBD::mysql@use DBD::mysql@' /opt/otrs/scripts/apache2-perl-
startup.pl && \  
sed -i 's@#use Kernel::System::DB::mysql@use Kernel::System::DB::mysql@'
/opt/otrs/scripts/apache2-perl-startup.pl && \  
cp -f /opt/otrs/Kernel/Config.pm.dist /opt/otrs/Kernel/Config.pm && \  
cp -f /opt/otrs/var/cron/otrs_daemon.dist /opt/otrs/var/cron/otrs_daemon  
  
COPY files/start.sh /opt/start.sh  
RUN chmod 755 /opt/*.sh  
  
ENTRYPOINT /opt/start.sh  

