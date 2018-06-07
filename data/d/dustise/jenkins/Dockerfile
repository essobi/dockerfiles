FROM dustise/oracle-jdk:alpine-jdk-0.8.4  
COPY run.sh /usr/local/bin  
COPY prepare.sh /usr/local/bin  
COPY config.xml /usr/share/jenkins/config/config.xml  
COPY install-plugins.sh /usr/local/bin  
COPY jenkins-support /usr/local/bin  
ENV JENKINS_HOME="/data/jenkins" \  
MAVEN_HOME="/usr/local/share/maven" \  
SONAR_HOME="/usr/local/share/sonar" \  
MAVEN_VER="3.5.3" \  
SONAR_SCANNER_VER="3.1.0.1141-linux" \  
KUBECTL_VER="1.10.2" \  
SLAVE_VER="3.20" \  
JENKINS_MODE="MASTER" \  
TIMEZONE="Asia/Shanghai" \  
JENKINS_UC="https://updates.jenkins-ci.org" \  
REF="$JENKINS_HOME/plugins" \  
ADMIN_USER="root" \  
ADMIN_PASSWORD="abcd!@#$"  
RUN prepare.sh  
EXPOSE 8080  
VOLUME ["/usr/share/jenkins/", "/data/jenkins", "/data/maven", "/data/kube",
"/data/sonar", "/data/robot"]  
CMD ["run.sh"]  

