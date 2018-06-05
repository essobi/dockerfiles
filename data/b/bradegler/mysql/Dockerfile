FROM bradegler/base  
MAINTAINER Brad Egler <begler@gmail.com>  
  
RUN apt-get install -y mysql-server mysql-client pwgen  
  
RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/"
/etc/mysql/my.cnf  
  
RUN echo "[program:mysqld]" > /etc/supervisor/conf.d/mysql.conf  
RUN echo "command=/usr/sbin/mysqld --basedir=/usr --datadir=/var/lib/mysql
--plugin-dir=/usr/lib/mysql/plugin --user=root --log-
error=/var/log/mysql/error.log --pid-file=/var/run/mysqld/mysqld.pid
--socket=/var/run/mysqld/mysqld.sock --port=3306" >>
/etc/supervisor/conf.d/mysql.conf  
  
ADD run.sh /run.sh  
RUN chmod 755 /run.sh  
  
EXPOSE 3306  
CMD ["/run.sh"]

