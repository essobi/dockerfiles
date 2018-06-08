FROM ubuntu:trusty  
MAINTAINER Matsumoto Hiroko <h.matsumoto@sint.co.jp>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN sed -i 's/\/archive.ubuntu.com/\/jp.archive.ubuntu.com/g'
/etc/apt/sources.list && \  
apt-get update && apt-get install -q -y openjdk-7-jre-headless && apt-get
clean  
ADD http://mirrors.jenkins-ci.org/war/1.578/jenkins.war /opt/jenkins.war  
RUN chmod 644 /opt/jenkins.war  
ENV JENKINS_HOME /jenkins  
  
ENTRYPOINT ["java", "-jar", "/opt/jenkins.war"]  
EXPOSE 8080  
CMD [""]

