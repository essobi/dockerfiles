FROM phusion/baseimage:0.9.16  
MAINTAINER E.T.Cook <e@etc.io>  
  
CMD ["/sbin/my_init"]  
  
# Expose environment variables  
ENV SECRET **RandomString**  
ENV TORAN_SCHEME http  
ENV TORAN_HTTP_PORT 80  
ENV TORAN_HTTPS_PORT 443  
ENV TORAN_HOST **ChangeMe**  
ENV TORAN_BASE_URL **NULL**  
ENV GITHUB_OAUTH **ChangeMe**  
ENV PUB_KEY **NULL**  
  
RUN apt-add-repository ppa:nginx/stable -y  
RUN export LANG=C.UTF-8; apt-add-repository ppa:ondrej/php5-5.6 -y  
  
# Add static user to keep UIDs in sync  
RUN groupadd -r alpha \  
&& useradd -r -g alpha -G sudo alpha  
  
RUN mkdir -p /home/alpha/.ssh && \  
chown -R alpha:alpha /home/alpha && \  
rm -f /etc/service/sshd/down  
  
# Install  
RUN apt-get update && \  
apt-get -y install \  
software-properties-common \  
git \  
mercurial \  
nginx \  
mysql-client \  
php5-mysql php-apc curl unzip php5-curl php5-gd php5-intl php-pear
php5-imagick \  
php5-imap php5-mcrypt php5-memcache php5-ps php5-pspell php5-recode
php5-sqlite \  
php5-tidy php5-xmlrpc php5-xsl php5-fpm php5-cli && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# nginx site conf  
ADD etc/nginx/nginx.conf /etc/nginx/nginx.conf  
ADD etc/nginx/sites-enabled/nginx-site.conf /etc/nginx/sites-available/default  
ADD etc/nginx/conf.d/upstream.conf /etc/nginx/conf.d/upstream.conf  
  
RUN mkdir /etc/service/nginx  
ADD run/nginx.sh /etc/service/nginx/run  
  
RUN mkdir /etc/service/php5-fpm  
ADD run/php5-fpm.sh /etc/service/php5-fpm/run  
  
# php5-fpm configuration  
ADD etc/php5/fpm/pool.d/www.conf /etc/php5/fpm/pool.d/  
  
# Add scripts  
RUN mkdir -p /etc/my_init.d  
ADD my_init.d/1-run.sh /etc/my_init.d/1-run.sh  
  
RUN chmod 755 /etc/my_init.d/*.sh /etc/service/php5-fpm/run
/etc/service/nginx/run  
  
# Install Toran Proxy  
RUN rm -Rf /var/www/html && \  
curl -O https://toranproxy.com/releases/toran-proxy-v1.4.0.tgz && tar zxvf
toran-proxy-v1.4.0.tgz -C /var/www && rm toran-proxy-v1.4.0.tgz && \  
cp /var/www/toran/app/config/parameters.yml.dist
/var/www/toran/app/config/parameters.yml && \  
chown -R alpha:alpha /var/www/*  
ADD toran/composer/auth.json /var/www/toran/app/toran/composer/auth.json  
  
RUN mkdir /home/alpha/mirrors && chown alpha:alpha /home/alpha/mirrors  
RUN mkdir -p /var/www/toran/app/toran/cache/ && \  
chmod -R 777 /var/www/toran/app/toran/cache/  
  
# Define mountable directories.  
VOLUME
["/var/log","/var/www/toran/app/cache","/var/www/toran/app/toran/cache"]  
  
# private expose  
EXPOSE 80 443 22

