FROM fedora:26  
MAINTAINER VCA Technology <developers@vcatechnology.com>  
  
# Build-time metadata as defined at http://label-schema.org  
ARG PROJECT_NAME  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="$PROJECT_NAME" \  
org.label-schema.description="A Fedora image that has new packages installed
daily" \  
org.label-schema.url="https://getfedora.org/" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/vcatechnology/docker-fedora" \  
org.label-schema.vendor="VCA Technology" \  
org.label-schema.version=$VERSION \  
org.label-schema.license=MIT \  
org.label-schema.schema-version="1.0"  
  
# Create package scripts  
ADD vca-install-package /usr/local/bin  
ADD vca-uninstall-package /usr/local/bin  
  
# Set the locale  
RUN vca-install-package langpacks-en_GB  
ENV LANG=en_GB.UTF-8  
# Update all packages  
RUN dnf -qy --setopt=deltarpm=false update \  
&& dnf clean all --enablerepo=\\*  

