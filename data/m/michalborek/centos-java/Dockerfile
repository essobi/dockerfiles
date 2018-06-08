FROM jboss/base-jdk:8  
MAINTAINER Michal Borek <michal@greenpath.pl>  
  
USER root  
RUN yum update -y && \  
yum install -y wget && \  
yum clean all  
  
RUN useradd --system --shell /usr/sbin/nologin ms  
USER ms  
CMD [ -f /ms/config ] && . /ms/config ; java $MS_JAVA_OPTS -jar
"/ms/${MS_JAR_NAME}"  

