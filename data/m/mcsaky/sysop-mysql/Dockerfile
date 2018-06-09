# Use phusion/baseimage as base image. To make your builds  
# reproducible, make sure you lock down to a specific version, not  
# to `latest`! See  
# https://github.com/phusion/baseimage-docker/blob/master/Changelog.md  
# for a list of version numbers.  
FROM phusion/baseimage:0.9.18  
MAINTAINER "Mihai Csaky" <mihai.csaky@sysop-consulting.ro>  
  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# ...put your own build instructions here...  
ENV MYSQL_SERVER mysql-server-5.6  
ENV DEBIAN_FRONTEND="noninteractive"  
RUN rm -f /etc/service/sshd/down  
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
ADD authorized_keys /tmp/authorized_keys  
RUN cat /tmp/authorized_keys > /root/.ssh/authorized_keys && rm -f
/tmp/authorized_keys  
  
RUN groupadd -r mysql && useradd -r -g mysql mysql  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install -y perl pwgen --no-install-recommends  
  
RUN apt-get install -y ${MYSQL_SERVER} \  
&& rm -rf /var/lib/mysql && mkdir -p /var/lib/mysql  
  
RUN sed -Ei 's/^(bind-address|log)/#&/' /etc/mysql/my.cnf \  
&& echo 'skip-host-cache\nskip-name-resolve' | awk '{ print } $1 == "[mysqld]"
&& c == 0 { c = 1; system("cat") }' /etc/mysql/my.cnf > /tmp/my.cnf \  
&& mv /tmp/my.cnf /etc/mysql/my.cnf  
  
ENV DATADIR /var/lib/mysql  
VOLUME /var/lib/mysql  
EXPOSE 3306  
RUN mkdir /etc/service/mysqld/  
ADD mysqld.sh /etc/service/mysqld/run  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

