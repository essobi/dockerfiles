#  
# Percona Server Dockerfile  
#  
# http://www.percona.com/doc/percona-server/5.6/installation/apt_repo.html  
#  
# docker run -d --name mysql -v `pwd`:/var/lib/mysql -p 3306:3306 -e
MYSQL_DATABASE=testdb wangyuntao/percona  
# docker run -it --link mysql:db wangyuntao/percona /bin/bash  
#  
FROM wangyuntao/dev  
MAINTAINER wyt <wyt.daily@gmail.com>  
  
RUN \  
apt-key adv --keyserver keys.gnupg.net --recv-keys 1C4CBDCDCD2EFD2A && \  
echo "deb http://repo.percona.com/apt `lsb_release -cs` main" >
/etc/apt/sources.list.d/percona.list && \  
apt-get update && \  
apt-get install -y percona-server-server-5.6 percona-server-client-5.6 && \  
sed -ri 's/^(bind-address\s+=\s127.0.0.1)/# \1/' /etc/mysql/my.cnf  
  
VOLUME ["/var/lib/mysql"]  
EXPOSE 3306  
ENV DOCKER_DIR /docker  
COPY entrypoint.sh $DOCKER_DIR/  
RUN chmod +x $DOCKER_DIR/entrypoint.sh  
  
ENTRYPOINT ["/docker/entrypoint.sh"]  
CMD ["mysqld"]

