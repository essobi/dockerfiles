FROM duffqiu/dockerjdk7  
  
  
RUN rpm --import http://mirror.centos.org/centos/RPM-GPG-KEY-CentOS-7  
  
RUN yum -y update && yum -y install tar curl && yum clean all  
  
ENV MAVEN_VERSION 3.3.3  
RUN curl -fsSL
http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C /usr/share \  
&& mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
ENV MAVEN_HOME /usr/share/maven  
  
WORKDIR /workspace  
  
CMD ["mvn"]  

