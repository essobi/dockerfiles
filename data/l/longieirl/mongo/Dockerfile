#  
# MongoDB Dockerfile  
#  
# Note: http://docs.mongodb.org/ecosystem/platforms/amazon-ec2/  
#  
# Base image  
FROM longieirl/base  
  
MAINTAINER jlongieirl@gmail.com  
  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -r mongodb && useradd -r -g mongodb mongodb  
  
# grab gosu for easy step-down from root  
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4  
RUN curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture)" \  
&& curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu  
  
ENV MONGO_RELEASE_FINGERPRINT DFFA3DCF326E302C4787673A01C4E7FAAAB2461C  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys
$MONGO_RELEASE_FINGERPRINT  
ENV MONGO_VERSION 2.6.7  
# Install MongoDB  
RUN curl -SL "https://fastdl.mongodb.org/linux/mongodb-
linux-x86_64-$MONGO_VERSION.tgz" -o mongo.tgz \  
&& curl -SL "https://fastdl.mongodb.org/linux/mongodb-
linux-x86_64-$MONGO_VERSION.tgz.sig" -o mongo.tgz.sig \  
&& gpg --verify mongo.tgz.sig \  
&& tar -xvf mongo.tgz -C /usr/local \--strip-components=1 \  
&& rm mongo.tgz*  
  
# Expose ports.  
# - 27017: process  
# - 28017: http  
EXPOSE 27017  
EXPOSE 28017  
# Create required directories  
RUN mkdir -p /scripts /data /data/db /data/arb /log /log/mongodb /journal  
RUN ln -s /journal /data/db/journal  
RUN chown -R mongodb:mongodb /data \  
&& chown -R mongodb:mongodb /journal \  
&& chown -R mongodb:mongodb /log  
  
# Define mountable directory  
VOLUME /data  
VOLUME /log  
  
# Copy required files over to container  
COPY config/ /conf/  
  
# Copy script to run mongodb  
COPY entrypoint.sh /scripts/entrypoint.sh  
RUN chmod +x /scripts/entrypoint.sh  
ENTRYPOINT ["/scripts/entrypoint.sh"]  
  
# Define default command  
CMD ["mongod"]

