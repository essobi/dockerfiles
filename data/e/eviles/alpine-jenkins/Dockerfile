FROM eviles/alpine-oracle-jdk8  
  
ARG JENKINS_VERSION=2.61  
ARG JENKINS_USER=jenkins  
ARG JENKINS_GROUP=jenkins  
ARG JENKINS_UID=1000  
ARG JENKINS_GID=1000  
ENV JENKINS_HOME=/var/jenkins  
ENV JENKINS_SLAVE_AGENT_PORT=50000  
RUN /usr/sbin/addgroup -g $JENKINS_GID $JENKINS_GROUP \  
&& /usr/sbin/adduser -u $JENKINS_UID -G $JENKINS_GROUP -h /home/$JENKINS_USER
-D $JENKINS_USER \  
&& apk --update add wget tar git unzip zip bzip2 \  
&& rm -rf /var/cache/apk/* \  
&& mkdir -p /usr/share/jenkins \  
&& curl -fsSL http://repo.jenkins-ci.org/public/org/jenkins-ci/main/jenkins-
war/${JENKINS_VERSION}/jenkins-war-${JENKINS_VERSION}.war -o
/usr/share/jenkins/jenkins.war \  
&& chown -R $JENKINS_USER:$JENKINS_GROUP /usr/share/jenkins \  
&& chmod ug+x /usr/share/jenkins/jenkins.war \  
&& mkdir -p ${JENKINS_HOME} \  
&& chown -R $JENKINS_USER:$JENKINS_GROUP ${JENKINS_HOME} \  
&& echo "[program:jenkins]" >> /etc/supervisord.conf \  
&& echo "user=jenkins" >> /etc/supervisord.conf \  
&& echo "command=java -jar /usr/share/jenkins/jenkins.war" >>
/etc/supervisord.conf  
  
EXPOSE 8080 50000  
VOLUME /var/jenkins  

