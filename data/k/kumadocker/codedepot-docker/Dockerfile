FROM alpine:3.6  
LABEL Name=codedepot Version=0.0.1  
RUN set -x && \  
apk add \--no-cache \  
bash curl sudo \  
postgresql python2 openjdk8 apache2 apache2-proxy openssh git maven && \  
mkdir /usr/local/tmp000 && \  
cd /usr/local/tmp000 && \  
curl
http://ftp.kddilabs.jp/infosystems/apache/tomcat/tomcat-8/v8.5.29/bin/apache-
tomcat-8.5.29.tar.gz | \  
tar -xzv -f - -C /usr/local/tmp000 && \  
mv /usr/local/tmp000/* /usr/local/tomcat && \  
rmdir /usr/local/tmp000 && \  
echo '<Location /codedepot/>' > /etc/apache2/conf.d/codedepot.conf && \  
echo ' ProxyPass ajp://127.0.0.1:8009/codedepot/' >>
/etc/apache2/conf.d/codedepot.conf && \  
echo '</Location>' >> /etc/apache2/conf.d/codedepot.conf && \  
sed -i.orig -e '/^LoadModule lbmethod_heartbeat_module/s/^/#/' -e
'/^LoadModule proxy_balancer_module/s/^/#/' /etc/apache2/conf.d/proxy.conf &&
\  
mkdir /run/apache2 /run/postgresql && \  
chown postgres.postgres /run/postgresql && \  
echo done.  
  
RUN set -x && \  
cd /usr/local && \  
git clone https://github.com/CodedepotOSS/CodeDepot.git codedepot && \  
cd codedepot && \  
sed -e '/^DATA_ROOT\s*=/s@=.*@=/data@' \  
-e "/^DBUSER\s*=/s/=.*/= ${DBUSER:-codedepot_user}/" \  
-e "/^DBPASS\s*=/s/=.*/= ${DBPASS:-codedepot_pass}/" \  
< build.properties.default > build.properties && \  
cat build.properties && \  
mkdir /data && \  
mvn package && \  
echo done.  
  
RUN set -x && \  
cd /usr/local/codedepot && \  
cp ./target/codedepot.war /usr/local/tomcat/webapps/ && \  
echo 'HACK CodeDepot/bin/initdb.sh...' && \  
sed -i.orig -e "s/-W/-w/" ./bin/initdb.sh && \  
echo done.  
  
RUN set -x && \  
echo 'echo "=== start === `date`"' > /startup.sh && \  
echo 'cd /usr/local/codedepot' >> /startup.sh && \  
echo 'if [ ! -f /pgdata/pg_hba.conf ]; then' >> /startup.sh && \  
echo ' echo "=== initalize PostgresSQL data dir ==="' >> /startup.sh && \  
echo ' mkdir -p /pgdata' >> /startup.sh && \  
echo ' chown -R postgres.postgres /pgdata' >> /startup.sh && \  
echo ' sudo -u postgres initdb \--no-locale /pgdata' >> /startup.sh && \  
echo ' echo "local codedepot_db '${DBUSER:-codedepot_user}' md5" >>
/pgdata/pg_hba.conf' >> /startup.sh && \  
echo ' echo "host codedepot_db '${DBUSER:-codedepot_user}' 127.0.0.1/32 md5"
>> /pgdata/pg_hba.conf' >> /startup.sh && \  
echo ' echo "host codedepot_db '${DBUSER:-codedepot_user}' ::1/128 md5" >>
/pgdata/pg_hba.conf' >> /startup.sh && \  
echo 'fi' >> /startup.sh && \  
echo 'sudo -u postgres /usr/bin/pg_ctl start -D /pgdata -l
/var/log/postgresql/pgdata.log' >> /startup.sh && \  
echo '/usr/sbin/httpd -k start' >> /startup.sh && \  
echo '/usr/local/tomcat/bin/startup.sh' >> /startup.sh && \  
echo './bin/setup.sh' >> /startup.sh && \  
echo 'if [ ! -f initdb.done ]; then' >> /startup.sh && \  
echo ' echo "=== initdb ==="' >> /startup.sh && \  
echo ' sudo -u postgres ./bin/initdb.sh && touch initdb.done' >> /startup.sh
&& \  
echo 'fi' >> /startup.sh && \  
echo 'tail -f /var/log/postgresql/pgdata.log
/usr/local/tomcat/logs/catalina.out /var/log/apache2/error.log' >> /startup.sh
&& \  
chmod a+x /startup.sh && \  
echo done.  
VOLUME [ "/pgdata", "/data" ]  
EXPOSE 80  
WORKDIR /usr/local/codedepot  
CMD /startup.sh  

