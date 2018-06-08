FROM ubuntu:17.10  
MAINTAINER Mike Halagan <mhalagan@nmdp.org>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ARG RELEASES="3310"  
COPY create_imgtdb.py opt/  
COPY requirements.txt opt/  
  
RUN apt-get update -q  
  
RUN apt-get install -qy wget curl build-essential cpp git \  
python3.6 python3-pip python3-dev \  
python3-setuptools uwsgi-plugin-python3 \  
python3.6-dev libxft-dev mysql-server \  
python-mysqldb python3-mysql.connector \  
&& curl https://bootstrap.pypa.io/get-pip.py | python3.6 \  
&& pip3 install --upgrade pip \  
&& pip3 install -r opt/requirements.txt  
  
RUN mkdir /var/run/mysqld \  
&& rm -rf /var/lib/mysql && mkdir -p /var/lib/mysql /var/run/mysqld \  
&& chown -R mysql:mysql /var/lib/mysql /var/run/mysqld \  
&& chmod 777 /var/run/mysqld \  
&& find /etc/mysql/ -name '*.cnf' -print0 \  
| xargs -0 grep -lZE '^(bind-address|log)' \  
| xargs -rt -0 sed -Ei 's/^(bind-address|log)/#&/' \  
&& echo '[mysqld]\nskip-host-cache\nskip-name-resolve' >
/etc/mysql/conf.d/docker.cnf  
  
VOLUME /var/lib/mysql  
  
COPY docker-entrypoint.sh /usr/local/bin/  
  
RUN /bin/bash -c "/usr/bin/mysqld_safe --skip-grant-tables &" \  
&& sleep 5 \  
&& mysql -u root -e "set @@global.show_compatibility_56=ON" \  
&& mysql -u root -e "CREATE DATABASE bioseqdb" \  
&& curl -OL
https://raw.githubusercontent.com/biosql/biosql/master/sql/biosqldb-mysql.sql
\  
&& mysql -u root bioseqdb < biosqldb-mysql.sql \  
&& python3.6 opt/create_imgtdb.py -v -r $RELEASES \  
&& mysqldump -p -u root -p bioseqdb > opt/biosqldb.sql \  
&& mysqladmin shutdown  
  
RUN ln -s usr/local/bin/docker-entrypoint.sh /entrypoint.sh \  
&& chmod a+rwx /usr/local/bin/docker-entrypoint.sh  
  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  
  
EXPOSE 3306  
EXPOSE 3307  
CMD ["mysqld"]

