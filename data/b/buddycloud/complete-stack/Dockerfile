# This Dockerfile sets up the Buddycloud stack from the database layer  
# all the way up to the webserver, API and user-facing webclient  
FROM ubuntu:14.04  
RUN apt-get update  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV LOG_DIR /var/log/buddycloud  
  
# we try to log everything into one directory  
RUN mkdir -p $LOG_DIR  
  
# Setup Database-layer  
RUN apt-get -y -q install --no-install-recommends postgresql-9.3 postgresql-
client-9.3 postgresql-contrib-9.3  
# Run the rest of the commands as the ``postgres`` user created by the
``postgres-9.3`` package when it was ``apt-get installed``  
USER postgres  
# Create a PostgreSQL role named ``docker`` with ``docker`` as the password
and  
# then create a database `docker` owned by the ``docker`` role.  
# Note: here we use ``&&\\`` to run commands one after the other - the ``\\``  
# allows the RUN command to span multiple lines.  
RUN /etc/init.d/postgresql start && psql --command "CREATE USER docker WITH
SUPERUSER PASSWORD 'docker';" &&\  
createdb -O docker docker  
# Adjust PostgreSQL configuration so that remote connections to the  
# database are possible.  
RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.3/main/pg_hba.conf  
# And add ``listen_addresses`` to ``/etc/postgresql/9.3/main/postgresql.conf``  
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf  
# Switch back to root  
USER root  
  
# Setup bind  
RUN apt-get install -y --no-install-recommends bind9  
ADD config/buddycloud-bind-zone-conf.local /tmp/buddycloud-bind-zone-
conf.local  
RUN cat /tmp/buddycloud-bind-zone-conf.local >> /etc/bind/named.conf.local  
ADD config/buddycloud-bind-zone.conf /etc/bind/db.buddycloud.dev  
  
# Setup XMPP-layer  
RUN apt-get install -y --no-install-recommends prosody lua-zlib lua-cyrussasl
lua-sec  
ADD config/prosody.cfg.lua /etc/prosody/prosody.cfg.lua  
RUN mkdir -p $LOG_DIR/prosody  
RUN chown -R prosody $LOG_DIR/prosody  
  
# Setup buddycloud-layer  
RUN apt-get install -y --no-install-recommends openjdk-7-jre-headless
dbconfig-common  
ADD http://downloads.buddycloud.com/packages/debian/nightly/buddycloud-server-
java/buddycloud-server-java_latest.deb /tmp/buddycloud-server.deb  
# ensure database is ready  
ADD config/buddycloud-server-java.dbconfig.conf /etc/dbconfig-
common/buddycloud-server-java.conf  
# install debian package  
RUN /etc/init.d/postgresql start && dpkg -i /tmp/buddycloud-server.deb  
# update configuration files  
ADD config/buddycloud-server-java-configuration.properties
/usr/share/buddycloud-server-java/configuration.properties  
ADD config/buddycloud-server-java-log4j.properties /usr/share/buddycloud-
server-java/log4j.properties  
  
# Setup buddycloud-media-server  
ADD http://downloads.buddycloud.com/packages/debian/nightly/buddycloud-media-
server/buddycloud-media-server_latest.deb /tmp/buddycloud-media-server.deb  
# ensure database is ready  
ADD config/buddycloud-media-server.dbconfig.conf /etc/dbconfig-
common/buddycloud-media-server.conf  
# install debian package  
RUN /etc/init.d/postgresql start && dpkg -i /tmp/buddycloud-media-server.deb  
# update configuration files  
ADD config/buddycloud-media-server-configuration.properties
/usr/share/buddycloud-media-server/mediaserver.properties  
ADD config/buddycloud-media-server-log4j.xml /usr/share/buddycloud-server-
java/logback.xml  
# create media server XMPP client account  
ADD bin/buddycloud-media-server-create-user.sh /tmp/buddycloud-media-server-
create-user.sh  
RUN /etc/init.d/prosody start && /bin/bash /tmp/buddycloud-media-server-
create-user.sh  
# create storage dir and give proper permissions  
RUN mkdir -p /var/lib/buddycloud-media-server; chown -R buddycloud:buddycloud
/var/lib/buddycloud-media-server  
  
# Setup http-api  
RUN apt-get install -y --no-install-recommends nodejs  
ADD http://downloads.buddycloud.com/packages/debian/nightly/buddycloud-http-
api/buddycloud-http-api_latest.deb /tmp/http-api.deb  
RUN dpkg -i /tmp/http-api.deb  
ADD config/buddycloud-http-api-config.js /usr/share/buddycloud-http-
api/config.js  
  
# Setup and configure nginx  
RUN apt-get install -y --no-install-recommends nginx  
RUN rm /etc/nginx/sites-enabled/default  
ADD config/nginx.conf /etc/nginx/nginx.conf  
# these are keys for buddycloud.dev. Prosody will also use them.  
RUN mkdir -p /etc/certs/  
ADD config/buddycloud.dev.cert.pem /etc/certs/  
ADD config/buddycloud.dev.key.pem /etc/certs/  
  
# Setup Buddycloud Webclient  
ADD
http://downloads.buddycloud.com/packages/debian/nightly/webclient/webclient_latest.deb
/tmp/webclient.deb  
RUN dpkg -i /tmp/webclient.deb  
ADD config/buddycloud-webclient-config.js /usr/share/buddycloud-
webclient/config.js  
ADD config/buddycloud-nginx-server-block /etc/nginx/sites-
available/buddycloud.dev  
  
# Configure nginx server block  
RUN ln -s /etc/nginx/sites-available/buddycloud.dev /etc/nginx/sites-enabled/  
  
# Define persistent volumes  
RUN apt-get install -y --no-install-recommends rsync  
ADD bin/restore-volumes.sh /tmp/restore-volumes.sh  
ADD bin/backup-volumes.sh /tmp/backup-volumes.sh  
RUN /bin/bash /tmp/backup-volumes.sh  
  
EXPOSE 80 443 5222 5269  
ENTRYPOINT /bin/bash /tmp/restore-volumes.sh && \  
mkdir -p $LOG_DIR/prosody && chown -R prosody $LOG_DIR/prosody && \  
mkdir -p $LOG_DIR/buddycloud-server-java && chown -R buddycloud
$LOG_DIR/buddycloud-server-java && \  
mkdir -p $LOG_DIR/buddycloud-http-api && chown -R buddycloud
$LOG_DIR/buddycloud-http-api && \  
mkdir -p $LOG_DIR/buddycloud-media-server && chown -R buddycloud
$LOG_DIR/buddycloud-media-server && \  
service bind9 start && service postgresql start && service prosody start && \  
/etc/init.d/buddycloud-server-java start && /etc/init.d/buddycloud-media-
server start && \  
service nginx restart && /etc/init.d/buddycloud-http-api start; /bin/bash  

