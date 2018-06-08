FROM ubuntu:16.04  
ENV APP_DIR /var/www/html/app  
ENV WORKDIR /workdir  
WORKDIR ${WORKDIR}  
ADD resources ${WORKDIR}  
# Install: apache, php, mod_php, mod_pdo_mysql, PHP_XML (also known as ext-
dom), Zip Extension, mbstring, gd, curl & git  
# Install s3fs - for mounting S3 buckets  
RUN export APACHE_LOG_DIR=/var/log/apache2 && \  
export S3FS_BUILD_DEPS="automake autotools-dev g++ git libcurl4-gnutls-dev
libfuse-dev libssl-dev libxml2-dev make pkg-config" && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
apache2 \  
php7.0 \  
libapache2-mod-php7.0 \  
php7.0-mysql \  
php7.0-xml \  
php7.0-zip \  
php7.0-mbstring \  
php7.0-gd \  
php7.0-curl \  
php7.0-sqlite3 \  
git \  
wget \  
cron \  
${S3FS_BUILD_DEPS} && \  
wget https://getcomposer.org/download/1.2.0/composer.phar && \  
mv ${WORKDIR}/composer.phar /usr/local/bin/composer && \  
chmod +x /usr/local/bin/composer && \  
mkdir s3fs-fuse && \  
cd s3fs-fuse && \  
git init && \  
git remote add origin https://github.com/s3fs-fuse/s3fs-fuse.git && \  
git fetch && \  
git checkout v1.80 && \  
./autogen.sh && \  
./configure && \  
make && \  
make install && \  
cd ${WORKDIR} && \  
rm -fr ${WORKDIR}/s3fs-fuse && \  
apt-get autoremove && \  
apt-get clean -y && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/apt/*.bin && \  
a2enmod rewrite && \  
a2enmod ssl && \  
rm /var/www/html/index.html && \  
mv -v ${WORKDIR}/000-default.conf /etc/apache2/sites-
available/000-default.conf && \  
mv -v ${WORKDIR}/000-default-ssl.conf /etc/apache2/sites-
available/000-default-ssl.conf && \  
mkdir -p /etc/apache2/certs/ && \  
cp cert.* /etc/apache2/certs/ && \  
sed -i '/session required pam_loginuid.so/c\\#session required
pam_loginuid.so' /etc/pam.d/cron  
  
EXPOSE 80  
EXPOSE 443  
ENTRYPOINT ["/bin/bash", "/workdir/docker-entrypoint.sh"]  

