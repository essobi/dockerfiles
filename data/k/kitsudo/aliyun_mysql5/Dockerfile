FROM kitsudo/aliyun_centos6.6  
MAINTAINER Dave Luo <kitsudo163@163.com>  
RUN yum install -y \  
mysql-server \  
mysql  
  
# Install Forego  
ADD https://github.com/jwilder/forego/releases/download/v0.16.1/forego
/usr/local/bin/forego  
RUN chmod u+x /usr/local/bin/forego  
  
ADD run.sh /root/  
COPY my.cnf /etc/my.cnf  
  
VOLUME /var/lib/mysql  
EXPOSE 3306  
ENTRYPOINT ["/root/run.sh"]  

