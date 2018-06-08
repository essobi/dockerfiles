FROM objectstyle/java8:latest  
  
MAINTAINER Andrus Adamchik <andrus at objectstyle dot com>  
  
LABEL name=objectstyle-maven3  
  
RUN yum -y install tar; yum -y install git  
RUN yum -y update; yum clean all  
  
ENV MAVEN_VERSION 3.3.3  
RUN curl -fsSL
http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C /usr/share \  
&& mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
ENV MAVEN_HOME=/usr/share/maven  
ENV PATH=${MAVEN_HOME}/bin:${PATH}  
  
RUN mkdir -p /root/work/  
WORKDIR /root/work/  
  
RUN mkdir /root/.ssh/  
RUN mkdir /root/.m2/  
  
CMD ["/bin/bash"]

