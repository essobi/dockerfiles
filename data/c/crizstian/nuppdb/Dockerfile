FROM debian:wheezy  
  
MAINTAINER <Cristian Ramirez Rosas, cristiano.rosetti@gmail.com>  
  
# Enviroment variables  
ENV MONGO_MAJOR 3.4  
ENV MONGO_VERSION 3.4.1  
ENV HOME=/home/nupp  
ENV PASS=nupp  
  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -r nupp && useradd -r -g nupp nupp  
  
# Installation:  
# Import MongoDB public GPG key AND create a MongoDB list file  
RUN set -ex apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys
42F3E95A2C4F08279C4960ADD68FA50FEA312927;  
  
RUN echo "deb http://repo.mongodb.org/apt/debian wheezy/mongodb-
org/$MONGO_MAJOR main" > /etc/apt/sources.list.d/mongodb-org.list  
  
# Update apt-get sources AND install MongoDB  
RUN set -x \  
&& apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y --force-yes \  
mongodb-org=$MONGO_VERSION \  
mongodb-org-server=$MONGO_VERSION \  
mongodb-org-shell=$MONGO_VERSION \  
mongodb-org-mongos=$MONGO_VERSION \  
mongodb-org-tools=$MONGO_VERSION \  
&& apt-get install -y sudo \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /var/lib/mongodb \  
&& mv /etc/mongod.conf /etc/mongod.conf.orig \  
&& apt-get clean && apt-get autoclean  
  
COPY service/mongod.service /lib/systemd/system/mongod.service  
  
RUN echo "nupp:${PASS}" | chpasswd \  
&& echo 'nupp ALL=(ALL:ALL) ALL' > /etc/sudoers \  
&& mkdir -p /data/db /data/logs /data/rs /data/keyfile /data/configdb
$HOME/nupp-database \  
&& touch $HOME/.mongorc.js \  
&& chown -R nupp:nupp /data/* $HOME/* \  
&& rm -rf /tmp/* /var/tmp/* \  
&& rm -rf /usr/share/doc  
  
WORKDIR $HOME/nupp-database  
  
EXPOSE 27017 27018 27019  
ENTRYPOINT ["/usr/bin/mongod"]  
  
USER nupp  

