FROM tomcat:8-jre8  
MAINTAINER Saberfrost  
  
ENV TZ Asia/Tokyo  
  
ENV GITBUCKET_HOME=/var/gitbucket  
ENV JENKINS_HOME=/var/jenkins  
ENV CATALINA_HOME=/usr/local/tomcat  
  
# Tomcat config  
COPY tomcat-users.xml $CATALINA_HOME/conf/tomcat-users.xml  
  
# gitbucket  
Add https://github.com/gitbucket/gitbucket/releases/download/4.0/gitbucket.war
$CATALINA_HOME/webapps/gitbucket.war  
#COPY gitbucket.war $CATALINA_HOME/webapps/gitbucket.war  
# jenkins  
Add http://mirrors.jenkins-ci.org/war/2.5/jenkins.war
$CATALINA_HOME/webapps/jenkins.war  
#COPY jenkins.war $CATALINA_HOME/webapps/jenkins.war  
WORKDIR $CATALINA_HOME  
  
EXPOSE 8080  
CMD [ "/usr/local/tomcat/bin/catalina.sh", "run" ]  
  

