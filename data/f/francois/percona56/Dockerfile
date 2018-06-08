FROM ubuntu:14.04  
MAINTAINER Francois Billant <fbillant@gmail.com>  
  
EXPOSE 22 3306 4444 4567 4568  
RUN apt-get update && apt-get install -y build-essential openssh-server
supervisor  
RUN mkdir -p /var/run/sshd /var/log/supervisor  
  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# ssh configuration  
RUN echo 'root:root' | chpasswd  
RUN sed -i "s!PermitRootLogin without-password!PermitRootLogin yes!"
/etc/ssh/sshd_config  
  
# percona installation/configuration  
RUN apt-key adv --keyserver keys.gnupg.net --recv-keys 1C4CBDCDCD2EFD2A  
RUN echo "deb http://repo.percona.com/apt trusty main" >
/etc/apt/sources.list.d/percona.list &&\  
echo "deb-src http://repo.percona.com/apt trusty main" >>
/etc/apt/sources.list.d/percona.list  
  
RUN apt-get update && apt-get install -y percona-xtradb-cluster-56  
  
ADD my.cnf /etc/mysql/my.cnf  
  
CMD ["/usr/bin/supervisord"]  

