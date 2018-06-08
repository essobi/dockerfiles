FROM java:7  
MAINTAINER http://kieker-monitoring.net/support/  
  
WORKDIR /opt  
  
EXPOSE 9191 9192  
# Set folder variables  
ENV KIEKER_FOLDER /opt/kieker  
ENV KIEKER_AGENT_FOLDER ${KIEKER_FOLDER}/agent  
ENV KIEKER_CONFIG_FOLDER ${KIEKER_FOLDER}/config  
ENV KIEKER_TMP_CONFIG_FOLDER ${KIEKER_FOLDER}/tmp-config  
ENV KIEKER_LOGS_FOLDER ${KIEKER_FOLDER}/logs  
ENV KIEKER_JAR_FOLDER ${KIEKER_FOLDER}/jar  
  
ENV KIEKER_RECIPESRSS_FOLDER ${KIEKER_FOLDER}/recipes-rss  
ENV KIEKER_RECIPESRSS_GIT "https://github.com/hora-prediction/recipes-rss"  
# Set other variables  
ENV KIEKER_MONITORING_PROPERTIES kieker.monitoring.properties  
ENV KIEKER_AGENT_JAR agent.jar  
ENV KIEKER_AOP aop.xml  
ENV KIEKER_JAVA_JAR rss-middletier.jar  
ENV APP_ENV dev  
  
COPY ${KIEKER_MONITORING_PROPERTIES}
${KIEKER_TMP_CONFIG_FOLDER}/${KIEKER_MONITORING_PROPERTIES}  
COPY ${KIEKER_AOP} ${KIEKER_TMP_CONFIG_FOLDER}/META-INF/${KIEKER_AOP}  
  
RUN \  
mkdir -p ${KIEKER_AGENT_FOLDER} && \  
mkdir -p ${KIEKER_LOGS_FOLDER} && \  
mkdir -p ${KIEKER_JAR_FOLDER} && \  
git clone ${KIEKER_RECIPESRSS_GIT} ${KIEKER_RECIPESRSS_FOLDER} && \  
cd ${KIEKER_RECIPESRSS_FOLDER} && \  
./gradlew -x check -x test clean build && \  
cp ${KIEKER_RECIPESRSS_FOLDER}/rss-middletier/build/libs/rss-
middletier*SNAPSHOT.jar ${KIEKER_JAR_FOLDER}/${KIEKER_JAVA_JAR} && \  
rm ${KIEKER_RECIPESRSS_FOLDER} -r && \  
rm /root/.gradle -r  
  
ENV KIEKER_AGENT_JAR_SRC "https://build.se.informatik.uni-
kiel.de/jenkins/job/kieker-
monitoring/job/kieker/job/master/lastSuccessfulBuild/artifact/build/libs/kieker-1.13-SNAPSHOT-
aspectj.jar"  
RUN \  
wget -q "${KIEKER_AGENT_JAR_SRC}" -O
"${KIEKER_AGENT_FOLDER}/${KIEKER_AGENT_JAR}"  
  
CMD \  
cp -nr ${KIEKER_TMP_CONFIG_FOLDER}/* ${KIEKER_CONFIG_FOLDER}/ && \  
rm ${KIEKER_TMP_CONFIG_FOLDER}/ -r && \  
java \  
-javaagent:${KIEKER_AGENT_FOLDER}/${KIEKER_AGENT_JAR} \  
-Deureka.serviceUrl.default=http://${TOMCAT_PORT_8080_TCP_ADDR}:8080/eureka/v2/ \  
-Dkieker.monitoring.configuration=${KIEKER_CONFIG_FOLDER}/${KIEKER_MONITORING_PROPERTIES} \  
-Dkieker.monitoring.writer.filesystem.AsciiFileWriter.customStoragePath=${KIEKER_LOGS_FOLDER} \  
-Daj.weaving.verbose=true \  
-Dkieker.monitoring.skipDefaultAOPConfiguration=true \  
-cp ${KIEKER_CONFIG_FOLDER}:${KIEKER_JAR_FOLDER}/${KIEKER_JAVA_JAR} \  
com.netflix.recipes.rss.server.MiddleTierServer  
  
VOLUME ["/opt/kieker"]  

