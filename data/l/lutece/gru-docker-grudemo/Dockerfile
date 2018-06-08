FROM debian:jessie  
  
# install needed apps  
RUN echo 'mysql-server mysql-server/root_password password motdepasse' |
debconf-set-selections && \  
echo 'mysql-server mysql-server/root_password_again password motdepasse' |
debconf-set-selections && \  
apt-get update && apt-get dist-upgrade -y && \  
apt-get install -y binutils curl locales unzip mysql-server-5.5 mysql-
client-5.5 tomcat7 --no-install-recommends && \  
curl -sL https://dev.lutece.paris.fr/war/gru.war > /tmp/gru.war && \  
localedef -c -i fr_FR -f UTF-8 fr_FR.UTF-8 && \  
rm -Rf /var/lib/apt/lists/*  
  
# COPY files to container  
COPY dump.sql /tmp/  
COPY docker-entrypoint.sh /  
  
# configure apps and load data...  
RUN chmod +x /docker-entrypoint.sh && \  
echo "[client]" > /root/.my.cnf && \  
echo "host = localhost" >> /root/.my.cnf && \  
echo "user = root" >> /root/.my.cnf && \  
echo "password = motdepasse" >> /root/.my.cnf && \  
sed -i'' -e 's/port="8080/port="80/g' /etc/tomcat7/server.xml && \  
unzip /tmp/gru.war -d /var/lib/tomcat7/webapps/gru/  
  
VOLUME ["/var/lib/mysql","/var/lib/tomcat7/webapps/gru/WEB-INF/logs/"]  
EXPOSE 3306 80  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

