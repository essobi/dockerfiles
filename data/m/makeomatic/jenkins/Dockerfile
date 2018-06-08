# Docker file to create Jenkins container.  
FROM cgswong/java:orajdk8  
  
# Setup environment  
ENV JENKINS_VERSION=1.658 \  
JENKINS_USER=jenkins \  
JENKINS_GROUP=jenkins \  
JENKINS_HOME=/opt/jenkins \  
JENKINS_PLUGINS="credentials ssh-credentials ssh-agent ssh-slaves git-client
git github github-api github-oauth ghprb scm-api postbuild-task greenballs"  
# # Install software  
RUN \  
apk --update upgrade \  
&& apk add openssh-client \  
&& mkdir -p ${JENKINS_HOME} ${JENKINS_HOME}/plugins ${JAVA_BASE} \  
&& addgroup ${JENKINS_GROUP} \  
&& adduser -h ${JENKINS_HOME} -D -s /bin/bash -G ${JENKINS_GROUP}
${JENKINS_USER} \  
&& chown -R ${JENKINS_USER}:${JENKINS_GROUP} ${JENKINS_HOME} \  
&& apk add 'su-exec>=0.2' \  
&& rm -rf /var/cache/apk/*  
  
# this is what we want jenkins to run with  
RUN apk --no-cache add --virtual .runDeps \  
git \  
openssl \  
ca-certificates  
  
# Expose volumes  
VOLUME ["${JENKINS_HOME}"]  
  
# Listen for main web interface (8080/tcp) and attached slave agents
(50000/tcp)  
EXPOSE 8080 50000  
COPY entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  
CMD ["java", "-jar", "/opt/jenkins/jenkins-${JENKINS_VERSION}.war"]  

