FROM vfarcic/jenkins-swarm-agent:latest  
  
USER root  
  
RUN apk --update --no-cache add curl openjdk8  
  
RUN curl -o apache-maven-3.5.2-bin.tar.gz
http://mirror.dsrg.utoronto.ca/apache/maven/maven-3/3.5.2/binaries/apache-
maven-3.5.2-bin.tar.gz  
RUN tar xzfv /apache-maven-3.5.2-bin.tar.gz -C /  
  
RUN pip install awscli  
  
RUN mkdir -p /root/.docker  
COPY config.json /root/.docker/  
#COPY docker-credential-ecr-login /usr/local/bin/  
#RUN chmod a+x /usr/local/bin/docker-credential-ecr-login  
#COPY artifactory-settings.xml /var/lib/jenkins/artifactory-settings.xml

