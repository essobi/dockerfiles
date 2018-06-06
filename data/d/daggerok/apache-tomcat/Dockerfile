##### USAGE BEGIN #####  
#  
# # apply base image:  
# FROM daggerok/apache-tomcat:9.0.6  
#  
# # healthy check:  
# HEALTHCHECK --interval=2s --retries=22 \  
# CMD wget -q --spider http://127.0.0.1:8080/app/health/ || exit 1  
#  
# # debug:  
# ARG JPDA_OPTS_ARG="${JAVA_OPTS}
-agentlib:jdwp=transport=dt_socket,address=1043,server=y,suspend=n"  
# ENV JPDA_OPTS="${JPDA_OPTS_ARG}"  
# EXPOSE 5005  
#  
# # multi-apps deployment:  
# COPY ./path/to/*.war ./path/to/another/*.war ${TOMCAT_HOME}/webapps/  
#  
##### USAGE END #####  
FROM openjdk:8u151-jdk-alpine  
MAINTAINER Maksim Kostromin https://github.com/daggerok/docker  
  
ARG TOMCAT_RELEASE=9  
ARG TOMCAT_VERSION=9.0.6  
ARG TOMCAT_USER_ARG="tomcat"  
ARG TOMCAT_FILE_ARG="apache-tomcat-${TOMCAT_VERSION}"  
ARG
TOMCAT_URL_ARG="https://archive.apache.org/dist/tomcat/tomcat-${TOMCAT_RELEASE}/v${TOMCAT_VERSION}/bin/${TOMCAT_FILE_ARG}.zip"  
ENV JAVA_VERSION="8"  
ENV TOMCAT_USER=${TOMCAT_USER_ARG} \  
TOMCAT_GROUP=${TOMCAT_USER_ARG}-group \  
TOMCAT_FILE=${TOMCAT_FILE_ARG} \  
TOMCAT_URL=${TOMCAT_URL_ARG}  
ENV TOMCAT_USER_HOME="/home/${TOMCAT_USER}"  
ENV TOMCAT_HOME="${TOMCAT_USER_HOME}/${TOMCAT_FILE}"  
RUN apk --no-cache --update add busybox-suid bash wget ca-certificates unzip
sudo openssh-client shadow \  
&& addgroup ${TOMCAT_GROUP} \  
&& echo "${TOMCAT_USER} ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers \  
&& sed -i "s/.*requiretty$/Defaults !requiretty/" /etc/sudoers \  
&& adduser -h ${TOMCAT_USER_HOME} -s /bin/bash -D -u 1025 ${TOMCAT_USER}
${TOMCAT_GROUP} \  
&& usermod -a -G wheel ${TOMCAT_USER} \  
&& wget --no-cookies \  
\--no-check-certificate \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie" \  
"http://download.oracle.com/otn-pub/java/jce/8/jce_policy-8.zip" \  
-O /tmp/jce_policy-8.zip \  
&& unzip -o /tmp/jce_policy-8.zip -d /tmp \  
&& mv -f ${JAVA_HOME}/lib/security ${JAVA_HOME}/lib/backup-security || true \  
&& mv -f /tmp/UnlimitedJCEPolicyJDK8 ${JAVA_HOME}/lib/security \  
&& apk --no-cache --no-network --purge del busybox-suid ca-certificates unzip
shadow \  
&& rm -rf /var/cache/apk/* /tmp/*  
  
USER ${TOMCAT_USER}  
WORKDIR ${TOMCAT_USER_HOME}  
  
CMD /bin/bash  
EXPOSE 8080  
ENTRYPOINT /bin/bash ${TOMCAT_HOME}/bin/catalina.sh start \  
&& tail -f ${TOMCAT_HOME}/logs/catalina.out  
  
RUN wget ${TOMCAT_URL} -O "${TOMCAT_USER_HOME}/${TOMCAT_FILE}.zip" \  
&& unzip "${TOMCAT_USER_HOME}/${TOMCAT_FILE}.zip" -d ${TOMCAT_USER_HOME} \  
&& rm -rf "${TOMCAT_USER_HOME}/${TOMCAT_FILE}.zip" \  
&& mkdir -p ${TOMCAT_HOME}/logs && touch ${TOMCAT_HOME}/logs/catalina.out \  
&& chown -R ${TOMCAT_USER}:${TOMCAT_USER} ${TOMCAT_HOME}/logs  

