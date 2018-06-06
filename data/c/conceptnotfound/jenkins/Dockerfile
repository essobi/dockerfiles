FROM ubuntu:12.10  
RUN apt-get update  
RUN apt-get install -y default-jre  
RUN apt-get install -y wget  
  
RUN wget -qO/usr/local/jenkins.war http://mirrors.jenkins-
ci.org/war/1.568/jenkins.war  
  
VOLUME /jenkins  
  
EXPOSE 8080  
ENV CONTEXT_PATH /jenkins  
  
CMD JENKINS_HOME=/jenkins java -jar /usr/local/jenkins.war
--prefix=$CONTEXT_PATH  

