FROM centos:7  
  
USER root  
RUN yum -y install java-1.8.0-openjdk-devel maven git && yum clean all  
  
ENV JAVA_HOME /usr/lib/jvm/java-1.8.0  
  
ENV PATH "$PATH":/${JAVA_HOME}/bin:.:  
  
CMD git clone https://github.com/lorislab/clingo4j.git \  
&& cd clingo4j \  
&& mvn clean install  

