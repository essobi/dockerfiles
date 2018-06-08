FROM manorrock/openjdk  
ENV JENKINS_VERSION 2.107.2  
ENV JENKINS_HOME /mnt  
ENV JENKINS_SLAVE_AGENT_PORT 50000  
RUN zypper --non-interactive refresh && \  
zypper --non-interactive install curl git && \  
curl -fL -o /opt/jenkins.war https://repo.jenkins-ci.org/public/org/jenkins-
ci/main/jenkins-war/{$JENKINS_VERSION}/jenkins-war-{$JENKINS_VERSION}.war && \  
zypper --non-interactive remove curl && \  
zypper --non-interactive clean -a  
WORKDIR ${JENKINS_HOME}  
EXPOSE 8080 ${JENKINS_SLAVE_AGENT_PORT}  
CMD ["sh", "-c", "java -jar /opt/jenkins.war"]  
  

