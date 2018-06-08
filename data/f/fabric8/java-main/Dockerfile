FROM fabric8/base-sti  
  
MAINTAINER iocanel@gmail.com  
LABEL io.openshift.s2i.scripts-url
https://raw.githubusercontent.com/fabric8io/java-main/master/.sti/bin/  
  
USER root  
  
RUN mkdir /opt/jolokia && curl -L
http://central.maven.org/maven2/org/jolokia/jolokia-jvm/1.2.3/jolokia-
jvm-1.2.3-agent.jar > /opt/jolokia/jolokia.jar  
  
USER jboss  
  
CMD ["/usr/bin/usage"]  

