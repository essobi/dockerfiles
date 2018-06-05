#  
# ddidier/pgadmin  
#  
# A Docker image for pgAdmin 3.  
#  
# docker build -t ddidier/pgadmin .  
FROM debian:jessie  
MAINTAINER David DIDIER  
  
ENV PGADMIN_VERSION=1.22.2-1.pgdg80+1  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends ca-certificates curl sudo wget \  
&& sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main"
> /etc/apt/sources.list.d/postgres.list' \  
&& wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-
key add - \  
&& apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y --no-install-recommends pgadmin3=$PGADMIN_VERSION
postgresql-client-9.6 xterm \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.10/gosu-$(dpkg --print-
architecture)" \  
&& curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/1.10/gosu-$(dpkg --print-
architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& apt-get autoremove -y \  
&& rm -rf /var/cache/* \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY files/usr/local/bin/docker-entrypoint /usr/local/bin/  
  
RUN chown root:root /usr/local/bin/docker-entrypoint \  
&& chmod 755 /usr/local/bin/docker-entrypoint  
  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint"]  

