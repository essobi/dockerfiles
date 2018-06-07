FROM openjdk:7-jdk  
  
ENV ZEPPELIN_VERSION=0.7.0 \  
ZEPPELIN_HOME=/opt/zeppelin \  
MONGO_VERSION=3.4  
RUN mkdir -p ${ZEPPELIN_HOME} && \  
curl -SL
http://mirror.easyname.ch/apache/zeppelin/zeppelin-${ZEPPELIN_VERSION}/zeppelin-${ZEPPELIN_VERSION}-bin-
all.tgz \  
| tar xz -C ${ZEPPELIN_HOME} && \  
mv ${ZEPPELIN_HOME}/zeppelin-${ZEPPELIN_VERSION}-bin-all/* ${ZEPPELIN_HOME} &&
\  
rm -rf ${ZEPPELIN_HOME}/zeppelin-${ZEPPELIN_VERSION}-bin-all && \  
rm -rf *.tgz && \  
mkdir -p ${ZEPPELIN_HOME}/interpreter/mongodb && \  
curl -SL -o ${ZEPPELIN_HOME}/interpreter/mongodb/zeppelin-
mongodb-${ZEPPELIN_VERSION}.jar \  
https://github.com/bbonnin/zeppelin-mongodb-
interpreter/releases/download/${ZEPPELIN_VERSION}/zeppelin-
mongodb-${ZEPPELIN_VERSION}.zip  
  
COPY run.sh /${ZEPPELIN_HOME}/run.sh  
RUN chmod +x /${ZEPPELIN_HOME}/run.sh  
  
# Install Mongo Shell  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
0C49F3730359A14518585931BC711F9BA15703C6 && \  
echo "deb http://repo.mongodb.org/apt/debian jessie/mongodb-
org/${MONGO_VERSION} main" > /etc/apt/sources.list.d/mongodb-org.list && \  
apt-get update && \  
apt-get install -y mongodb-org-shell  
  
EXPOSE 8080  
VOLUME ${ZEPPELIN_HOME}/logs ${ZEPPELIN_HOME}/notebook  
  
CMD ${ZEPPELIN_HOME}/run.sh

