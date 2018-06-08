FROM michaelpc/dind  
  
RUN apt-get update && apt-get install -y wget; wget -q -O -
http://pkg.jenkins-ci.org/debian-stable/jenkins-ci.org.key | apt-key add -;  
RUN echo "deb http://pkg.jenkins-ci.org/debian-stable binary/" >>
/etc/apt/sources.list; apt-get update; apt-get install gdebi-core jenkins -y  
RUN usermod -a -G docker jenkins  
  
ADD ./start-jenkins.sh /usr/local/bin/start-jenkins.sh  
RUN chmod +x /usr/local/bin/start-jenkins.sh  
  
ENV JENKINS_HOME /var/lib/jenkins  
  
EXPOSE 8080  
RUN apt-get install sudo -y  
  
RUN cpanm --notest TAP::Formatter::JUnit  
  
ENV SERVICE_START_JENKINS jenkins  

