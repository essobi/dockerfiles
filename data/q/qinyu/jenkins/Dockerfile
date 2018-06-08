FROM jenkins/jenkins:lts-alpine  
ARG VERSION=lts-alpine  
  
LABEL version=$VERSION \  
maintainer="qinyusuain@gmail.com"  
  
ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false"  
COPY security.groovy /usr/share/jenkins/ref/init.groovy.d/security.groovy  
  
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt  
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt  
  
USER root  
RUN apk add --no-cache docker shadow sudo  
  
COPY grant-jenkins-access-to-docker-socket.sh /usr/local/bin/grant-jenkins-
access-to-docker-socket.sh  
COPY jenkins-with-docker.sh /usr/local/bin/jenkins-with-docker.sh  
  
ENTRYPOINT [ "/bin/tini", "--", "/usr/local/bin/jenkins-with-docker.sh" ]

