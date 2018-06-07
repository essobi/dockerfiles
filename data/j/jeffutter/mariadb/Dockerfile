# MariaDB  
#  
# VERSION 0.0.1  
FROM ubuntu  
MAINTAINER Jeffery Utter "jeff@jeffutter.com"  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN locale-gen $LANG; echo "LANG=\"${LANG}\"" > /etc/default/locale; dpkg-
reconfigure locales  
  
# prevent apt from starting postgres right after the installation  
RUN echo "#!/bin/sh\nexit 101" > /usr/sbin/policy-rc.d; chmod +x
/usr/sbin/policy-rc.d  
  
RUN apt-get update  
  
RUN apt-get -y install software-properties-common  
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0xcbcb082a1bb943db  
RUN add-apt-repository 'deb http://mirror.jmu.edu/pub/mariadb/repo/10.0/ubuntu
trusty main'  
  
RUN apt-get update  
RUN apt-get -y install mariadb-server  
  
ADD mysql/my.cnf /etc/mysql/my.cnf  
RUN cp /etc/mysql/my.cnf /etc/mysql/my.cnf.orig ;\  
sed -i '/^bind-address*/ s/^/#/' /etc/mysql/my.cnf  
  
# allow autostart again  
RUN rm /usr/sbin/policy-rc.d  
  
EXPOSE 3306  
CMD ["/usr/bin/mysqld_safe"]  

