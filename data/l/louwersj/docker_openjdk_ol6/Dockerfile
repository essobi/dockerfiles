FROM oraclelinux:6.9  
MAINTAINER Johan Louwers <louwersj@gmail.com>  
LABEL maintainer="louwersj@gmail.com"  
  
# Parse arguments for the build command.  
ARG VERSION  
ARG VCS_URL  
ARG VCS_REF  
ARG BUILD_DATE  
  
# A little bit of metadata management.  
# See http://label-schema.org/  
LABEL org.label-schema.schema-version="1.0" \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vendor="louwersj@gmail.com" \  
org.label-schema.version=$VERSION \  
org.label-schema.vcs-url=$VCS_URL \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.name="openJDK" \  
org.label-schema.description="Java OpenJDK 1.7.0 on Oracle Linux 6"  
  
RUN yum -y install java-1.7.0-openjdk-devel && yum clean all  
  
ENV JAVA_HOME /usr/lib/jvm/java-openjdk  
  
CMD ["java", "-version"]  

