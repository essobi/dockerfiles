#  
# Jenkins Dockerfile  
#  
# https://github.com/tamboraorg/docker/crejenkins  
#  
# Pull base image.  
FROM tamboraorg/crejava:2010.0  
MAINTAINER Michael Kahle <michael.kahle@yahoo.de>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV INITRD No  
ENV LANG en_US.UTF-8  
RUN wget -q -O - https://pkg.jenkins.io/debian/jenkins-ci.org.key | apt-key
add - && \  
echo deb https://pkg.jenkins.io/debian-stable binary/ | tee
/etc/apt/sources.list.d/jenkins.list  
  
RUN apt-get update && \  
apt-get install --no-install-recommends -y openjdk-$JAVA_VERSION-jdk jenkins
ant && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
update-rc.d -f jenkins disable  
  
RUN mkdir -p /cre && touch /cre/versions.txt && \  
echo "$(date +'%F %R') \t creJenkins \t $(java -jar
/usr/share/jenkins/jenkins.war --version)" >> /cre/versions.txt && \  
echo "$(date +'%F %R') \t ant \t $(ant -version)" >> /cre/versions.txt  
  
ENV JENKINS_HOME /var/jenkins  
  
COPY cre /cre  
  
EXPOSE 8080 50000  
# CMD ["/usr/bin/java", "-jar", "/usr/share/jenkins/jenkins.war"]  
CMD ["/usr/bin/java", "-jar", "/usr/share/jenkins/jenkins.war", "--
argumentsRealm.passwd.jenkins=swordfish", "--
argumentsRealm.roles.jenkins=admin"]  
# CMD /cre/start-jenkins.sh  
# CMD ["/usr/bin/java", "-version"]

