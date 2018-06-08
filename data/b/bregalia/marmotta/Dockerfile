# Dockerfile for Apache Marmotta (584 branch)  
FROM debian:jessie-backports  
MAINTAINER Blake Regalia <blake.regalia@gmail.com>  
  
# Marmotta web server  
EXPOSE 8080  
# PostgreSQL database  
EXPOSE 5432  
# Marmotta source code  
WORKDIR /src  
COPY . /src  
  
# configuration  
ENV DB_NAME kiwi  
ENV DB_USER script  
ENV DB_PASS pass  
ENV POSTGRESQL_VERSION 10  
ENV POSTGIS_VERSION 2.4  
ENV WAR_PATH /src/launchers/marmotta-webapp/target/marmotta.war  
ENV CONF_PATH /var/lib/marmotta/system-config.properties  
  
# prepare the environment  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y \  
default-jdk \  
maven \  
tomcat7 \  
|| apt-get install -y -f  
  
# build  
RUN mvn clean install -DskipTests -DskipITs  
RUN test -e $WAR_PATH || exit  
  
# install and configure postgres from the PGDG repo  
RUN apt-get update && apt-get install -y locales apt-utils \  
&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8  
ENV LANG en_US.utf8  
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys
B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8  
RUN echo 'deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main' >
/etc/apt/sources.list.d/pgdg.list  
RUN apt-get update \  
&& apt-get install -y postgresql-common \  
&& sed -ri 's/#(create_main_cluster) .*$/\1 = false/' /etc/postgresql-
common/createcluster.conf \  
&& apt-get install -y \  
postgresql-$POSTGRESQL_VERSION \  
postgresql-$POSTGRESQL_VERSION-postgis-$POSTGIS_VERSION \  
postgresql-contrib-$POSTGRESQL_VERSION  
  
RUN pg_createcluster $POSTGRESQL_VERSION main --start  
USER postgres  
RUN service postgresql start \  
&& psql --command "CREATE USER $DB_USER WITH SUPERUSER LOGIN PASSWORD
'$DB_PASS';" \  
&& psql --command "CREATE DATABASE $DB_NAME WITH OWNER $DB_USER;" \  
&& psql $DB_NAME < ./libraries/kiwi/kiwi-
triplestore/src/main/resources/org/apache/marmotta/kiwi/persistence/pgsql/create_base_tables.sql
\  
&& psql $DB_NAME < ./aux/add-indexes.sql  
USER root  
RUN service postgresql stop  
  
# Adjust PostgreSQL configuration so that remote connections to the database
are possible.  
RUN echo "host all all 0.0.0.0/0 md5" >>
"/etc/postgresql/$POSTGRESQL_VERSION/main/pg_hba.conf"  
#RUN echo "host all all 127.0.0.1/32 md5" >>
/etc/postgresql/$POSTGRESQL_VERSION/main/pg_hba.conf  
# Also add `listen_addresses` to postgresql.conf  
RUN echo "listen_addresses='*'" >>
"/etc/postgresql/$POSTGRESQL_VERSION/main/postgresql.conf"  
  
# install the webapp  
#RUN dpkg --debug=2000 --install target/marmotta_*_all.deb <\-- we'd need to
fix the postinst  
RUN mkdir -p /usr/share/marmotta  
RUN cp $WAR_PATH /usr/share/marmotta/  
RUN chown tomcat7:tomcat7 /usr/share/marmotta/marmotta.war  
RUN cp /src/launchers/marmotta-webapp/src/deb/tomcat/marmotta.xml
/var/lib/tomcat7/conf/Catalina/localhost/  
RUN chown tomcat7:tomcat7
/var/lib/tomcat7/conf/Catalina/localhost/marmotta.xml  
RUN mkdir -p "$(dirname $CONF_PATH)"  
RUN echo "security.enabled = false" > $CONF_PATH  
RUN echo "database.type = postgres" >> $CONF_PATH  
RUN echo "database.url =
jdbc:postgresql://localhost:5432/$DB_NAME?prepareThreshold=3" >> $CONF_PATH  
RUN echo "database.user = $DB_USER" >> $CONF_PATH  
RUN echo "database.password = $DB_PASS" >> $CONF_PATH  
RUN echo "kiwi.setup.database = true" >> $CONF_PATH  
RUN chown -R tomcat7:tomcat7 "$(dirname $CONF_PATH)"  
  
# cleanup  
RUN mvn clean \  
&& rm -rf ~/.m2 \  
&& apt-get remove maven --purge -y \  
&& apt-get autoremove -y \  
&& apt-get clean -y \  
&& apt-get autoclean -y \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/*  
  
# entrypoint  
RUN cp /src/launchers/marmotta-webapp/src/docker/entrypoint.sh
/usr/local/bin/marmotta.sh  
ENTRYPOINT ["/usr/local/bin/marmotta.sh"]  

