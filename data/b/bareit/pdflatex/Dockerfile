FROM ubuntu:latest  
MAINTAINER Thomas Stainer <stainer.tom@gmail.com>  
  
# Build-time metadata as defined at http://label-schema.org  
ARG PROJECT_NAME  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="$PROJECT_NAME" \  
org.label-schema.description="Ubuntu docker image with pdflatex" \  
org.label-schema.url="" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/thomasms/docker-pdflatex" \  
org.label-schema.vendor="Thomas Stainer" \  
org.label-schema.version=$VERSION \  
org.label-schema.license="MIT" \  
org.label-schema.schema-version="1.0"  
# Install additional packages  
RUN apt-get \--yes update && \  
apt-get \--yes upgrade && \  
apt-get \--yes install texlive texlive-latex-recommended texlive-latex-extra
&& \  
apt-get \--yes install git ssh  
  

