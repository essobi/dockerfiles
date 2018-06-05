FROM jenkins:2.3  
  
# Give jenkins user the rights to import java certs  
# Need root permissions  
USER root  
RUN chmod a+w $JAVA_HOME/jre/lib/security/cacerts  
  
# switch to jenkins user  
ARG user=jenkins  
ENV JENKINS_OPTS \--httpsKeyStore=$JAVA_HOME/jre/lib/security/cacerts  
USER ${user}  
COPY jenkins.sh /usr/local/bin/jenkins.sh  

