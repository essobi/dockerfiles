FROM debian:jessie  
MAINTAINER Arcus "http://arcus.io"  
RUN apt-get update  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get install -y wget openjdk-7-jre-headless git-core unzip
apache2-utils  
RUN wget -q -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | apt-key
add -  
RUN echo "deb http://pkg.jenkins-ci.org/debian binary/" >
/etc/apt/sources.list.d/jenkins.list  
RUN apt-get update  
RUN apt-get install -y jenkins  
RUN mkdir -p /var/lib/jenkins/plugins  
RUN (cd /var/lib/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-ci.org/latest/cobertura.hpi)  
RUN (cd /var/lib/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-ci.org/latest/greenballs.hpi)  
RUN (cd /var/lib/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-ci.org/latest/instant-messaging.hpi)  
RUN (cd /var/lib/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-ci.org/latest/ircbot.hpi)  
RUN (cd /var/lib/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-ci.org/latest/postbuild-task.hpi)  
RUN (cd /var/lib/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-ci.org/latest/copy-to-slave.hpi)  
RUN (cd /var/lib/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-ci.org/latest/credentials.hpi)  
RUN (cd /var/lib/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-ci.org/latest/ssh-credentials.hpi)  
RUN (cd /var/lib/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-ci.org/latest/ssh-agent.hpi)  
RUN (cd /var/lib/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-ci.org/latest/git-client.hpi)  
RUN (cd /var/lib/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-ci.org/latest/git.hpi)  
RUN (cd /var/lib/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-ci.org/latest/scm-api.hpi)  
RUN (cd /var/lib/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-ci.org/latest/swarm.hpi)  
RUN (cd /var/lib/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-ci.org/latest/envinject.hpi)  
RUN (cd /var/lib/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-ci.org/latest/parameterized-trigger.hpi)  
RUN (cd /var/lib/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-ci.org/latest/token-macro.hpi)  
RUN (cd /var/lib/jenkins/plugins && wget --no-check-certificate
http://updates.jenkins-ci.org/latest/build-name-setter.hpi)  
ADD config.xml /var/lib/jenkins/config.xml  
ENV JENKINS_HOME /var/lib/jenkins  
RUN wget --no-check-certificate
https://get.docker.io/builds/Linux/x86_64/docker-latest -O
/usr/local/bin/docker && chmod +x /usr/local/bin/docker  
RUN wget http://s3.amazonaws.com/ec2-downloads/ec2-api-tools.zip -O
/tmp/ec2tools.zip && \  
mkdir /usr/local/aws && unzip -d /usr/local/aws /tmp/ec2tools.zip && rm
/tmp/ec2tools.zip && \  
mv /usr/local/aws/ec2-api-tools-* /usr/local/aws/ec2  
ENV PATH $PATH:/usr/local/aws/ec2/bin  
ENV EC2_HOME /usr/local/aws/ec2  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64/jre  
  
  
EXPOSE 8080  
EXPOSE 8081  
VOLUME /var/lib/jenkins  
ENTRYPOINT ["java", "-jar", "/usr/share/jenkins/jenkins.war"]  
CMD []  

