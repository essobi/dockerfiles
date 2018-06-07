FROM eviles/oracle-jdk8  
  
ARG JENKINS_VERSION=2.14  
ARG JENKINS_USER=jenkins  
ARG JENKINS_GROUP=jenkins  
ARG JENKINS_UID=1000  
ARG JENKINS_GID=1000  
ENV JENKINS_HOME=/var/jenkins  
ENV JENKINS_SLAVE_AGENT_PORT=50000  
RUN /usr/sbin/groupadd --gid $JENKINS_GID $JENKINS_GROUP \  
&& /usr/sbin/useradd --uid $JENKINS_UID \--gid $JENKINS_GID \--create-home
--shell /bin/bash $JENKINS_USER \  
&& yum install -y wget git git-svn unzip zip bzip2 \  
&& yum clean all \  
&& rm -rf /var/cache/yum/* \  
&& mkdir -p /usr/share/jenkins \  
&& curl -fsSL http://repo.jenkins-ci.org/public/org/jenkins-ci/main/jenkins-
war/${JENKINS_VERSION}/jenkins-war-${JENKINS_VERSION}.war -o
/usr/share/jenkins/jenkins.war \  
&& chown -R $JENKINS_USER:$JENKINS_GROUP /usr/share/jenkins \  
&& chmod ug+x /usr/share/jenkins/jenkins.war \  
&& mkdir -p ${JENKINS_HOME} \  
&& chown -R $JENKINS_USER:$JENKINS_GROUP ${JENKINS_HOME} \  
&& echo "[program:jenkins]" >> /etc/supervisord.conf \  
#&& echo "user=jenkins" >> /etc/supervisord.conf \  
&& echo "command=java -jar /usr/share/jenkins/jenkins.war" >>
/etc/supervisord.conf  
  
EXPOSE 8080 50000  
VOLUME /var/jenkins  

