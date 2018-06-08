FROM livingstoneonline/base:alpine  
MAINTAINER Nigel Banks <nigel.g.banks@gmail.com>  
  
LABEL "License"="GPLv3" \  
"Version"="0.0.1"  
  
EXPOSE 80  
  
ARG DRUPAL_VERSION="7.54"  
ARG DRUSH_VERSION="8.1.10"  
  
ENV DRUPAL_ROOT=/var/www/localhost/htdocs  
  
WORKDIR ${DRUPAL_ROOT}  
  
RUN apk-install \  
apache2 \  
apache2-proxy \  
apache2-utils \  
bash \  
coreutils \  
git \  
lftp \  
mysql-client \  
php5-apache2 \  
php5-ctype \  
php5-curl \  
php5-ftp \  
php5-gd \  
php5-json \  
php5-mysql \  
php5-openssl \  
php5-pdo \  
php5-pdo_mysql \  
php5-pear \  
php5-phar \  
php5-posix \  
php5-soap \  
php5-xml \  
php5-xmlreader \  
php5-xsl \  
php5-zip \  
py-pip \  
python \  
&& \  
pip install --upgrade pip && \  
pip install csvkit && \  
mkdir /run/apache2 && \  
chown -R apache:apache /var/www && \  
chmod 2775 /var/www/localhost && \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin && \  
mv /usr/local/bin/composer.phar /usr/local/bin/composer && \  
chmod a+x /usr/local/bin/composer && \  
curl -L -o /usr/local/bin/drush https://github.com/drush-
ops/drush/releases/download/${DRUSH_VERSION}/drush.phar && \  
chmod a+x /usr/local/bin/drush && \  
s6-setuidgid apache drush dl -y --destination=/var/www/localhost --drupal-
project-rename=htdocs drupal-${DRUPAL_VERSION} && \  
s6-setuidgid apache mkdir ${DRUPAL_ROOT}/sites/all/modules/contrib \  
${DRUPAL_ROOT}/sites/all/modules/custom \  
${DRUPAL_ROOT}/sites/all/modules/features && \  
cleanup  
  
COPY build /build  
  
# Custom ImageMagick build, see packages image.  
RUN echo '/build/repository' >> /etc/apk/repositories && \  
cp /build/ssh.rsa.pub /etc/apk/keys && \  
apk-install imagemagick-custom  
  
# Install Drupal dependencies  
RUN cd ${DRUPAL_ROOT} && drush make -y --no-cache /build/dependencies.make &&
\  
chown -R apache:apache ${DRUPAL_ROOT} && \  
cleanup  
  
COPY rootfs /  

