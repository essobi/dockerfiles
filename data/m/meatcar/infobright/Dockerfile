# Infobright Community Edition (ICE) Docker Container  
# Infobright is a MySQL Database Engine. See http://www.infobright.org/ for
more details.  
# Based on https://registry.hub.docker.com/_/mysql/  
#  
# Usage: docker run -e MYSQL_ROOT_PASSWORD=mysecretpassword -d mysql  
FROM ubuntu:14.04  
MAINTAINER Denys Pavlov <denys.pavlov@gmail.com>  
  
  
# https://github.com/dotcloud/docker/issues/1024  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -sf /bin/true /sbin/initctl  
  
RUN apt-get -qq update  
RUN apt-get -qqy install wget screen  
RUN cd /tmp; wget -nv -q
http://www.infobright.org/downloads/ice/infobright-4.0.7-0-x86_64-ice.deb  
RUN dpkg -i /tmp/infobright-4.0.7-0-x86_64-ice.deb >/dev/null  
  
RUN cd /usr/local/infobright/; ./postconfig.sh >/dev/null  
  
ENV PATH $PATH:/usr/local/infobright/bin:/usr/local/infobright/scripts  
ENV MYSQL_DATADIR /mnt/mysql_data  
  
WORKDIR /usr/local/infobright  
VOLUME /mnt/mysql_data  
  
# Accept connections from outside container  
RUN sed -i -e
"s;^\\(.*\\)/usr/local/infobright-.*/data\\(.*\\)$;\1$MYSQL_DATADIR\2;"
/etc/my-ib.cnf  
RUN sed -i -e "s/\\(\\#skip-networking\\)/\1\nbind-address=0.0.0.0\nskip-name-
resolve/" /etc/my-ib.cnf  
  
ADD docker-entrypoint.sh /entrypoint.sh  
EXPOSE 5029  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["mysqld_safe"]  

