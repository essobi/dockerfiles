FROM centos:7  
MAINTAINER Zinway <z@zin.so>  
  
# change timezone for CST  
RUN ln -snf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  
  
# disable delta RPMs  
RUN echo "deltarpm=0" >> /etc/yum.conf  
  
# Install tools  
RUN yum install -y yum-utils epel-release python-setuptools psmisc unzip mysql  
  
#Install yum repos and utils  
RUN rpm -Uvh http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-
centos-7-0.el7.ngx.noarch.rpm && \  
rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-7.rpm && \  
yum-config-manager -q --enable remi && \  
yum-config-manager -q --enable remi-php55  
  
# Install nginx, php-fpm and php extensions  
RUN yum install -y nginx  
RUN yum install -y php-fpm  
RUN yum install -y php-mysqlnd php-mysqli php-gd php-mcrypt php-zip php-xml
php-iconv php-curl php-soap php-simplexml php-pdo php-dom php-cli php-mbstring
php-pecl-geoip php-devel GeoIP-devel  
  
# Clean up yum repos to save spaces  
RUN yum update -y && yum clean all  
  
# tweak nginx config  
RUN sed -i -e"s/worker_processes 1/worker_processes 4/" /etc/nginx/nginx.conf  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
# tweak php-fpm config  
RUN sed -i -e "s/;date.timezone =.*/date.timezone = Asia\/Shanghai/"
/etc/php.ini  
RUN sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g" /etc/php.ini  
#RUN sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g"
/etc/php.ini  
#RUN sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g" /etc/php.ini  
RUN sed -i -e "s/daemonize\s*=\s*yes/daemonize = no/g" /etc/php-fpm.conf  
RUN sed -i -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g"
/etc/php-fpm.d/www.conf  
#RUN sed -i -e "s/pm.max_children = 5/pm.max_children = 9/g" /etc/php-
fpm.d/www.conf  
#RUN sed -i -e "s/pm.start_servers = 2/pm.start_servers = 3/g" /etc/php-
fpm.d/www.conf  
#RUN sed -i -e "s/pm.min_spare_servers = 1/pm.min_spare_servers = 2/g"
/etc/php-fpm.d/www.conf  
#RUN sed -i -e "s/pm.max_spare_servers = 3/pm.max_spare_servers = 4/g"
/etc/php-fpm.d/www.conf  
#RUN sed -i -e "s/pm.max_requests = 500/pm.max_requests = 200/g" /etc/php-
fpm.d/www.conf  
RUN sed -i -e "s/php_admin_flag\\[log_errors\\] =
.*/;php_admin_flag[log_errors] =/" \  
-e "s/php_admin_value\\[error_log\\] =.*/;php_admin_value[error_log] =/" /etc/php-fpm.d/www.conf && \  
echo "php_admin_value[display_errors] = 'stderr'" >> /etc/php-fpm.d/www.conf  
  
# fix ownership of sock file for php-fpm as our version of nginx runs as nginx  
RUN sed -i -e "s/listen = 127.0.0.1:9000/listen = \/var\/run\/php5-fpm.sock/g"
\  
-e "s/user = apache/user = nginx/g" \  
-e "s/group = apache/group = nginx/g" \  
-e "s/;listen.owner = nobody/listen.owner = nginx/g" \  
-e "s/;listen.group = nobody/listen.group = nginx/g" \  
-e "s/;listen.mode = 0660/listen.mode = 0750/g" /etc/php-fpm.d/www.conf  
  
# add missing always_populate_raw_post_data = -1 to php.ini (bug #8, piwik bug
#6468)  
RUN sed -i 's/;always_populate_raw_post_data/always_populate_raw_post_data/g'
/etc/php.ini  
  
# install nginx piwik config  
ADD nginx-piwik.conf /etc/nginx/conf.d/default.conf  
  
# download piwik  
RUN curl -O "http://builds.piwik.org/piwik.zip"  
  
# unarchive piwik  
RUN unzip piwik.zip  
  
# add GeoIPCity support  
RUN echo "geoip.custom_directory=/piwik/misc" >> /etc/php.d/geoip.ini  
RUN curl -o -
http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz | gzip
-d - > /piwik/misc/GeoIPCity.dat  
  
# add piwik config  
ADD config.ini.php /piwik/config/config.ini.php  
  
# add init-piwik.sh  
ADD init-piwik.sh /opt/init-piwik.sh  
  
#Install supervisor  
RUN easy_install supervisor  
  
# Adding the configuration file of the Supervisor  
ADD supervisord.conf /etc/  
  
# add serve-piwik.sh  
ADD serve-piwik.sh /opt/serve-piwik.sh  
RUN chmod +x /opt/serve-piwik.sh  
  
# Set the port to 80  
EXPOSE 80  
# start piwik  
CMD ["/opt/serve-piwik.sh"]  

