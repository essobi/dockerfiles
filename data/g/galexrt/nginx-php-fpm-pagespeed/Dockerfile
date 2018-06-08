FROM centos:7  
  
LABEL maintainer="Alexander Trost <galexrt@googlemail.com>"  
  
ENV NPS_VERSION=1.12.34.2-beta NGINX_VERSION=1.11.8  
  
RUN yum -q update -y && \  
yum -q install -y gcc-c++ pcre-devel zlib-devel make unzip wget libuuid-devel
\  
sudo pcre-devel openssl python-setuptools \  
php-fpm php-common php-mysql php-xml php-pgsql \  
php-pecl-memcache php-pdo php-odbc php-mysql php-mbstring php-ldap \  
php-intl php-gd php-bcmath php-soap php-process php-pear php-recode \  
php-pspell php-snmp php-xmlrpc && \  
adduser -r -m -d /var/cache/nginx -s /sbin/nologin nginx && \  
easy_install pip && \  
pip install supervisor && \  
mkdir -p /var/log/supervisord/ /www /certs /configs && \  
sed -i 's/;cgi.fix_pathinfo.*/cgi.fix_pathinfo=0/g' /etc/php.ini && \  
sed -i 's/user.*/user = nginx/g' /etc/php-fpm.d/www.conf && \  
sed -i 's/group.*/group = nginx/g' /etc/php-fpm.d/www.conf && \  
cd && \  
curl -f -L -sS -O https://ngxpagespeed.com/install && \  
chmod u+x install && \  
./install \--assume-yes \  
\--no-deps-check \  
\--nginx-version latest \  
\--ngx-pagespeed-version latest-stable && \  
rm -f /etc/nginx/conf.d/* && \  
mkdir -p /var/ngx_pagespeed_cache /etc/nginx/conf.d/ /var/log/nginx
/var/log/pagespeed /var/lib/php/session && \  
chown nginx:nginx -R /var/ngx_pagespeed_cache /var/log/pagespeed
/var/lib/php/session && \  
yum -q remove -y gcc-c++ pcre-devel zlib-devel make unzip wget libuuid-devel
&& \  
rm -rf /root/* /tmp/* /var/tmp/* /var/lib/yum/* /var/cache/yum/*  
  
COPY nginx.conf /usr/local/nginx/conf/nginx.conf  
COPY nginx-default.conf /etc/nginx/conf.d/default.conf  
COPY supervisord.conf /etc/supervisor/supervisord.conf  
  
VOLUME ["/www", "/certs", "/configs"]  
  
ENTRYPOINT ["/usr/bin/supervisord"]  

