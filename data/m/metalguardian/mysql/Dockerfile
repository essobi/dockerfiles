FROM ubuntu:14.04.3  
MAINTAINER Ivan Pushkin <imetalguardi+docker@gmail.com>  
  
RUN groupadd -r mysql && useradd -r -g mysql mysql  
  
RUN mkdir /docker-entrypoint-initdb.d  
  
ENV TERM xterm  
ENV MYSQL_MAJOR 5.7  
ENV MYSQL_VERSION 5.7.*  
  
# add mysql repository  
RUN apt-key adv --keyserver pool.sks-keyservers.net --recv-keys
A4A9406876FCBD3C456770C88C718D3B5072E1F5  
RUN echo "deb http://repo.mysql.com/apt/ubuntu/ $(lsb_release -cs)
mysql-${MYSQL_MAJOR}" > /etc/apt/sources.list.d/mysql.list  
  
# update  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y -q --no-install-recommends
install \  
mysql-server=${MYSQL_VERSION} \  
mysql-client=${MYSQL_VERSION}  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN rm -rf /var/lib/mysql && mkdir -p /var/lib/mysql  
  
RUN sed -Ei 's/^(bind-address|log)/#&/' /etc/mysql/my.cnf \  
&& echo 'skip-host-cache\nskip-name-resolve' | awk '{ print } $1 == "[mysqld]"
&& c == 0 { c = 1; system("cat") }' /etc/mysql/my.cnf > /tmp/my.cnf \  
&& mv /tmp/my.cnf /etc/mysql/my.cnf  
  
VOLUME ["/var/lib/mysql"]  
  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 3306  
CMD ["mysqld"]  

