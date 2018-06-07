#  
# ementux/nginx-php-serf  
#  
# Nginx with necessary php modules and Serf for scalable website  
#  
# See https://github.com/ementux/docker  
#  
FROM ementux/base  
MAINTAINER Michal Grna <michal.grna@ementux.org>  
  
# install php + modules, unzip & supervisor  
RUN yum -y update && yum -y install nginx php-fpm php-common php-pecl-apc php-
cli php-pdo php-mysqlnd php-pecl-memcached php-gd php-xml php-mbstring php-
mcrypt unzip && yum clean all  
  
# add configuration file and wrapper for Nginx  
COPY nginx.conf /etc/nginx/nginx.conf  
RUN mkdir -p /etc/service/nginx/  
COPY nginx.run /etc/service/nginx/run  
RUN chmod 755 /etc/service/nginx/run  
  
# add configuration file and wrapper for PHP-FPM  
RUN sed -i -r 's/^user = apache/user = nginx/; s/^group = apache/group =
nginx/' /etc/php-fpm.d/www.conf  
RUN mkdir -p /etc/service/php-fpm/  
COPY php-fpm.run /etc/service/php-fpm/run  
RUN chmod 755 /etc/service/php-fpm/run  
  
# install Serf  
ADD https://dl.bintray.com/mitchellh/serf/0.6.4_linux_amd64.zip /tmp/serf.zip  
RUN unzip /tmp/serf.zip -d /usr/local/bin/  
RUN rm /tmp/serf.zip  
  
# add configuration files and handlers for Serf  
COPY serf-config /etc/serf  
RUN mkdir -p /etc/service/serf/  
COPY serf.run /etc/service/serf/run  
RUN chmod 755 /etc/service/serf/run  
  
# add application volume  
VOLUME [ "/srv/www/logs" , "/srv/www/public_html" ]  
RUN chown -R nginx:nginx /srv/www  
  
# expose http & Serf ports  
EXPOSE 80 7946 7373  
# start webserver (nginx + php-fpm) and Serf  
ENTRYPOINT [ "/usr/sbin/runit_bootstrap" ]  

