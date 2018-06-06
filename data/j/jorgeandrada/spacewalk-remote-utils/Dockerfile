FROM centos:7  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="spacewalk-remote-utils" \  
org.label-schema.description="Image centos 7 with ansible for CI test" \  
org.label-schema.url="http://andradaprieto.es" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/jandradap/spacewalk-remote-utils"
\  
org.label-schema.vendor="Jorge Andrada Prieto" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0" \  
maintainer="Jorge Andrada Prieto <jandradap@gmail.com>" \  
org.label-schema.docker.cmd="docker run -it jorgeandrada/spacewalk-remote-
utils bash"  
  
RUN rpm -ivh http://yum.spacewalkproject.org/2.7/RHEL/7/x86_64/spacewalk-
repo-2.7-2.el7.noarch.rpm \  
&& yum makecache fast \  
&& yum install -y spacewalk-remote-utils \  
&& yum clean all  

