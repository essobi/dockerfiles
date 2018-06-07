FROM centos:centos7  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="rpm-builder" \  
org.label-schema.description="Centos 7 image with utils for builds packages in
rpm" \  
org.label-schema.url="http://andradaprieto.es" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/jandradap/rpm-builder" \  
org.label-schema.vendor="Jorge Andrada Prieto" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0" \  
maintainer="Jorge Andrada Prieto <jandradap@gmail.com>" \  
org.label-schema.docker.cmd=""  
  
RUN yum makecache fast \  
&& yum -y --setopt=tsflags=nodocs install \  
rpm-build \  
rpmdevtools \  
rpmlint \  
make \  
gcc \  
&& yum clean all \  
&& touch ~/.rpmmacros  
  
WORKDIR /root  

