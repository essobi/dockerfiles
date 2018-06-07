FROM centos:7.3.1611  
MAINTAINER Rajesh Jonnalagadda(<admin.squad@phenompeople.com>)  
EXPOSE 27017  
ARG MONGODB_VERSION=3.4.9  
ARG MONGO_HOME=/opt/mongodb  
RUN useradd mongod -u 402 && \  
yum install -y -q wget && \  
wget -q -O /tmp/mongodb.tar.gz https://fastdl.mongodb.org/linux/mongodb-
linux-x86_64-${MONGODB_VERSION}.tgz && \  
tar -xzf /tmp/mongodb.tar.gz -C /opt/ && \  
ln -sf /opt/mongodb-linux-x86_64-${MONGODB_VERSION} /opt/mongodb  
ADD start-server.sh /opt/mongodb/start-server.sh  
RUN mkdir -p /var/log/mongodb /etc/mongodb /var/run/mongodb && \  
chown -R mongod:mongod /var/log/mongodb /var/log/mongodb /var/run/mongodb
/opt/mongodb && \  
touch /var/log/mongodb/mongod.log && \  
chmod a+x /opt/mongodb/start-server.sh  
ADD mongod.conf /etc/mongod.conf  
ENV MONGO_HOME=${MONGO_HOME} \  
PATH=${MONGO_HOME}/bin:$PATH  
USER mongod  
ENTRYPOINT ["/opt/mongodb/start-server.sh"]

