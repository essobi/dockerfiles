FROM debian:jessie  
MAINTAINER Tobias Knipping <knipping@tk-schulsoftware.de>  
  
# Enable Backports  
RUN awk '$1 ~ "^deb" { $3 = $3 "-backports"; print; exit }'
/etc/apt/sources.list > /etc/apt/sources.list.d/backports.list  
# Update the package repository  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get upgrade -y && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y wget curl locales git ca-
certificates unzip  
  
# Configure timezone and locale  
RUN echo "Europe/Berlin" > /etc/timezone && \  
dpkg-reconfigure -f noninteractive tzdata && \  
echo "de_DE.UTF-8 UTF-8" > /etc/locale.gen && \  
locale-gen de_DE.UTF-8 && \  
DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales && \  
/usr/sbin/update-locale LANG=de_DE.UTF-8  
ENV LANGUAGE=de_DE.UTF-8 LANG=de_DE.UTF-8 LC_ALL=de_DE.UTF-8  
  
# Install Postgres and Java (for SonarScanner)  
# explicitly set user/group IDs  
RUN groupadd -r postgres --gid=999 && useradd -r -g postgres --uid=999
postgres  
  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main" >
/etc/apt/sources.list.d/pgdg.list && \  
curl -sS https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - &&
\  
DEBIAN_FRONTEND=noninteractive apt-get update -yqq && \  
DEBIAN_FRONTEND=noninteractive apt-get install postgresql-9.6 postgresql-
contrib-9.6 libpq-dev openjdk-8-jre-headless -yqq  
  
# Added dotdeb to apt  
RUN echo "deb http://packages.dotdeb.org jessie all" >>
/etc/apt/sources.list.d/dotdeb.org.list && \  
echo "deb-src http://packages.dotdeb.org jessie all" >>
/etc/apt/sources.list.d/dotdeb.org.list && \  
curl -sS http://www.dotdeb.org/dotdeb.gpg | apt-key add -  
  
# Install PHP 7.0  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -yqq; \  
DEBIAN_FRONTEND=noninteractive apt-get install -y php7.0 php7.0-apcu
php7.0-cli php7.0-common php7.0-curl php7.0-dev php7.0-gd php7.0-igbinary
php7.0-intl php7.0-json php7.0-ldap php7.0-mbstring php7.0-mcrypt
php7.0-memcached php7.0-msgpack php7.0-opcache php7.0-pgsql php7.0-readline
php7.0-redis php7.0-xml php7.0-zip  
  
# Let's set the default timezone in cli config  
RUN sed -i 's/\;date\\.timezone\ \=/date\\.timezone\ \=\ Europe\/Berlin/g'
/etc/php/7.0/cli/php.ini  
  
# Setup Composer and PHPUnit  
RUN curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer && \  
curl --location --output /usr/local/bin/phpunit
https://phar.phpunit.de/phpunit.phar && \  
chmod +x /usr/local/bin/phpunit  
  
# Install Node, npm, bower for assets  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash - && \  
apt-get install -yyq nodejs && \  
npm install -g bower && \  
ln -s /usr/bin/nodejs /usr/local/bin/node  
  
# Adding letsencrypt-ca to truststore  
RUN export KEYSTORE=/etc/ssl/certs/java/cacerts && \  
mkdir /usr/share/ca-certificates/le && \  
wget -P /usr/share/ca-certificates/le/
https://letsencrypt.org/certs/letsencryptauthorityx1.der && \  
wget -P /usr/share/ca-certificates/le/
https://letsencrypt.org/certs/letsencryptauthorityx2.der && \  
wget -P /usr/share/ca-certificates/le/ https://letsencrypt.org/certs/lets-
encrypt-x1-cross-signed.pem && \  
wget -P /usr/share/ca-certificates/le/ https://letsencrypt.org/certs/lets-
encrypt-x2-cross-signed.pem && \  
wget -P /usr/share/ca-certificates/le/ https://letsencrypt.org/certs/lets-
encrypt-x3-cross-signed.pem && \  
wget -P /usr/share/ca-certificates/le/ https://letsencrypt.org/certs/lets-
encrypt-x4-cross-signed.pem && \  
echo "le/lets-encrypt-x1-cross-signed.pem" >> /etc/ca-certificates.conf && \  
echo "le/lets-encrypt-x2-cross-signed.pem" >> /etc/ca-certificates.conf && \  
echo "le/lets-encrypt-x3-cross-signed.pem" >> /etc/ca-certificates.conf && \  
echo "le/lets-encrypt-x4-cross-signed.pem" >> /etc/ca-certificates.conf && \  
keytool -trustcacerts -keystore $KEYSTORE -storepass changeit -noprompt
-importcert -alias letsencryptx1 -file /usr/share/ca-
certificates/le/letsencryptauthorityx1.der && \  
keytool -trustcacerts -keystore $KEYSTORE -storepass changeit -noprompt
-importcert -alias letsencryptx2 -file /usr/share/ca-
certificates/le/letsencryptauthorityx2.der && \  
keytool -trustcacerts -keystore $KEYSTORE -storepass changeit -noprompt
-importcert -alias letsencryptauthorityx1 -file /usr/share/ca-
certificates/le/lets-encrypt-x1-cross-signed.pem && \  
keytool -trustcacerts -keystore $KEYSTORE -storepass changeit -noprompt
-importcert -alias letsencryptauthorityx2 -file /usr/share/ca-
certificates/le/lets-encrypt-x2-cross-signed.pem && \  
keytool -trustcacerts -keystore $KEYSTORE -storepass changeit -noprompt
-importcert -alias letsencryptauthorityx3 -file /usr/share/ca-
certificates/le/lets-encrypt-x3-cross-signed.pem && \  
keytool -trustcacerts -keystore $KEYSTORE -storepass changeit -noprompt
-importcert -alias letsencryptauthorityx4 -file /usr/share/ca-
certificates/le/lets-encrypt-x4-cross-signed.pem && \  
update-ca-certificates --fresh  
  
RUN curl --location --output /opt/sonar-scanner-2.8.zip
https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-
scanner-2.8.zip && \  
unzip /opt/sonar-scanner-2.8.zip -d /opt/ && \  
chmod 777 -R /opt/sonar-scanner-2.8/bin  
  
RUN mkdir -p /var/run/postgresql && chown -R postgres /var/run/postgresql  
ENV PATH=/usr/lib/postgresql/9.6/bin:$PATH PGDATA=/var/lib/postgresql/data  
  
USER postgres  
RUN initdb -E 'UTF-8' --lc-collate='de_DE.UTF-8' --lc-ctype='de_DE.UTF-8'  
  
USER root  
  
CMD ["php", "-a"]  

