FROM ubuntu:trusty  
MAINTAINER udzura "udzura@udzura.jp"  
RUN echo "#!/bin/sh\nexit 101" > /usr/sbin/policy-rc.d; chmod +x
/usr/sbin/policy-rc.d  
RUN apt-get update  
RUN apt-get -y install lsof  
  
RUN echo mysql-server-5.5 mysql-server/root_password password 'mysq1' |
debconf-set-selections  
RUN echo mysql-server-5.5 mysql-server/root_password_again password 'mysq1' |
debconf-set-selections  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-server-5.5  
  
ADD . /usr/local/bin  
RUN chmod a+x /usr/local/bin/start-mysql.sh  
  
RUN rm /usr/sbin/policy-rc.d  
  
RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/"
/etc/mysql/my.cnf  
  
# for debug  
VOLUME /var/log/mysql  
  
EXPOSE 3306  
CMD "/usr/local/bin/start-mysql.sh"

