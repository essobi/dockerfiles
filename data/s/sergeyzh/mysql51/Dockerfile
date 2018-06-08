FROM sergeyzh/centos6-epel  
  
MAINTAINER Sergey Zhukov, sergey@jetbrains.com  
  
ENV MYSQL_VER mysql-5.1.73-linux-x86_64-glibc23  
  
RUN wget http://dev.mysql.com/get/Downloads/MySQL-5.1/${MYSQL_VER}.tar.gz ;
tar -xzf ${MYSQL_VER}.tar.gz ; \  
mv ${MYSQL_VER} mysql ; rm ${MYSQL_VER}.tar.gz  
  
VOLUME "/mnt/mysql"  
  
ENV MYSQL_DATA /mnt/mysql/data  
ENV MYSQL_BASE /mysql  
  
RUN sed -i "s|^basedir=|basedir=${MYSQL_BASE}|g" /mysql/support-
files/mysql.server  
RUN sed -i "s|^datadir=|datadir=${MYSQL_DATA}|g" /mysql/support-
files/mysql.server  
RUN /usr/sbin/useradd mysql ; mkdir /mnt/mysql ; chown -R mysql.mysql /mysql
/mnt/mysql  
  
# RUN su - mysql "-c cd /mysql ; scripts/mysql_install_db"  
ENV PATH $PATH:/mysql/bin  
  
ADD entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
ADD run-services.sh /  
RUN chmod +x /run-services.sh  
  
CMD /run-services.sh  
  
EXPOSE 3306  

