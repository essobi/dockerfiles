# Dockerizing base image for eXo Platform with:  
#  
# - Libre Office  
# - eXo Platform Community  
# Build: docker build -t exoplatform/ubuntu-jdk7-exo:plf-4.1.0 .  
#  
# Run: docker run -t -i --name=exo exoplatform/ubuntu-jdk7-exo:plf-4.1.0  
# docker run -d --name=exo exoplatform/ubuntu-jdk7-exo:plf-4.1.0  
# docker run -d --name=exo -p 8080:8080 exoplatform/ubuntu-jdk7-exo:plf-4.1.0  
FROM ubuntu:latest  
MAINTAINER Mihai Csaky <mihai.csaky@sysop-consulting.ro>  
  
# Environment variables  
ENV EXO_VERSION 4.3.0  
ENV EXO_RELEASE 4.3.0  
ENV EXO_EDITION community  
ENV MYSQL_DRIVER_VERSION 5.1.38  
ENV EXO_APP_DIR /opt/exo  
ENV EXO_DATA_DIR /srv/exo  
ENV EXO_LOG_DIR /var/log/exo  
ENV EXO_TMP_DIR /tmp/exo-tmp  
  
ENV EXO_USER exo  
ENV EXO_GROUP ${EXO_USER}  
  
ENV JAVA_HOME /usr/local/java  
ENV ORACLE_JAVA_HOME /usr/lib/jvm/java-7-oracle/  
  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN useradd --create-home --user-group --shell /bin/bash ${EXO_USER}  
  
# Set the debconf frontend to Noninteractive  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
RUN apt-get -y install software-properties-common  
  
#prepare and install JDK  
RUN \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java7-installer  
  
RUN ln -s $ORACLE_JAVA_HOME $JAVA_HOME  
  
#install additional software  
RUN apt-get -y install ant curl unzip sudo tar software-properties-common
python-jinja2 python-pip jq git  
RUN pip install j2cli  
  
# Install some useful or needed tools  
RUN apt-get -qq update && \  
apt-get -qq -y upgrade && \  
apt-get -qq -y install libreoffice-calc libreoffice-draw libreoffice-impress
libreoffice-math libreoffice-writer && \  
apt-get -qq -y autoremove && \  
apt-get -qq -y autoclean  
  
# Create needed directories  
RUN mkdir -p ${EXO_APP_DIR}  
RUN mkdir -p ${EXO_DATA_DIR} && chown ${EXO_USER}:${EXO_GROUP} ${EXO_DATA_DIR}  
RUN mkdir -p ${EXO_TMP_DIR} && chown ${EXO_USER}:${EXO_GROUP} ${EXO_TMP_DIR}  
RUN mkdir -p ${EXO_LOG_DIR} && chown ${EXO_USER}:${EXO_GROUP} ${EXO_LOG_DIR}  
  
# Install eXo Platform  
# http://sourceforge.net/projects/exo/files/Platform4.2/eXo-Platform-
community-tomcat-4.2.0.zip/download  
# http://netcologne.dl.sourceforge.net/project/exo/Platform4.2/eXo-Platform-
community-tomcat-4.2.0.zip  
# http://netcologne.dl.sourceforge.net/project/exo/Platform4.3/eXo-Platform-
community-4.3.0.zip  
RUN curl -L -o ${EXO_DATA_DIR}/eXo-Platform-${EXO_EDITION}-${EXO_VERSION}.zip
\  
http://netcologne.dl.sourceforge.net/project/exo/Platform4.3/eXo-Platform-
community-4.3.0.zip && \  
unzip -q ${EXO_DATA_DIR}/eXo-Platform-${EXO_EDITION}-${EXO_VERSION}.zip -d
${EXO_APP_DIR} && \  
rm -f ${EXO_DATA_DIR}/eXo-Platform-${EXO_EDITION}-${EXO_VERSION}.zip && \  
ln -s ${EXO_APP_DIR}/platform-${EXO_EDITION}-${EXO_RELEASE}
${EXO_APP_DIR}/current  
  
#Add mysql JDBC driver  
#http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-5.1.37.zip  
RUN curl -L -o ${EXO_DATA_DIR}/mysql-jdbc-${MYSQL_DRIVER_VERSION}.zip
https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-${MYSQL_DRIVER_VERSION}.zip && \  
unzip -q ${EXO_DATA_DIR}/mysql-jdbc-${MYSQL_DRIVER_VERSION}.zip -d /srv/ && \  
cp /srv/mysql-connector-java-${MYSQL_DRIVER_VERSION}/mysql-connector-
java-${MYSQL_DRIVER_VERSION}-bin.jar ${EXO_APP_DIR}/current/lib/  
  
COPY server.xml ${EXO_APP_DIR}/current/conf/server.xml  
COPY exo.properties ${EXO_APP_DIR}/current/gatein/conf/exo.properties  
  
RUN echo "JAVA_OPTS=\"-Dmysql.database=\$MYSQL_DATABASE
-Dmysql.user=\$MYSQL_USER -Dmysql.password=\$MYSQL_PASSWORD
-Dmysql.host=\$MYSQL_SERVICE_HOST -Dmysql.port=\$MYSQL_SERVICE_PORT
\$JAVA_OPTS\"" >> ${EXO_APP_DIR}/current/bin/setenv.sh && \  
rm -rf ${EXO_APP_DIR}/current/logs && ln -s ${EXO_LOG_DIR}
${EXO_APP_DIR}/current/logs && \  
chown -R ${EXO_USER}:${EXO_GROUP} ${EXO_APP_DIR}/current/  
  
EXPOSE 8080  
# FIXME : replace "exo" by ${EXO_USER} when
https://github.com/docker/docker/issues/4909 will be fixed.  
USER exo  
CMD ${EXO_APP_DIR}/current/start_eXo.sh --data ${EXO_DATA_DIR}  
  

