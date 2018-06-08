FROM centos:7  
MAINTAINER Adam Zheng adam.w.zheng@icloud.com  
  
ENV S6_RELEASE 1.21.2.1  
ENV SIMPLESAMLPHP_RELEASE 1.15.0  
  
#Add S6 Overlay  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v$S6_RELEASE/s6-overlay-amd64.tar.gz
/tmp/  
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C / --exclude="./bin" \  
&& tar xzf /tmp/s6-overlay-amd64.tar.gz -C /usr ./bin  
  
#Install SimpleSAMLphp Requirements  
RUN yum -y install epel-release \  
&& rpm -Uvh https://centos7.iuscommunity.org/ius-release.rpm \  
&& echo -e '[nginx]\nname=nginx
repo\nbaseurl=http://nginx.org/packages/centos/7/$basearch/\ngpgcheck=0\nenabled=1'
> /etc/yum.repos.d/nginx.repo \  
&& yum -y install nginx php56u-fpm php56u-fpm-nginx php56u-dom php56u-mbstring
php56u-pdo php56u-pecl-memcache php56u-ldap sendmail \  
&& sed -i 's/user = apache/user = nginx/' /etc/php-fpm.d/www.conf \  
&& sed -i 's/group = apache/group = nginx/' /etc/php-fpm.d/www.conf  
  
#Configure webserver  
RUN echo -e 'server {\n listen 80 default_server;\n listen [::]:80
default_server;\n server_name _;\n root /var/simplesamlphp/www/;\n index
index.php;\n\n location /simplesaml {\n alias /var/simplesamlphp/www/;\n
location ~ ^(?<prefix>/simplesaml)(?<phpfile>.+?.php)(?<pathinfo>/.*)?$ {\n
include fastcgi_params;\n fastcgi_pass 127.0.0.1:9000;\n
fastcgi_split_path_info ^(.+?.php)(/.+)$;\n fastcgi_param SCRIPT_FILENAME
$document_root$phpfile;\n fastcgi_param PATH_INFO $pathinfo if_not_empty;\n
}\n }\n\n location ~ .php$ {\n fastcgi_split_path_info ^(.+.php)(/.+)$;\n
fastcgi_pass 127.0.0.1:9000;\n fastcgi_param SCRIPT_FILENAME
$document_root$fastcgi_script_name;\n include fastcgi_params;\n add_header
Cache-control no-cache;\n }\n}' > /etc/nginx/conf.d/default.conf \  
&& mkdir -p /var/lib/php/session/ \  
&& chown -Rv nginx:nginx /var/lib/php/session/  
  
#Download SimpleSAMLphp, Archive must remain present for seeding post install.  
RUN curl -Lo /var/simplesamlphp.tar.gz
https://github.com/simplesamlphp/simplesamlphp/releases/download/v$SIMPLESAMLPHP_RELEASE/simplesamlphp-$SIMPLESAMLPHP_RELEASE.tar.gz
\  
&& tar xzf /var/simplesamlphp.tar.gz --directory /var \  
&& mv /var/simplesamlphp-* /var/simplesamlphp \  
&& touch /var/simplesamlphp/cert/breadcrumb \  
&& touch /var/simplesamlphp/log/breadcrumb  
  
#Redirect NGINX Logs  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
#Add Service NGINX to be Monitored by S6  
RUN mkdir -p /etc/services.d/nginx/ \  
&& touch /etc/services.d/nginx/run \  
&& echo '#!/usr/bin/execlineb -P' > /etc/services.d/nginx/run \  
&& echo 'nginx -g "daemon off;"' >> /etc/services.d/nginx/run  
  
#Add Service PHP-FPM to be Monitored by S6  
RUN mkdir -p /etc/services.d/php-fpm/ \  
&& touch /etc/services.d/php-fpm/run \  
&& echo '#!/usr/bin/execlineb -P' > /etc/services.d/php-fpm/run \  
&& echo '/usr/sbin/php-fpm' >> /etc/services.d/php-fpm/run \--nodaemonize \  
&& sed -i 's|pid = /run/php-fpm/php-fpm.pid|pid = /run/php-fpm.pid|g'
/etc/php-fpm.conf  
  
#Copy the SimpleSAMLphp CLI Install Script into the Container to be executed
on startup  
COPY install-simplesamlphp.sh /etc/cont-init.d/  
RUN chmod u+x /etc/cont-init.d/install-simplesamlphp.sh  
RUN yum -y update && yum clean all && rm -rf /var/cache/yum && >
/var/log/yum.log  
  
ENTRYPOINT ["/init"]  

