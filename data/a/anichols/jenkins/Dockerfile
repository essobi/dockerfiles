FROM ubuntu:14.04  
MAINTAINER Aaron Nichols "anichols@trumped.org"  
RUN echo deb http://archive.ubuntu.com/ubuntu precise universe >>
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get install -y openjdk-7-jre-headless git  
RUN apt-get clean  
ADD http://mirrors.jenkins-ci.org/war/1.568/jenkins.war /opt/jenkins.war  
RUN ln -sf /jenkins /root/.jenkins  
  
EXPOSE 8080  
VOLUME ["/jenkins"]  
CMD /usr/bin/java -jar /opt/jenkins.war $JAVA_OPTS  

