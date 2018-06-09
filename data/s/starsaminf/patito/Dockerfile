FROM debian:jessie-slim  
COPY ./docker-entrypoint.sh /usr/local/bin/  
  
RUN set -ex \  
&& apt-get update \  
&& apt-get install -y make flex g++ libmysqlclient-dev libmysql++-dev php5-fpm
php5-mysql php5-gd nginx \  
# mysql  
&& echo 'mysql-server-5.5 mysql-server/root_password password ""' | debconf-
set-selections \  
&& echo 'mysql-server-5.5 mysql-server/root_password_again password ""'
|debconf-set-selections \  
#&& apt-get update  
&& apt-get install -y mysql-server \  
# code  
&& /usr/sbin/useradd -m -u 1536 judge \  
# clear  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/* \  
#  
&& USER=`cat /etc/mysql/debian.cnf |grep user|head -1|awk '{print $3}'` \  
&& PASSWORD=`cat /etc/mysql/debian.cnf |grep password|head -1|awk '{print
$3}'` \  
&& CPU=`grep "cpu cores" /proc/cpuinfo |head -1|awk '{print $4}'` \  
&& sed -i "s/post_max_size = 8M/post_max_size = 80M/g" /etc/php5/fpm/php.ini \  
&& sed -i "s/upload_max_filesize = 2M/upload_max_filesize = 80M/g"
/etc/php5/fpm/php.ini \  
# db  
&& chown -R mysql:mysql /var/lib/mysql \  
&& service mysql restart \  
&& service mysql status \  
&& echo $USER > /home/judge/password.txt \  
&& echo $PASSWORD >> /home/judge/password.txt \  
#&& mysql -h localhost -u$USER -p$PASSWORD< /home/judge/src/install/db.sql \  
#&& echo "insert into jol.privilege
values('admin','administrator','N');"|mysql -h localhost -u$USER -p$PASSWORD \  
#&& service mysql stop \  
&& chmod +x /usr/local/bin/docker-entrypoint.sh \  
&& ln -s /usr/local/bin/docker-entrypoint.sh /docker-entrypoint.sh  
  
COPY nginx/default.conf /etc/nginx/sites-available/default  
  
WORKDIR /home/judge/  
EXPOSE 80  
VOLUME ["/home/judge/"]  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
#CMD judged /home/judge debug && tail -f /dev/null  

