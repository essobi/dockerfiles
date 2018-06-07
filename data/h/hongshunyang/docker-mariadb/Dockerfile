FROM hongshunyang/docker-alpine  
MAINTAINER Hongshun Yang <yanghongshun@outlook.com>  
  
RUN echo "@testing http://dl-4.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories  
  
RUN apk -U add \  
gosu@testing \  
mariadb \  
mariadb-client \  
pwgen \  
tzdata \  
&& rm -rf /var/cache/apk/*  
  
RUN mkdir -p /var/run/mysqld \  
&& chown mysql:mysql /var/run/mysqld \  
&& mkdir -p /var/log/mysql \  
&& chown mysql:mysql /var/log/mysql \  
&& mkdir -p /etc/mysql/conf.d \  
&& chown mysql:mysql /etc/mysql/conf.d \  
&& mkdir -p /var/lib/mysql \  
&& chown -R mysql:mysql /var/lib/mysql \  
&& rm /etc/mysql/my.cnf  
  
COPY rootfs/_usr_local_bin_docker-entrypoint.sh /usr/local/bin/docker-
entrypoint.sh  
RUN ln -s /usr/local/bin/docker-entrypoint.sh /  
RUN chmod a+x /usr/local/bin/docker-entrypoint.sh  
  
RUN mkdir /docker-entrypoint-initdb.d  
  
COPY tmpl/_etc_mysql_my.cnf.tmpl /etc/mysql/my.cnf  
#RUN dockerize -template "/etc/mysql/my.cnf.tmpl:/etc/mysql/my.cnf"  
VOLUME /var/lib/mysql  
EXPOSE 3306  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
# todo log  
#CMD ["mysqld"]  
## need add command:["mysqld"]  

