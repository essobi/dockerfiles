FROM bwits/base-centos6-puppet  
  
MAINTAINER Bill W  
  
ENV JAVA_VERSION=1.7.0  
ENV RUNDECK_VERSION=2.6.0-1.11.GA  
  
RUN puppet resource package java-${JAVA_VERSION}-openjdk ensure=latest  
RUN puppet resource yumrepo bintray-rundeck
baseurl='http://dl.bintray.com/rundeck/rundeck-rpm/' descr='bintray rundeck
repo' enabled='1' gpgcheck='0' priority='1'  
RUN puppet resource package rundeck ensure=${RUNDECK_VERSION}  
RUN puppet resource package wget ensure=latest  
  
RUN wget https://github.com/rundeck-plugins/rundeck-ec2-nodes-
plugin/releases/download/1.5/rundeck-ec2-nodes-plugin-1.5.jar -O
/var/lib/rundeck/libext/rundeck-ec2-nodes-plugin-1.5.jar  
CMD source /etc/rundeck/profile && ${JAVA_HOME:-/usr}/bin/java ${RDECK_JVM}
-cp ${BOOTSTRAP_CP} com.dtolabs.rundeck.RunServer /var/lib/rundeck
${RDECK_HTTP_PORT}  

