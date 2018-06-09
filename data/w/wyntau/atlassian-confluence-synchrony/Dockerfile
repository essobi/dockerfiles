FROM openjdk:8-jdk-alpine  
  
RUN apk add --no-cache bash curl tini  
  
ENV SYNCHRONY_HOME=/opt/atlassian/synchrony  
  
ENV DB_URL="jdbc:postgresql://postgres:5432/confluence"  
ENV DB_USER="root"  
ENV DB_PASSWD=""  
ENV SYNCHRONY_HOST="nginx"  
ENV CLUSTER_JOIN_PROPERTIES="-Dcluster.join.type=multicast"  
ARG SYNCHRONY_VERSION=6.8.2  
ARG SYNCHRONY_TARGZ=atlassian-confluence-${SYNCHRONY_VERSION}.tar.gz  
ARG
SYNCHRONY_DOWNLOAD_URL=https://www.atlassian.com/software/confluence/downloads/binary/${SYNCHRONY_TARGZ}  
  
ARG JDBC_DRIVER_JAR=postgresql-42.1.1.jar  
ARG JDBC_DRIVER_JAR_TARGZ_PATH=atlassian-
confluence-${SYNCHRONY_VERSION}/confluence/WEB-INF/lib/${JDBC_DRIVER_JAR}  
  
ARG SYNCHRONY_STANDALONE_JAR=synchrony-standalone.jar  
ARG SYNCHRONY_STANDALONE_JAR_TARGZ_PATH=atlassian-
confluence-${SYNCHRONY_VERSION}/confluence/WEB-
INF/packages/${SYNCHRONY_STANDALONE_JAR}  
  
ARG SYNCHRONY_DIR=synchrony  
ARG SYNCHRONY_DIR_TARGZ_PATH=atlassian-
confluence-${SYNCHRONY_VERSION}/bin/${SYNCHRONY_DIR}  
  
COPY ./getip.sh ${SYNCHRONY_HOME}/  
  
RUN curl -O -L --silent ${SYNCHRONY_DOWNLOAD_URL} \  
&& tar -xz -C "/opt/atlassian/" \--strip-components=2
${SYNCHRONY_DIR_TARGZ_PATH} < ${SYNCHRONY_TARGZ} \  
&& tar -xz -C "${SYNCHRONY_HOME}" \--strip-components=4
${JDBC_DRIVER_JAR_TARGZ_PATH} < ${SYNCHRONY_TARGZ} \  
&& tar -xz -C "${SYNCHRONY_HOME}" \--strip-components=4
${SYNCHRONY_STANDALONE_JAR_TARGZ_PATH} < ${SYNCHRONY_TARGZ} \  
&& rm ${SYNCHRONY_TARGZ} \  
&& sed -i -e 's/"<SERVER_IP>"/`${SYNCHRONY_HOME}\/getip.sh`/'
${SYNCHRONY_HOME}/start-synchrony.sh \  
&& sed -i -e 's/"<YOUR_DATABASE_URL>"/${DB_URL}/' ${SYNCHRONY_HOME}/start-
synchrony.sh \  
&& sed -i -e 's/"<DB_USERNAME>"/${DB_USER}/' ${SYNCHRONY_HOME}/start-
synchrony.sh \  
&& sed -i -e 's/"<DB_PASSWORD>"/${DB_PASSWD}/' ${SYNCHRONY_HOME}/start-
synchrony.sh \  
&& sed -i -e 's/"<JDBC_DRIVER_PATH>"/${SYNCHRONY_HOME}\/${JDBC_DRIVER_JAR}/'
${SYNCHRONY_HOME}/start-synchrony.sh \  
&& sed -i -e
's/"<PATH_TO_SYNCHRONY_STANDALONE_JAR>"/${SYNCHRONY_HOME}\/${SYNCHRONY_STANDALONE_JAR}/'
${SYNCHRONY_HOME}/start-synchrony.sh \  
&& sed -i -e 's/"<SYNCHRONY_URL>"/http:\/\/${SYNCHRONY_HOST}\/synchrony/'
${SYNCHRONY_HOME}/start-synchrony.sh  
  
CMD ["/opt/atlassian/synchrony/start-synchrony.sh", "-fg"]  
ENTRYPOINT [ "/sbin/tini", "--" ]  

