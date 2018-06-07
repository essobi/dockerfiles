FROM ubuntu:wily  
  
MAINTAINER Manuel Ryan <ryan@shamu.ch>  
  
# Switch back to ARG once docker hub will be running docker >= 1.9  
ENV maven_repo=http://central.maven.org/maven2  
ENV npm_repo=https://registry.npmjs.org/  
  
ADD install.sh /install.sh  
RUN chmod +x /install.sh  
RUN /install.sh  
  
VOLUME /sources  
VOLUME /dependencies  
VOLUME /output  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
ENV JAVADOC_ARGS -skipUiFiles  
  
ADD run.sh /run.sh  
RUN chmod +x /run.sh  
CMD /run.sh  

