FROM java:8-jre  
  
MAINTAINER Jeremy PETIT "jeremy.petit@gmail.com"  
## ENV VARIABLES --------------------  
ENV COMMAFEED_VERSION 2.3.0  
ENV JAVA_OPTS -Xmx128m  
ENV DB_URL jdbc:postgresql://<postgres>:5432/commafeed  
ENV DB_TIMEOUT 60  
ENV DB_USER commafeed  
ENV DB_PASSWORD changeme  
ENV DOMAIN changeme  
ENV URI /rss  
ENV ADMIN_PASSWORD changeme  
ENV ADMIN_EMAIL changeme  
  
  
## VOLUMES --------------------------  
VOLUME ["/etc/commafeed", "/etc/nginx/conf.d", "/etc/postgres/init",
"/backups", "/var/log/commafeed"]  
WORKDIR /opt/commafeed  
  
# explicitly set user/group IDs  
RUN groupadd -r commafeed --gid=999 && useradd -r -g commafeed --uid=999
commafeed \  
&& mkdir -p /home/commafeed \  
&& chmod 700 /home/commafeed \  
&& chown commafeed:commafeed /home/commafeed  
  
# install gosu  
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends ca-certificates \  
&& rm -rf /var/lib/apt/lists/* \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture)" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& rm -rf /var/lib/apt/lists/*  
  
# install commafeed  
RUN mkdir -p /etc/commafeed /opt/commafeed/templates /backups
/var/log/commafeed /templates \  
&& curl -Lo /opt/commafeed/commafeed.jar
"https://github.com/Athou/commafeed/releases/download/${COMMAFEED_VERSION}/commafeed.jar"
\  
&& curl -Lo /opt/commafeed/templates/commafeed.yml.template
"https://raw.githubusercontent.com/Athou/commafeed/${COMMAFEED_VERSION}/config.yml.example"
\  
&& chmod 770 /opt/commafeed/commafeed.jar \  
&& chown -R commafeed:commafeed /opt/commafeed \  
&& touch /tmp/setAdminPass.remove  
  
COPY bin/* /usr/local/bin/  
COPY templates/* /templates/  
COPY docker-entrypoint.sh /  
RUN chmod 700 /docker-entrypoint.sh /usr/local/bin/backup  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["commafeed"]  

