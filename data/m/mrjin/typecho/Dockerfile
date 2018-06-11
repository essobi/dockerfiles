FROM ubuntu:14.04  
MAINTAINER mejin<me@jinfeijie.cn>  
  
# 安装依赖  
ENV DEBIAN_FRONTEND noninteractive  
ENV DEPENDENT supervisor git apache2 libapache2-mod-php5 mysql-server
php5-mysql pwgen php-apc php5-mcrypt php5-gd wget curl  
RUN set -x && \  
apt-get update && \  
apt-get -y install $DEPENDENT && \  
echo "ServerName localhost-bulid-mrjin" >> /etc/apache2/apache2.conf  
  
# 添加镜像配置和脚本  
ADD start-apache2.sh /start-apache2.sh  
ADD start-mysqld.sh /start-mysqld.sh  
ADD start-sshd.sh /start-sshd.sh  
ADD run.sh /run.sh  
RUN chmod 755 /*.sh  
ADD my.cnf /etc/mysql/conf.d/my.cnf  
ADD supervisord-apache2.conf /etc/supervisor/conf.d/supervisord-apache2.conf  
ADD supervisord-mysqld.conf /etc/supervisor/conf.d/supervisord-mysqld.conf  
ADD supervisord-sshd.conf /etc/supervisor/conf.d/supervisord-sshd.conf  
  
RUN set -x && pwd  
  
# 移除预安装的数据库  
RUN rm -rf /var/lib/mysql/*  
  
# 添加 MySQL utils  
ADD create_mysql_root.sh /create_mysql_root.sh  
  
# 配置使用 .htaccess  
ADD apache_default /etc/apache2/sites-available/000-default.conf  
RUN a2enmod rewrite  
  
ENV WEB_GIT_URL https://github.com/typecho/typecho.git  
# 配置/html 作为网站的根路径  
RUN mkdir -p /html && rm -rf /var/www/html && ln -s /html /var/www/html &&
chown -R www-data:www-data /html/  
RUN git clone $WEB_GIT_URL /html  
  
# 配置PHP的环境变量  
ENV PHP_UPLOAD_MAX_FILESIZE 10M  
ENV PHP_POST_MAX_SIZE 10M  
  
# 配置来自《金斐杰的网站 - openssh docker 构建文件代码》http://jinfeijie.cn/?p=50  
ENV MYSQL_USER mrjin  
ENV MYSQL_PASS jin123  
ENV ROOT_PASS jin123  
  
# 安装SSH  
RUN set -x \  
&& apt-get install -y openssh-server  
  
# 配置openssh  
RUN mkdir /var/run/sshd  
RUN echo 'root:'$ROOT_PASS |chpasswd  
RUN echo 'PermitRootLogin yes' > /etc/ssh/sshd_config  
  
RUN chmod 755 /*.sh  
  
# 为MySQL添加挂载区域  
VOLUME ["/etc/mysql", "/var/lib/mysql", "/html"]  
  
EXPOSE 80 3306 22 443  
CMD ["/run.sh"]  

