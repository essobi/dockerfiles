FROM ubuntu:trusty  
  
RUN echo "deb http://us.archive.ubuntu.com/ubuntu/ trusty-updates main
restricted" >> /etc/apt/sources.list  
RUN echo "deb-src http://us.archive.ubuntu.com/ubuntu/ trusty-updates main
restricted" >> /etc/apt/sources.list  
RUN apt-get update  
  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
  
RUN apt-get install -y build-essential cmake curl ncurses-dev  
  
RUN mkdir /opts  
RUN cd /opts && curl -LO
http://dev.mysql.com/get/Downloads/MySQL-5.6/mysql-5.6.21.tar.gz  
RUN cd /opts && curl -LO http://q4m.kazuhooku.com/dist/q4m-0.9.14.tar.gz  
RUN cd /opts && tar zxf mysql-5.6.21.tar.gz  
RUN cd /opts && tar zxf q4m-0.9.14.tar.gz  
  
RUN mv /opts/q4m-0.9.14 /opts/mysql-5.6.21/storage/q4m  
RUN cd /opts/mysql-5.6.21 && cmake . -DCMAKE_INSTALL_PREFIX=/usr/local/q4m  
RUN cd /opts/mysql-5.6.21 && make  
RUN cd /opts/mysql-5.6.21 && make install  
  
RUN useradd mysql  
RUN gpasswd -a mysql mysql  
RUN chown -R mysql:mysql /usr/local/q4m  
  
RUN cd /usr/local/q4m && su -c './scripts/mysql_install_db --skip-name-
resolve' mysql  
RUN cd /usr/local/q4m && \  
./support-files/mysql.server start && \  
/usr/local/q4m/bin/mysql -u root < /opts/mysql-5.6.21/storage/q4m/support-
files/install.sql && \  
/usr/local/q4m/bin/mysql -u root -e 'GRANT ALL PRIVILEGES ON *.* TO root@"%"'
&& \  
/usr/local/q4m/bin/mysql -u root -e 'SHOW PLUGINS'  
  
EXPOSE 3306  
CMD ["/usr/local/q4m/bin/mysqld_safe"]  

