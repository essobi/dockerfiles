FROM debian:wheezy  
MAINTAINER Stan <teftin@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-key adv --recv-keys --keyserver keyserver.ubuntu.com
0xcbcb082a1bb943db  
RUN echo 'deb http://ams2.mirrors.digitalocean.com/mariadb/repo/10.1/debian
wheezy main' > /etc/apt/sources.list.d/mariadb.list  
RUN apt-get update  
  
RUN apt-get install -y mariadb-server  
  
ADD run.sh /run.sh  
  
VOLUME /mysql  
  
EXPOSE 3306  
CMD exec bash /run.sh  

