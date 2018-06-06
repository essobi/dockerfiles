FROM guacamole/guacamole  
  
RUN apt update; apt upgrade -y  
RUN apt install -y build-essential libcairo2-dev libjpeg62-turbo-dev libpng-
dev libossp-uuid-dev libavcodec-dev libavutil-dev libswscale-dev libfreerdp-
dev libpango1.0-dev libssh2-1-dev libtelnet-dev libvncserver-dev libpulse-dev
libssl-dev libvorbis-dev libwebp-dev freerdp2-x11 ghostscript jq wget curl  
#RUN apt install -y mysql-server mysql-client mysql-common mysql-utilities  
COPY guacamole-server-0.9.13_amd64.deb /tmp/guacamole-server-0.9.13_amd64.deb  
RUN dpkg -i /tmp/guacamole-server-0.9.13_amd64.deb && \  
ldconfig  
  
RUN apt install -y apt-utils  
RUN { \  
echo debconf debconf/frontend select Noninteractive; \  
} | debconf-set-selections \  
&& apt-get install -y mysql-server mysql-client mysql-common mysql-utilities  
  
RUN cd /tmp && \  
SERVER=$(curl -s 'https://www.apache.org/dyn/closer.cgi?as_json=1' | jq --raw-
output '.preferred|rtrimstr("/")') && \  
wget $SERVER/incubator/guacamole/0.9.13-incubating/binary/guacamole-auth-
jdbc-0.9.13-incubating.tar.gz && \  
tar -xzf guacamole-auth-jdbc-0.9.13-incubating.tar.gz && \  
service mysql restart && \  
mysql -u root -e "create database guacamole_db" && \  
mysql -u root -e "create user 'guacamole_user'@'localhost' identified by
'guacamole_pass'" && \  
mysql -u root -e "GRANT SELECT,INSERT,UPDATE,DELETE ON guacamole_db.* TO
'guacamole_user'@'localhost'" && \  
mysql -u root -e "flush privileges" && \  
cat guacamole-auth-jdbc-0.9.13-incubating/mysql/schema/*.sql | mysql -u root
guacamole_db  
  
ENV GUACD_HOSTNAME 0.0.0.0  
ENV MYSQL_HOSTNAME localhost  
ENV MYSQL_DATABASE guacamole_db  
ENV MYSQL_USER guacamole_user  
ENV MYSQL_PASSWORD guacamole_pass  
  
COPY start.sh /opt/start.sh  
RUN chmod +x /opt/start.sh  
CMD ["/opt/start.sh"]  

