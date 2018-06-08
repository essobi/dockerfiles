#  
# Mica Dockerfile  
#  
# https://github.com/obiba/docker-mica  
#  
# Pull base image  
FROM openjdk:8  
MAINTAINER OBiBa <dev@obiba.org>  
  
# grab gosu for easy step-down from root  
# see https://github.com/tianon/gosu/blob/master/INSTALL.md  
ENV GOSU_VERSION 1.10  
ENV GOSU_KEY B42F6819007F00F88E364FD4036A9C25BF357DD4  
RUN set -ex; \  
\  
fetchDeps=' \  
ca-certificates \  
wget \  
'; \  
apt-get update; \  
apt-get install -y --no-install-recommends $fetchDeps; \  
rm -rf /var/lib/apt/lists/*; \  
\  
dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')"; \  
wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch";
\  
wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc";
\  
\  
# verify the signature  
export GNUPGHOME="$(mktemp -d)"; \  
gpg --keyserver pgp.mit.edu --recv-keys "$GOSU_KEY" || \  
gpg --keyserver keyserver.pgp.com --recv-keys "$GOSU_KEY" || \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$GOSU_KEY"; \  
gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu; \  
rm -rf "$GNUPGHOME" /usr/local/bin/gosu.asc; \  
\  
chmod +x /usr/local/bin/gosu; \  
# verify that the binary works  
gosu nobody true;  
  
ENV LANG C.UTF-8  
ENV LANGUAGE C.UTF-8  
ENV LC_ALL C.UTF-8  
ENV MICA_ADMINISTRATOR_PASSWORD=password  
ENV MICA_ANONYMOUS_PASSWORD=password  
ENV MICA_HOME=/srv  
ENV JAVA_OPTS=-Xmx2G  
  
ENV MICA_VERSION 2.1  
# Install Mica Python Client  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y apt-transport-https unzip  
  
RUN \  
wget -q -O - https://pkg.obiba.org/obiba.org.key | apt-key add - && \  
echo 'deb https://pkg.obiba.org unstable/' | tee
/etc/apt/sources.list.d/obiba.list && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y mica-python-client  
  
# Install Mica Server  
RUN set -x && \  
cd /usr/share/ && \  
wget -q -O mica2.zip
https://ci.obiba.org/view/Mica/job/Mica2-${MICA_VERSION}.x/ws/mica-
dist/target/mica-dist-${MICA_VERSION}-SNAPSHOT-dist.zip && \  
unzip -q mica2.zip && \  
rm mica2.zip && \  
mv mica-dist-${MICA_VERSION}-SNAPSHOT mica2  
  
RUN chmod +x /usr/share/mica2/bin/mica2  
  
COPY ./bin /opt/mica/bin  
  
RUN chmod +x -R /opt/mica/bin  
RUN adduser --system --home $MICA_HOME \--no-create-home --disabled-password
mica  
RUN chown -R mica /opt/mica  
  
VOLUME /srv  
  
# http and https  
EXPOSE 8082 8445  
# Define default command.  
COPY ./docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["app"]  

