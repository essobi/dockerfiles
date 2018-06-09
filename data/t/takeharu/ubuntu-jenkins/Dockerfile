FROM ubuntu:14.04  
MAINTAINER Takeharu Yamaguchi <https://github.com/takeharu>  
  
RUN apt-get update && apt-get install -y wget  
RUN wget -q -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key|apt-key
add -  
RUN sh -c 'echo deb http://pkg.jenkins-ci.org/debian binary/ >
/etc/apt/sources.list.d/jenkins.list'  
RUN apt-get update && apt-get install -y jenkins  
  
EXPOSE 8080  
CMD ["java","-jar","/usr/share/jenkins/jenkins.war"]  

