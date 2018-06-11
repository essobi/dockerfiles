FROM centos  
MAINTAINER VCA Technology <developers@vcatechnology.com>  
  
# Build-time metadata as defined at http://label-schema.org  
ARG PROJECT_NAME  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="$PROJECT_NAME" \  
org.label-schema.description="A CentOS image that is updated daily with new
packages" \  
org.label-schema.url="https://www.centos.org/" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/vcatechnology/docker-centos" \  
org.label-schema.vendor="VCA Technology" \  
org.label-schema.version=$VERSION \  
org.label-schema.license=MIT \  
org.label-schema.schema-version="1.0"  
  
# Update all packages  
RUN yum -y update && \  
yum clean all  
  
# install locale  
RUN localedef -c -f UTF-8 -i en_US en_GB.UTF-8  
ENV LANG=en_GB.UTF-8  
# Create install script  
RUN touch /usr/local/bin/vca-install-package && \  
chmod +x /usr/local/bin/vca-install-package && \  
echo '#! /bin/sh' >> /usr/local/bin/vca-install-package && \  
echo 'set -e' >> /usr/local/bin/vca-install-package && \  
echo 'yum -y --enablerepo=extras install $@' >> /usr/local/bin/vca-install-
package && \  
echo 'yum clean all' >> /usr/local/bin/vca-install-package  
  
# Create uninstall script  
RUN touch /usr/local/bin/vca-uninstall-package && \  
chmod +x /usr/local/bin/vca-uninstall-package && \  
echo '#! /bin/sh' >> /usr/local/bin/vca-uninstall-package && \  
echo 'set -e' >> /usr/local/bin/vca-uninstall-package && \  
echo 'yum -y remove $@' >> /usr/local/bin/vca-uninstall-package  
  
# Enable the packages for enterprise linux  
RUN vca-install-package epel-release  

