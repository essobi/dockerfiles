FROM ubuntu:14.04.2  
MAINTAINER touchps <puneet.mir@gmail.com>  
  
  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -r mongodb && useradd -r -g mongodb mongodb  
  
# NUMA Configure  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
ca-certificates curl \  
numactl \  
&& rm -rf /var/lib/apt/lists/*  
  
# gosu download  
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4  
RUN curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.4/gosu-$(dpkg --print-
architecture)" \  
&& curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/1.4/gosu-$(dpkg --print-
architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu  
  
# Installation:  
# Import MongoDB public GPG key AND create a MongoDB list file  
ENV MONGO_MAJOR 3.0  
ENV MONGO_VERSION 3.0.5  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10  
RUN echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-
org/$MONGO_MAJOR multiverse" | tee /etc/apt/sources.list.d/mongodb-
org-"$MONGO_MAJOR".list  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y \  
mongodb-org=$MONGO_VERSION \  
mongodb-org-server=$MONGO_VERSION \  
mongodb-org-shell=$MONGO_VERSION \  
mongodb-org-mongos=$MONGO_VERSION \  
mongodb-org-tools=$MONGO_VERSION  
  
# Create the MongoDB data directory  
RUN mkdir -p /data/db && chown -R mongodb:mongodb /data/db  
VOLUME /data/db  
  
COPY docker-entrypoint.sh /entrypoint.sh  
# RUN chown mongodb:mongodb /entrypoint.sh  
RUN chmod ug+x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
# Expose port 27017 from the container to the host  
EXPOSE 27017  
# Set usr/bin/mongod as the dockerized entry-point application  
# ENTRYPOINT ["/entrypoint.sh"]  
CMD ["mongod"]  

