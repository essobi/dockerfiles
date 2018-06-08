FROM ubuntu:12.04  
MAINTAINER Hans Donner <hans.donner@pobox.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# everything up to date  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list && \  
apt-get update && \  
apt-get upgrade -y  
  
# install system components  
RUN apt-get -y install python-software-properties  
  
# install mariadb  
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0xcbcb082a1bb943db && \  
add-apt-repository 'deb http://mirror.jmu.edu/pub/mariadb/repo/5.5/ubuntu
precise main' && \  
apt-get update && \  
apt-get install -y mariadb-server  
  
# replace default config  
RUN mv /etc/mysql/my.cnf /etc/mysql/my.cnf.org  
ADD mariadb.cnf /etc/mysql/my.cnf  
  
# add scripts and install dependencies  
RUN mkdir /docker  
ADD scripts /docker/scripts  
RUN chmod +x /docker/scripts/*  
RUN apt-get install -y netcat-openbsd  
  
# extra config on volume  
RUN rm -rf /etc/mysql/conf.d  
VOLUME /etc/mysql/conf.d  
  
# data on volume  
VOLUME /var/lib/mysql  
  
# expose ports  
EXPOSE 3306  
# entrypoint  
ENTRYPOINT ["/docker/scripts/start"]  

