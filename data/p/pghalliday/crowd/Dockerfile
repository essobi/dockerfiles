FROM ubuntu:latest  
  
ENV ATLASSIAN_HOME=/var/atlassian/application-data \  
CROWD_USER=crowd \  
CROWD_GROUP=crowd \  
CROWD_CHECKSUM=c857eb16f65ed99ab8b289fe671e3cea89140d42f85639304caa91a3ba9ade05
\  
CROWD_BASENAME=atlassian-crowd-2.8.0 \  
CROWD_INSTALL_DIR=/opt/atlassian/crowd  
  
ENV CROWD_HOME=${ATLASSIAN_HOME}/crowd \  
CROWD_TARBALL=${CROWD_BASENAME}.tar.gz  
  
ENV
CROWD_URL=https://www.atlassian.com/software/crowd/downloads/binary/${CROWD_TARBALL}  
  
RUN apt-get update \  
&& apt-get install -y \  
wget \  
openjdk-7-jre  
ENV JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64  
  
RUN mkdir -p ${ATLASSIAN_HOME} \  
&& groupadd -r ${CROWD_GROUP} \  
&& useradd -r -g ${CROWD_GROUP} -d ${CROWD_HOME} ${CROWD_USER} \  
&& mkdir -p ${CROWD_INSTALL_DIR}  
  
# patch the openid configuration  
COPY crowd.properties /  
COPY crowd-init.properties /  
  
WORKDIR ${CROWD_INSTALL_DIR}  
RUN wget -q ${CROWD_URL} \  
&& echo ${CROWD_CHECKSUM} ${CROWD_TARBALL} | sha256sum -c - \  
&& tar zxf ${CROWD_TARBALL} \  
&& rm ${CROWD_TARBALL} \  
&& ln -s ${CROWD_BASENAME} current \  
&& chgrp ${CROWD_GROUP} current/*.sh \  
&& chgrp ${CROWD_GROUP} current/apache-tomcat/bin/*.sh \  
&& chmod g+x current/*.sh \  
&& chmod g+x current/apache-tomcat/bin/*.sh \  
&& chown -R ${CROWD_USER}:${CROWD_GROUP} current/apache-tomcat/logs \  
&& chown -R ${CROWD_USER}:${CROWD_GROUP} current/apache-tomcat/work \  
&& chown -R ${CROWD_USER}:${CROWD_GROUP} current/apache-tomcat/temp \  
&& touch -a current/atlassian-crowd-openid-server.log \  
&& mkdir current/database \  
&& chown -R ${CROWD_USER}:${CROWD_GROUP} current/database \  
&& chown -R ${CROWD_USER}:${CROWD_GROUP} current/atlassian-crowd-openid-
server.log \  
&& cp /crowd.properties current/crowd-openidserver-webapp/WEB-
INF/classes/crowd.properties \  
&& sed "s|CROWD_HOME|${CROWD_HOME}|g" </crowd-init.properties >current/crowd-
webapp/WEB-INF/classes/crowd-init.properties  
  
COPY docker-entrypoint.sh /  
COPY crowd-server.xml /  
COPY crowdid-postgres-openidserver.xml /  
COPY crowdid-postgres-jdbc.properties /  
VOLUME ${CROWD_HOME}  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
WORKDIR ${CROWD_INSTALL_DIR}/current  
EXPOSE 8095  
CMD apache-tomcat/bin/catalina.sh run  

