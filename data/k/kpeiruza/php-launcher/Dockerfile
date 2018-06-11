FROM library/debian:stretch  
MAINTAINER kenneth@floss.cat  
# Stripdown & Install --no-install-recommends  
RUN apt-get update && \  
apt-get -qq -y upgrade && \  
apt-get -y install file libapache2-mod-php7.0 php-curl php-gettext php-mcrypt
php-intl php-soap php-gd ssl-cert unzip tar apache2 git wget php-mysql
composer pear-channels php-amqp php-amqplib php-auth-sasl php-date php-db
libapache2-mod-php composer pear-channels php-amqp php-amqplib php-auth-sasl
php-date php-db libapache2-mod-php php-bcmath php-bz2 php-cli php-common php-
curl php-enchant php-gd php-gmp php-imap php-interbase php-intl php-json php-
ldap php-mbstring php-mcrypt php-mysql php-odbc php-pgsql php-pspell php-
readline php-recode php-snmp php-soap php-sqlite3 php-sybase php-tidy php-xml
php-xmlrpc php-zip php-dompdf php-email-validator php-fdomdocument php-fpdf
php-geoip php-getid3 php-gettext php-php-gettext php-gmagick php-gnupg php-
http-request php-http-request2 php-http-webdav-server php-image-text php-
imagick php-invoker php-json-schema php-kdyby-events php-letodms-core php-
libsodium php-log php-mail php-mail-mime php-mailparse php-markdown php-mdb2
php-mdb2-driver-mysql php-mdb2-driver-pgsql php-memcache php-memcached php-mf2
php-mockery php-mockery-doc php-mongodb php-monolog php-msgpack php-net-dime
php-net-dns2 php-net-ftp php-net-idna2 php-net-imap php-net-ipv6 php-net-ldap2
php-net-ldap3 php-net-nntp php-net-publicsuffix php-net-sieve php-net-smtp
php-net-socket php-net-url php-net-url2 php-net-whois php-nette php-nrk-predis
php-numbers-words php-oauth php-parser php-patchwork-utf8 php-pclzip php-pear
php-http php-pecl-http php-pecl-http-dev php-phpdocumentor-reflection php-
phpdocumentor-reflection-common php-phpdocumentor-reflection-docblock php-
phpdocumentor-type-resolver php-phpseclib php-phpspec-prophecy php-pimple php-
pinba php-propro php-propro-dev php-proxy-manager php-psr-log php-radius php-
random-compat php-raphf php-raphf-dev php-redis php-rrd php-sabre-dav-2.1 php-
sabre-event php-sabre-http-3 php-sabre-uri php-sabre-vobject php-sabre-
vobject-3 php-sabre-xml php-sabre-dav php-services-weather php-smbclient php-
solr php-sql-formatter php-ssh2 php-stomp php-text-captcha php-text-figlet
php-text-languagedetect php-text-password php-text-template php-text-wiki php-
timer php-token-stream php-tokenreflection php-uploadprogress php-uuid php-
validate php-xml-htmlsax3 php-xml-rpc2 php-xml-svg php-yaml php-zmq
libapache2-mod-php7.0 libphp7.0-embed php7.0 php7.0-bcmath php7.0-bz2
php7.0-cgi php7.0-cli php7.0-common php7.0-curl php7.0-dba php7.0-gd
php7.0-gmp php7.0-imap php7.0-intl php7.0-json php7.0-ldap php7.0-mbstring
php7.0-mcrypt php7.0-mysql php7.0-odbc php7.0-pgsql php7.0-pspell
php7.0-readline php7.0-recode php7.0-snmp php7.0-soap php7.0-sqlite3
php7.0-tidy php7.0-xml php7.0-xmlrpc php7.0-xsl php7.0-zip && \  
rm -rf /etc/apache2/conf-enabled/* && \  
ln -s /etc/apache2/conf-available/security* /etc/apache2/conf-enabled/ && \  
a2dismod -f authn_file authz_user status autoindex reqtimeout access_compat
alias filter && \  
a2enmod -f rewrite && \  
ln -sf /dev/stdout /var/log/apache2/other_vhosts_access.log && \  
ln -sf /dev/stdout /var/log/apache2/access.log && \  
ln -sf /dev/stderr /var/log/apache2/error.log && \  
sed -i "s/.*ServerTokens.*/ServerTokens Prod/" /etc/apache2/conf-
available/security.conf && \  
sed -i "s/.*ServerSignature.*/ServerSignature Off/" /etc/apache2/conf-
available/security.conf && \  
echo "<DirectoryMatch \"/\\.git\">\nRequire all denied\n</DirectoryMatch>" >
/etc/apache2/conf-available/403-dotgit.conf && \  
a2enconf security 403-dotgit && \  
rm -r /var/log/apt/* /var/cache/apt/archives/ /usr/share/doc/ /usr/share/man
/usr/include  
  
COPY conf/vhost.conf /etc/apache2/sites-available/000-default.conf  
COPY conf/mpm_prefork.conf /etc/apache2/mods-available/mpm_prefork.conf  
  
# Purga final  
COPY functions.sh bootstrap.sh /  
EXPOSE 80  
ENTRYPOINT [ "/bootstrap.sh"]  

