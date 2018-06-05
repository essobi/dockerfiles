FROM bradegler/php5  
MAINTAINER Brad Egler <begler@gmail.com>  
  
# Install mysql  
RUN apt-get update  
RUN apt-get install -y mysql-server pwgen  
  
RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/"
/etc/mysql/my.cnf  
  
RUN echo "[program:mysqld]" > /etc/supervisor/conf.d/mysql.conf  
RUN echo "command=/usr/sbin/mysqld --basedir=/usr --datadir=/var/lib/mysql
--plugin-dir=/usr/lib/mysql/plugin --user=root --log-
error=/var/log/mysql/error.log --pid-file=/var/run/mysqld/mysqld.pid
--socket=/var/run/mysqld/mysqld.sock --port=3306" >>
/etc/supervisor/conf.d/mysql.conf  
  
# Modify nginx settings  
RUN sed -i -e"s/keepalive_timeout\s*65/keepalive_timeout 2/"
/etc/nginx/nginx.conf  
RUN sed -i -e"s/keepalive_timeout 2/keepalive_timeout
2;\n\tclient_max_body_size 100m/" /etc/nginx/nginx.conf  
  
# php-fpm config  
RUN sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g"
/etc/php5/fpm/php.ini  
RUN sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g"
/etc/php5/fpm/php.ini  
RUN sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g"
/etc/php5/fpm/php.ini  
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php5/fpm/php-
fpm.conf  
RUN sed -i -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g"
/etc/php5/fpm/pool.d/www.conf  
RUN find /etc/php5/cli/conf.d/ -name "*.ini" -exec sed -i -re
's/^(\s*)#(.*)/\1;\2/g' {} \;  
  
# Install Wordpress  
ADD http://wordpress.org/latest.tar.gz /usr/share/nginx/latest.tar.gz  
RUN cd /usr/share/nginx/ && tar xvf latest.tar.gz && rm latest.tar.gz  
RUN chown -R www-data:www-data /usr/share/nginx/wordpress  
  
ADD ./run.sh /run.sh  
RUN chmod 755 /run.sh  
  
CMD ["/run.sh"]

