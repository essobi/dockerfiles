FROM alpine:edge  
MAINTAINER Jakob Gillich <jakob@gillich.me>  
  
ARG INVOICEPLANE_VERSION=1.4.10  
ENV UID=991 GID=991 \  
TZ=Etc/UTC \  
INVOICEPLANE_URL=http://localhost:8888  
RUN apk add --no-cache \  
nginx \  
gettext \  
su-exec \  
tzdata \  
s6 \  
ca-certificates \  
mariadb \  
mariadb-client \  
pwgen \  
php7 \  
php7-fpm \  
php7-mbstring \  
php7-gd \  
php7-mcrypt \  
php7-opcache \  
php7-json \  
php7-pdo \  
php7-pdo_mysql \  
php7-mysqli \  
php7-zlib \  
php7-xmlrpc \  
php7-openssl \  
&& mkdir /invoiceplane \  
&& INVOICEPLANE_ZIP=v${INVOICEPLANE_VERSION}.zip \  
&& wget -q
https://github.com/InvoicePlane/InvoicePlane/releases/download/v${INVOICEPLANE_VERSION}/${INVOICEPLANE_ZIP}
\  
&& unzip $INVOICEPLANE_ZIP -d /invoiceplane && rm $INVOICEPLANE_ZIP \  
# setup will complain if it doesn't exist.  
&& mkdir /invoiceplane/uploads/customer_files  
  
COPY config.php /invoiceplane/application/config/config.php  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY php-fpm.conf /etc/php7/php-fpm.conf  
COPY my.cnf /etc/mysql/my.cnf  
COPY run.sh /usr/local/bin/run.sh  
COPY setup.sh /usr/local/bin/setup.sh  
COPY s6.d /etc/s6.d  
  
RUN chmod +x /usr/local/bin/* /etc/s6.d/*/* /etc/s6.d/.s6-svscan/*  
  
VOLUME /data  
  
EXPOSE 8888  
LABEL description="A free and open source invoicing application" \  
invoiceplane="InvoicePlane v${INVOICEPLANE_VERSION}"  
  
CMD ["run.sh"]

