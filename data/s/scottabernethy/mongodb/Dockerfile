# Dockerfile for scottabernethy/mongo  
FROM scottabernethy/debian  
  
# Add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -r mongodb && useradd -r -g mongodb mongodb  
  
ENV MONGO_MAJOR 3.0  
ENV MONGO_VERSION 3.0.2  
# gpg: key 7F0CEB10: public key "Richard Kreuter <richard@10gen.com>" imported  
RUN \  
apt-key adv --keyserver pool.sks-keyservers.net --recv-keys
492EAFE8CD016A07919F1D2B9ECBEC467F0CEB10 && \  
echo "deb http://repo.mongodb.org/apt/debian wheezy/mongodb-org/$MONGO_MAJOR
main" > /etc/apt/sources.list.d/mongodb-org.list  
  
RUN \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
mongodb-org=$MONGO_VERSION \  
numactl \  
&& \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/lib/mongodb && \  
mv /etc/mongod.conf /etc/mongod.conf.orig  
  
RUN mkdir -p /data/db && chown -R mongodb:mongodb /data/db  
VOLUME /data/db  
  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 27017  
CMD ["mongod"]  

