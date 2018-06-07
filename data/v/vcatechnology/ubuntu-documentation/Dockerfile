FROM vcatechnology/ubuntu-ci  
MAINTAINER VCA Technology <developers@vcatechnology.com>  
  
# Build-time metadata as defined at http://label-schema.org  
ARG PROJECT_NAME  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="$PROJECT_NAME" \  
org.label-schema.description="A Ubuntu docker image that is used in the VCA
Technology continuous integration infrastructure to build documentation" \  
org.label-schema.url="https://www.ubuntu.com/" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/vcatechnology/docker-ubuntu-
documentation" \  
org.label-schema.vendor="VCA Technology" \  
org.label-schema.version=$VERSION \  
org.label-schema.license=MIT \  
org.label-schema.schema-version="1.0"  
  
# Install useful packages  
RUN sudo vca-install-package \  
python-pandocfilters \  
pylint \  
pandoc \  
build-essential \  
jq \  
texlive-base \  
texlive-xetex  
  

