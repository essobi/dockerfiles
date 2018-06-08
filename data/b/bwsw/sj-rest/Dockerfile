FROM ubuntu:xenial  
  
MAINTAINER BITWORKS  
  
ENV version 1.0-SNAPSHOT  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install Oracle JDK 8  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" |
tee /etc/apt/sources.list.d/webupd8team-java.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" |
tee -a /etc/apt/sources.list.d/webupd8team-java.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys EEA14886 &&
\  
apt-get update && \  
echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true"
| debconf-set-selections && \  
apt-get install -y \--no-install-recommends apt-utils && \  
apt-get install -y \--no-install-recommends bc oracle-java8-installer && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN echo "deb http://dl.bintray.com/sbt/debian /" | tee -a
/etc/apt/sources.list.d/sbt.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv 642AC823 && \  
apt-get update && \  
apt-get install -y \--no-install-recommends nginx supervisor sbt && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Install npm and node.js  
RUN set -x && \  
apt-get update && \  
apt-get install -y curl bzip2 git make build-essential && \  
curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get update && \  
apt-get install -y ca-certificates nodejs && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# see .dockerignore in root dir  
COPY ./project /opt/bin/juggler/project  
COPY ./build.sbt /opt/bin/juggler/  
COPY ./core/sj-common /opt/bin/juggler/core/sj-common  
COPY ./core/sj-crud-rest /opt/bin/juggler/core/sj-crud-rest  
COPY ./core/sj-frontend /opt/bin/juggler/core/sj-frontend  
  
#Prepare UI  
RUN cd /opt/bin/juggler/core/sj-frontend && \  
npm cache clear && \  
npm install -g n && \  
npm install -g typings && \  
npm install --unsafe-perm && \  
npm run build && \  
# mkdir /var/www && \  
cp dist/. /var/www/ -R && \  
rm -rf /root/.npm *  
  
# Prepare Rest  
WORKDIR /opt/bin/juggler  
  
RUN mkdir -p /root/.sbt/0.13 && \  
echo 'scalacOptions ++= Seq("-Xmax-classfile-name","100")' >
/root/.sbt/0.13/global.sbt && \  
sbt sj-crud-rest/assembly && \  
mv core/sj-crud-rest/target/scala-2.12/sj-crud-rest-${version}.jar . && \  
sbt clean clean-files && \  
rm -rf /root/.ivy2/cache  
  
COPY ./docker/rest /opt/bin/juggler/docker/rest  
  
RUN ln -s /opt/bin/juggler/docker/rest/rest-supervisor.conf
/etc/supervisor/conf.d/ && \  
ln -s /opt/bin/juggler/docker/rest/rest-nginx.conf /etc/nginx/conf.d/ && \  
rm /etc/nginx/sites-available/default && \  
echo 'daemon off;' >> /etc/nginx/nginx.conf  
  
CMD ["/bin/bash", "/opt/bin/juggler/docker/rest/rest-run.sh"]  

