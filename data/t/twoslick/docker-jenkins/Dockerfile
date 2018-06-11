FROM stackbrew/ubuntu:14.04  
MAINTAINER Tim Rupe "tim@rupe.org"  
# Java 8 install  
# Add oracle ppa @ webupd8  
RUN apt-get update  
RUN apt-get -y install software-properties-common  
RUN add-apt-repository ppa:webupd8team/java  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | sudo /usr/bin/debconf-set-selections  
  
RUN apt-get update && apt-get clean  
RUN apt-get install -q -y git oracle-java8-installer oracle-java8-set-default
&& apt-get clean  
ADD http://mirrors.jenkins-ci.org/war/1.577/jenkins.war /opt/jenkins.war  
RUN chmod 644 /opt/jenkins.war  
ENV JENKINS_HOME /jenkins  
  
ENTRYPOINT ["java", "-jar", "/opt/jenkins.war"]  
EXPOSE 8080  
CMD [""]  

