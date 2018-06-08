FROM alpine:latest  
MAINTAINER Eric Ball <eball@ccctechcenter.org>  
  
RUN apk --update --no-cache add \  
nginx \  
php5-fpm \  
php5-pdo \  
php5-json \  
php5-openssl \  
php5-pgsql \  
php5-pdo_pgsql \  
php5-mcrypt \  
php5-sqlite3 \  
php5-pdo_sqlite \  
php5-ctype \  
php5-zlib \  
php5-xml \  
php5-gd \  
curl \  
py-pip \  
php5-curl \  
php5-zip \  
php5-dom \  
supervisor  
  
RUN ln -s `which php5` /usr/bin/php  
  
ADD build_pdftk.sh /bin/  
ENV VER_PDFTK=2.02  
RUN apk --no-cache add --update unzip wget make fastjar gcc gcc-java g++ && \  
/bin/build_pdftk.sh && \  
apk del build-base unzip wget make fastjar && \  
rm -rf /var/cache/apk/* && \  
pdftk  
  
# Configure supervisor  
RUN pip install --upgrade pip && \  
pip install supervisor-stdout  
  
RUN mkdir -p /etc/nginx  
RUN mkdir -p /run/nginx  
RUN mkdir -p /var/run/php5-fpm  
RUN mkdir -p /var/log/supervisor  
  
RUN rm /etc/nginx/nginx.conf  
ADD nginx.conf /etc/nginx/nginx.conf  
  
RUN rm /etc/php5/php-fpm.conf  
ADD php-fpm.conf /etc/php5/php-fpm.conf  
  
RUN rm -f /etc/php5/php.ini  
ADD php.ini /etc/php5/php.ini  
  
VOLUME ["/var/www", "/etc/nginx/sites-enabled"]  
  
ADD nginx-supervisor.ini /etc/supervisor.d/nginx-supervisor.ini  
ENV TIMEZONE America/Los_Angeles  
  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
  
EXPOSE 80 9000  
CMD ["/usr/bin/supervisord"]  

