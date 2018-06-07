FROM ubuntu:trusty  
MAINTAINER Jeffery Utter "jeff.utter@firespring.com"  
RUN bash -c "debconf-set-selections <<< 'mysql-server mysql-
server/root_password password super'"  
RUN bash -c "debconf-set-selections <<< 'mysql-server mysql-
server/root_password_again password super'"  
  
RUN apt-get update \  
&& apt-get install -y cpanminus build-essential supervisor libdbd-mysql-perl
sysstat mysql-server libmysqlclient-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir -p /etc/mysql/conf.d \  
&& { \  
echo '[mysqld]'; \  
echo 'skip-host-cache'; \  
echo 'skip-name-resolve'; \  
echo 'user = mysql'; \  
echo 'datadir = /var/lib/mysql'; \  
echo '!includedir /etc/mysql/conf.d/'; \  
} > /etc/mysql/my.cnf  
  
RUN mkdir -p /etc/mogilefs \  
&& mkdir -p /var/mogdata/  
  
RUN cpanm install --force MogileFS::Server \  
&& cpanm install DBD::mysql \  
&& cpanm install MogileFS::Utils  
  
RUN mysqld & \  
until [ `mysql -h127.0.0.1 -uroot -psuper -e 'select null limit 1' 2>/dev/null
>/dev/null; echo $?` -eq 0 ]; do sleep 1; done \  
&& mysql -uroot -psuper -e "GRANT ALL PRIVILEGES ON *.* TO 'root'@'%'
IDENTIFIED BY 'super';" \  
&& mogdbsetup --type=MySQL --yes --dbrootuser=root --dbrootpass=super
--dbname=mogilefs --dbuser=mogile --dbpassword=sekrit  
  
ADD mogilefsd.conf /etc/mogilefs/mogilefsd.conf  
ADD mogilefs.conf /root/.mogilefs.conf  
ADD run.sh /run.sh  
  
RUN adduser mogile --system --disabled-password \  
&& chown mogile -R /var/mogdata  
  
EXPOSE 7001  
ENTRYPOINT ["/run.sh"]  

