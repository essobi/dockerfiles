FROM centos:centos7  
  
MAINTAINER Muhammad Zeeshan Munir <mzmunirr@gmail.com>  
  
RUN yum install -y mariadb-server mariadb  
RUN mysql_install_db --user=mysql --ldata=/var/lib/mysql/  
  
RUN sed -i '/\\[mysqld\\]/aport=3306' /etc/my.cnf  
  
RUN \  
echo "/usr/bin/mysqld_safe --basedir=/usr &" > /tmp/config && \  
echo "cat /var/log/mariadb/mariadb.log" >> /tmp/config && \  
echo "mysqladmin --silent --wait=30 ping || exit 1" >> /tmp/config && \  
echo "mysql -e 'GRANT ALL PRIVILEGES ON *.* TO \"root\"@\"%\";'" >>
/tmp/config && \  
bash /tmp/config && \  
rm -f /tmp/config  
  
VOLUME ["/var/lib/mysql"]  
  
WORKDIR /data  
  
CMD ["/usr/bin/mysqld_safe"]  
  
EXPOSE 3306  

