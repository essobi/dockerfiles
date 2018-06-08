FROM ubuntu:12.04  
MAINTAINER Steve Mayne <steve.mayne@gmail.com>  
  
RUN apt-get update && apt-get install -q -y \  
bison \  
build-essential \  
checkinstall \  
libncurses5-dev  
  
ADD mysql-4.1.25.tar.gz /usr/local/src  
COPY buildmysql4.sh /tmp/buildmysql4.sh  
RUN chmod +x /tmp/buildmysql4.sh  
RUN /tmp/buildmysql4.sh  
  
FROM ubuntu:12.04  
ENV PATH /usr/local/mysql/bin:$PATH  
ENV MYSQLDATA /usr/local/mysql/var  
VOLUME /usr/local/mysql/var  
  
COPY \--from=0 /usr/local/src/mysql-4.1.25/mysql_4.1.25-1_amd64.deb
/tmp/mysql_4.1.25-1_amd64.deb  
RUN dpkg -i /tmp/mysql_4.1.25-1_amd64.deb && rm /tmp/mysql_4.1.25-1_amd64.deb  
COPY my.cnf /etc/my.cnf  
RUN groupadd -r mysql && useradd -r -g mysql mysql  
RUN chown -R root /usr/local/mysql && chown -R mysql /usr/local/mysql/var &&
chgrp -R mysql /usr/local/mysql  
  
COPY docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
  
EXPOSE 3306  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["mysqld_safe"]  

