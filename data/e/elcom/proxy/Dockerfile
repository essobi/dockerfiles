FROM debian:stretch  
MAINTAINER LWB  
  
ENV REPOSITORY=GIT  
ENV BRANCH=master  
ENV DOCKER_GEN_VERSION=0.7.3  
ENV DOCKER_HOST=unix:///tmp/docker.sock  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes --no-install-
recommends \  
krb5-user krb5-config \  
apache2 libapache2-mod-auth-kerb \  
wget ca-certificates \  
git && \  
rm -rf /var/lib/apt/lists  
  
RUN a2enmod headers auth_kerb rewrite proxy proxy_http  
  
RUN wget https://github.com/jwilder/docker-
gen/releases/download/$DOCKER_GEN_VERSION/docker-gen-linux-
amd64-$DOCKER_GEN_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xvzf docker-gen-linux-
amd64-$DOCKER_GEN_VERSION.tar.gz \  
&& rm /docker-gen-linux-amd64-$DOCKER_GEN_VERSION.tar.gz  
  
COPY docker-entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
COPY docker-start.sh /start.sh  
RUN chmod +x /start.sh  
  
EXPOSE 80  
CMD /usr/sbin/apache2ctl -D FOREGROUND  
CMD /start.sh  

