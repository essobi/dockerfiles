FROM debian:jessie  
MAINTAINER kakilangit <theguywhodrinkscoffeeandcodes@gmail.com>  
  
# https://downloads.mariadb.org/  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM dumb  
  
RUN groupadd -r mysql && useradd -r -g mysql mysql \  
&& printf "deb http://mariadb.biz.net.id/repo/10.2/ubuntu trusty main" >>
/etc/apt/sources.list \  
&& apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0xcbcb082a1bb943db \  
&& apt-get update && apt-get install -y \  
mariadb-server \  
mariadb-plugin-oqgraph \  
pwgen \  
&& apt-get autoremove -y \  
&& apt-get autoclean \  
&& apt-get clean \  
&& rm -rf /var/lib/mysql/* /var/lib/apt/lists/*  
  
COPY config/my.cnf /etc/mysql/my.cnf  
COPY config/create_mariadb_admin_user.sh /create_mariadb_admin_user.sh  
COPY config/run.sh /run.sh  
RUN chmod 775 /*.sh  
  
VOLUME ["/etc/mysql", "/var/lib/mysql"]  
  
EXPOSE 3306  
CMD ["/run.sh"]  

