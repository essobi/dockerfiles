FROM centos/ruby-24-centos7  
  
ARG JAVA_VERSION=1.8.0  
ARG JAVA_VERSION_DETAIL=1.8.0.151  
ARG LANG=en_US.UTF-8  
ENV JAVA_HOME=/usr/lib/jvm/${JAVA_VERSION_DETAIL}/jre/  
  
USER root  
  
RUN yum -y --setopt=tsflags=nodocs update && \  
scl enable rh-ruby24 -- gem install listen && \  
scl enable rh-ruby24 -- gem install ascii_binder && \  
yum -y install java-${JAVA_VERSION}-openjdk-${JAVA_VERSION_DETAIL} && \  
yum clean all && \  
rm -rf /var/cache/yum  
  
LABEL url="http://www.asciibinder.org" \  
summary="a documentation system built on Asciidoctor" \  
description="AsciiBinder is for documenting versioned, interrelated projects.
Run this container image from the documentation repository, which is mounted
into the container. Note: Generated files will be owned by root." \  
RUN="docker run -it --rm \  
-v $(pwd):/usr/src/docs:z \  
IMAGE"  
LABEL org.opennms.java.version="openjdk-${JAVA_VERSION}-{JAVA_VERSION_DETAIL}"  
  
COPY ./docker-entrypoint.sh /  
  
WORKDIR /docs  
  
VOLUME ["/docs"]  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["--help"]  

