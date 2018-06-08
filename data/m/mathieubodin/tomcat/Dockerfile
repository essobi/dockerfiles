FROM alpine:latest as prepare-install  
  
LABEL MAINTAINER="mathieu.bodin@gmail.com"  
  
RUN apk add --no-cache --virtual=build-dependencies curl unzip  
  
RUN mkdir -p /tomcat  
  
ARG JAVA_VERSION=8  
ARG JAVA_UPDATE=161  
ARG JAVA_BUILD=12  
ARG TOMCAT_VERSION=8.0.50  
ARG TOMCAT_MAJOR=8  
# Install Java  
ARG ORACLE_TOKEN=2f38c3b165be4555a1fa6e98c45e0808  
ARG JAVA_DOWNLOAD_URL=http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION}u${JAVA_UPDATE}-b${JAVA_BUILD}/${ORACLE_TOKEN}/jdk-${JAVA_VERSION}u${JAVA_UPDATE}-linux-x64.tar.gz  
  
RUN curl -LSs -b "oraclelicense=accept-securebackup-cookie"
${JAVA_DOWNLOAD_URL} -o /jdk-linux-x64.tar.gz  
RUN tar xzf /jdk-linux-x64.tar.gz -C /tomcat  
RUN mv /tomcat/jdk1.${JAVA_VERSION}.0_${JAVA_UPDATE} /tomcat/jdk  
ARG JAVA_HOME=/tomcat/jdk  
# Install JCE  
ARG JCE_DOWNLOAD_URL=http://download.oracle.com/otn-
pub/java/jce/${JAVA_VERSION}/jce_policy-${JAVA_VERSION}.zip  
RUN curl -LSs -b "oraclelicense=accept-securebackup-cookie"
${JCE_DOWNLOAD_URL} -o /jce_policy.zip  
RUN unzip -jo -d ${JAVA_HOME}/jre/lib/security /jce_policy.zip  
# Install Tomcat  
ARG
TOMCAT_DOWNLOAD_URL=https://www.apache.org/dist/tomcat/tomcat-${TOMCAT_MAJOR}/v${TOMCAT_VERSION}/bin/apache-
tomcat-${TOMCAT_VERSION}.tar.gz  
RUN curl -sSG ${TOMCAT_DOWNLOAD_URL} -o /apache-tomcat.tar.gz  
RUN tar xzf /apache-tomcat.tar.gz -C /tomcat  
RUN mv /tomcat/apache-tomcat-${TOMCAT_VERSION} /tomcat/apache-tomcat  
ARG CATALINA_HOME=/tomcat/apache-tomcat  
  
# Configure Tomcat  
COPY tomcat-users.xml ${CATALINA_HOME}/conf  
  
# Clean up  
RUN apk del --no-cache build-dependencies  
RUN rm /jdk-linux-x64.tar.gz /apache-tomcat.tar.gz /jce_policy.zip  
RUN rm -rf ${JAVA_HOME}/*src.zip \  
${JAVA_HOME}/lib/missioncontrol \  
${JAVA_HOME}/lib/visualvm \  
${JAVA_HOME}/lib/*javafx* \  
${JAVA_HOME}/jre/lib/security/README.txt \  
${JAVA_HOME}/jre/lib/plugin.jar \  
${JAVA_HOME}/jre/lib/ext/jfxrt.jar \  
${JAVA_HOME}/jre/bin/javaws \  
${JAVA_HOME}/jre/lib/javaws.jar \  
${JAVA_HOME}/jre/lib/desktop \  
${JAVA_HOME}/jre/plugin \  
${JAVA_HOME}/jre/lib/deploy* \  
${JAVA_HOME}/jre/lib/*javafx* \  
${JAVA_HOME}/jre/lib/*jfx* \  
${JAVA_HOME}/jre/lib/amd64/libdecora_sse.so \  
${JAVA_HOME}/jre/lib/amd64/libprism_*.so \  
${JAVA_HOME}/jre/lib/amd64/libfxplugins.so \  
${JAVA_HOME}/jre/lib/amd64/libglass.so \  
${JAVA_HOME}/jre/lib/amd64/libgstreamer-lite.so \  
${JAVA_HOME}/jre/lib/amd64/libjavafx*.so \  
${JAVA_HOME}/jre/lib/amd64/libjfx*.so \  
${JAVA_HOME}/jre/bin/jjs \  
${JAVA_HOME}/jre/bin/keytool \  
${JAVA_HOME}/jre/bin/orbd \  
${JAVA_HOME}/jre/bin/pack200 \  
${JAVA_HOME}/jre/bin/policytool \  
${JAVA_HOME}/jre/bin/rmid \  
${JAVA_HOME}/jre/bin/rmiregistry \  
${JAVA_HOME}/jre/bin/servertool \  
${JAVA_HOME}/jre/bin/tnameserv \  
${JAVA_HOME}/jre/bin/unpack200 \  
${JAVA_HOME}/jre/lib/ext/nashorn.jar \  
${JAVA_HOME}/jre/lib/jfr.jar \  
${JAVA_HOME}/jre/lib/jfr \  
${JAVA_HOME}/jre/lib/oblique-fonts \  
${CATALINA_HOME}/bin/*.bat \  
${CATALINA_HOME}/webapps/docs \  
${CATALINA_HOME}/webapps/ROOT \  
${CATALINA_HOME}/webapps/examples \  
${CATALINA_HOME}/webapps/host-manager  
  
FROM gcr.io/distroless/base  
  
COPY --from=prepare-install /tomcat /  
  
EXPOSE 8000 8005 8009 8080  
  
ENTRYPOINT [ "/jdk/bin/java" ]  
CMD [ "-Djava.util.logging.config.file=/apache-
tomcat/conf/logging.properties", \  
"-Djava.util.logging.manager=org.apache.juli.ClassLoaderLogManager", \  
"-Djdk.tls.ephemeralDHKeySize=2048", \  
"-Djava.protocol.handler.pkgs=org.apache.catalina.webresources", \  
"-agentlib:jdwp=transport=dt_socket,address=127.0.0.1:8000,server=y,suspend=n",
\  
"-classpath", "/apache-tomcat/bin/bootstrap.jar:/apache-tomcat/bin/tomcat-
juli.jar", \  
"-Dcatalina.base=/apache-tomcat", \  
"-Dcatalina.home=/apache-tomcat", \  
"-Dcatalina.admin.password=", \  
"-Djava.io.tmpdir=/apache-tomcat/temp", \  
"org.apache.catalina.startup.Bootstrap", \  
"start" ]

