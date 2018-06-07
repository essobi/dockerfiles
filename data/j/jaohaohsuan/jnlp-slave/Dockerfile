FROM openjdk:8-jdk-alpine  
  
RUN sed -i 's/\/root/\/home\/jenkins/g' /etc/passwd && mkdir -p /home/jenkins  
  
RUN apk --no-cache add curl \  
docker \  
bash \  
ansible \  
git \  
vim \  
openssh-client  
  
LABEL Description="This is a base image, which provides the Jenkins agent
executable (slave.jar)" Vendor="Jenkins project" Version="3.7"  
  
ARG VERSION=3.7  
RUN curl --create-dirs -sSLo /usr/share/jenkins/slave.jar
https://repo.jenkins-ci.org/public/org/jenkins-
ci/main/remoting/${VERSION}/remoting-${VERSION}.jar \  
&& chmod 755 /usr/share/jenkins \  
&& chmod 644 /usr/share/jenkins/slave.jar  
  
RUN mkdir -p /home/jenkins/.jenkins  
VOLUME ["/home/jenkins/.jenkins"]  
WORKDIR /home/jenkins  
  
COPY jenkins-slave /usr/local/bin/jenkins-slave  
ENV JAVA_OPTS="-Xms256m -Xmx256m -XX:PermSize=64M -XX:MaxPermSize=128M"  
ENTRYPOINT ["jenkins-slave"]  

