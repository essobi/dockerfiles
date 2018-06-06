FROM debian  
MAINTAINER Chris MacPherson <chris@macpherson.scot>  
  
# This MySQL base image is based upon https://github.com/zanox/docker-mysql
and it's licence is found on the same page.  
# The purpose of the image is to provide a fast launch time which the stock
mysql or mysql/mysql-server images do not.  
# This increases the usability of the image for use in development and
continous integration stacks.  
# This image simply uses a newer version of MySQL - 5.7.  
# There is no data volume mounted so persisted data is not possible.  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -r mysql && useradd -r -g mysql mysql  
  
RUN rm -rf /var/lib/apt/lists/*  
  
# gpg: key 5072E1F5: public key "MySQL Release Engineering <mysql-
build@oss.oracle.com>" imported  
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys
A4A9406876FCBD3C456770C88C718D3B5072E1F5  
  
ENV MYSQL_MAJOR 5.7  
RUN echo "deb http://repo.mysql.com/apt/debian/ jessie mysql-${MYSQL_MAJOR}" >
/etc/apt/sources.list.d/mysql.list \  
&& echo "deb-src http://repo.mysql.com/apt/debian/ jessie
mysql-${MYSQL_MAJOR}" >> /etc/apt/sources.list.d/mysql.list  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install --assume-yes --no-install-
recommends mysql-community-server \  
&& apt-get download mysql-community-server && dpkg-deb -R mysql-community-
serve*.deb foo \  
&& cp foo/usr/bin/mysql_tzinfo_to_sql . && rm -r foo mysql-community-
serve*.deb \  
&& apt-get clean && rm -r /var/lib/apt/lists/*  
  
RUN mkdir -p /var/run/mysqld && chown mysql:mysql /var/run/mysqld \  
&& touch /var/log/mysql_general.log && chmod 666 /var/log/mysql_general.log  
  
COPY start-mysql stop-mysql /bin/  
  
RUN sed -Ei 's/^(bind-address|log)/#&/' /etc/mysql/my.cnf \  
&& echo 'skip-host-cache\nskip-name-resolve\npid-
file=/var/run/mysqld/mysqld.pid\nbind-address=0.0.0.0' | awk '{ print } $1 ==
"[mysqld]" \  
&& c == 0 { c = 1; system("cat") }' /etc/mysql/my.cnf > /tmp/my.cnf \  
&& mv /tmp/my.cnf /etc/mysql/my.cnf  
  
# Wrap your MySQL commands with start-mysql and stop-mysql  
# Anything inside will have access to MySQL server  
RUN start-mysql && \  
echo "UPDATE user SET host = '%' WHERE user = 'root';" | mysql mysql \  
&& ./mysql_tzinfo_to_sql /usr/share/zoneinfo | mysql mysql --force && \  
stop-mysql  
  
EXPOSE 3306  
CMD ["mysqld"]  

