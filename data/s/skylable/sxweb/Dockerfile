FROM centos:centos7  
MAINTAINER Skylable Dev-Team <dev-team@skylable.com>  
  
# Install deps  
RUN yum clean all && \  
yum -y update && \  
yum -y install epel-release && \  
yum -y install php-cli php-fpm php-mysql \  
php-ZendFramework php-ZendFramework-Db-Adapter-Pdo-Mysql \  
php-guzzlehttp-streams.noarch php-guzzle-Guzzle.noarch php-Monolog.noarch
nginx \  
php-gd php-mysql php-pdo php-xml php-mbstring php-process \  
wget sudo bwm-ng git pwgen mariadb telnet supervisor && \  
yum clean all;  
  
copy skylable.repo /etc/yum.repos.d/  
  
RUN yum -y install skylable-sx  
#RUN git clone -b 0.9.1 http://git.skylable.com/sxweb /var/www/sxweb  
RUN git clone http://git.skylable.com/sxweb /var/www/sxweb  
  
copy nginx-sxweb.conf /etc/nginx/conf.d/  
copy nginx.conf /etc/nginx/  
copy php-fpm-www.conf /etc/php-fpm.d/www.conf  
copy config.inc.php /var/www/sxweb/public/  
copy run.sh /  
copy supervisord.conf /etc/supervisor/supervisord.conf  
  
# Modify permissions  
RUN find /var/www/sxweb -type d -exec chmod 755 {} \; && \  
find /var/www/sxweb -type f -exec chmod 644 {} \; && \  
chown -R root:root /var/www/sxweb && \  
mkdir -p /var/www/sxweb/data && \  
mkdir -p /var/www/sxweb/data/logs && \  
find /var/www/sxweb/data -type d -exec chmod 700 {} \; && \  
chown -R nginx /var/www/sxweb/data && \  
chmod 750 /var/www/sxweb/application/configs/ && \  
chown nginx /var/www/sxweb/application/configs/ && \  
chown nginx /var/www/sxweb/public/ && \  
chown nginx /var/www/sxweb/public/install.php && \  
mkdir -p /var/lib/php/session && \  
chown nginx:nginx /var/lib/php/session  
  
  
EXPOSE 443 80 3306  
CMD ["/run.sh"]  

