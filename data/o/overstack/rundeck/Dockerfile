FROM centos:centos6  
MAINTAINER SHS  
  
RUN yum -y install epel-release && rpm -Uvh http://repo.rundeck.org/latest.rpm
&& yum -y update  
  
RUN yum -y -q install java-1.7.0-openjdk ansible sshpass openssh-clients git
rundeck && yum clean all  
  
RUN curl -o /var/lib/rundeck/libext/rundeck-hipchat-plugin-1.5.0.jar
http://search.maven.org/remotecontent?filepath=com/hbakkum/rundeck/plugins/rundeck-
hipchat-plugin/1.5.0/rundeck-hipchat-plugin-1.5.0.jar  
  
EXPOSE 4440 4443  
CMD CMD source /etc/rundeck/profile && ${JAVA_HOME:-/usr}/bin/java
${RDECK_JVM} -cp ${BOOTSTRAP_CP} com.dtolabs.rundeck.RunServer
/var/lib/rundeck ${RDECK_HTTP_PORT}  

