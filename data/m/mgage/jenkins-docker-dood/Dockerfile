FROM jenkinsci/blueocean:1.0.1  
  
ENV JENKINS_OPTS \--httpPort=-1 \--httpsPort=8443
\--httpsKeyStore=/var/jenkins_home/keystore \--httpsKeyStorePassword=password  
ENV DOCKER_UID 1005  
  
USER root  
ADD ca.pem .  
RUN apk --update add shadow docker==1.12.6-r0 && \  
groupmod docker -g $DOCKER_UID && \  
usermod -aG docker jenkins && \  
keytool -noprompt -storepass changeit -import -trustcacerts -file ca.pem
-alias CA_ALIAS -keystore $JAVA_HOME/jre/lib/security/cacerts  
  
USER jenkins  

