FROM densuke/trusty-jp:latest  
MAINTAINER densuke  
RUN apt-get update  
RUN apt-get install -y openjdk-7-jre-headless git wget  
RUN mkdir /var/jenkins_home  
USER root  
WORKDIR /  
ENV JENKINS_HOME /var/jenkins_home  
ENV PATH /usr/local/bin:/usr/bin:/bin  
RUN wget -nv -O /usr/local/bin/jenkins.war http://mirrors.jenkins-
ci.org/war/latest/jenkins.war  
EXPOSE 8080  
EXPOSE 50000  
ENTRYPOINT ["/usr/bin/java", "-jar", "/usr/local/bin/jenkins.war"]  

