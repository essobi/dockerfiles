ARG DOCKER_VER=17.06  
FROM docker:${DOCKER_VER}  
  
RUN adduser -G root -D jenkins \  
&& apk --update --no-cache add openjdk8-jre python py-pip git openssh bash
build-base \  
&& pip install docker-compose  
  
#USER jenkins  
COPY swarm-client-3.3.jar /home/jenkins/swarm-client.jar  
COPY wait-for-it.sh /home/jenkins/wait-for-it.sh  
  
ARG DOCKER_VER  
ENV DVER ${DOCKER_VER}  
ENV JENKINS_USER_FILE "/run/secrets/jenkins_user"  
ENV JENKINS_PASSWORD_FILE "/run/secrets/jenkins_password"  
CMD /home/jenkins/wait-for-it.sh -t 0 jenkins:50000 -- java -jar
/home/jenkins/swarm-client.jar -username $(cat ${JENKINS_USER_FILE}) -password
$(cat ${JENKINS_PASSWORD_FILE}) -master http://jenkins:8080 -labels docker
-labels ${DVER} -fsroot /var/jenkins_workspace -executors 1  

