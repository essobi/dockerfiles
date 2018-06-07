FROM phusion/baseimage:0.9.18  
MAINTAINER "Fabio Rauber" <fabiorauber@gmail.com>  
  
ENV OS=ubuntu \  
OS_VERSION=14.04 \  
TERM=xterm  
  
RUN localedef -i pt_BR -c -f ISO-8859-1 pt_BR && \  
localedef -i pt_BR -c -f UTF-8 pt_BR && \  
echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select
true | debconf-set-selections  
  
RUN add-apt-repository "deb http://archive.ubuntu.com/ubuntu $(lsb_release
-sc) multiverse" && \  
apt-get update && apt-get upgrade -y && \  
apt-get install -y subversion \  
wget \  
apache2 \  
postgresql-client \  
libapache2-mod-proxy-html \  
libapache2-mod-php5 \  
php5-pgsql \  
php5-ldap \  
php5-gd \  
php5-dev \  
unoconv \  
default-jre \  
php-pear \  
ttf-mscorefonts-installer \  
python2.7 \  
python-psycopg2 \  
php-apc \  
php5-curl \  
php5-memcached \  
memcached \  
libmemcached-dev \  
libssh2-1-dev \  
pkg-config \  
libreoffice && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN svn co https://svn.solis.com.br/sagu2/trunk/phing/deploy instalador --no-
auth-cache << EOF\\\  
t\\\  
EOF && \  
cd instalador && \  
pecl install channel://pecl.php.net/ssh2-0.12 && \  
pear config-set preferred_state stable && \  
pear config-set auto_discover 1 && \  
pear upgrade && \  
pear channel-discover pear.phing.info && \  
pear install phing/phing && \  
pear install HTTP_Request2 && \  
pear install XML_Parser && \  
pear config-set preferred_state alpha && \  
pear install VersionControl_SVN-0.4.0 && \  
pear install Net_LDAP2  
  
RUN cd instalador && \  
sed -i 's/locate/true/g' build/ubuntu/build-*.xml && \  
sed -i 's/psql/true/g' build/ubuntu/build-*.xml && \  
sed -i 's/service/true/g' build/ubuntu/build-*.xml && \  
sed -i
's/httpd.servername=academico.instituicao.com.br/httpd.servername=localhost/g'
./properties/ubuntu/build-httpd.properties && \  
sed -i
's/httpd.servername=academico.instituicao.com.br/httpd.servername=localhost/g'
./properties/build-httpd.properties && \  
phing -Ddeploy.syncdb=false && \  
rm -rf /instalador/package && \  
a2dissite 000-default && \  
a2dissite default-ssl && \  
sed -i 's/ ServerName localhost/ SetEnvIf X-Forwarded-Proto https HTTPS=on/g'
/etc/apache2/sites-enabled/localhost.conf  
  
RUN mkdir /etc/service/apache  
ADD runit.sh /etc/service/apache/run  
  
ADD make_files_dir.sh /instalador/  
RUN /instalador/make_files_dir.sh  
  
VOLUME /var/solisge-files  
  
EXPOSE 80  

