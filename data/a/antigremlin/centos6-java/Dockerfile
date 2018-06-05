FROM centos:6  
ENV LANG=en_US.utf8  
RUN yum -y update && yum -y install tar && yum clean all  
  
RUN curl -s -L --header "Cookie: oraclelicense=accept-securebackup-cookie;" \  
http://download.oracle.com/otn-pub/java/jdk/8u66-b17/server-
jre-8u66-linux-x64.tar.gz \  
| tar xz -C /opt --no-same-owner  
  
ENV JAVA_HOME=/opt/jdk1.8.0_66  
ENV PATH=$PATH:$JAVA_HOME/bin  

