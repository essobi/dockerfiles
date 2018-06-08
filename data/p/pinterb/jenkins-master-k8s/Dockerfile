FROM jenkins:2.19.3  
  
MAINTAINER Brad Pinter <brad.pinter@gmail.com>  
  
# Metadata params  
ARG VCS_URL  
ARG VCS_REF  
ARG BUILD_DATE  
ARG VERSION  
  
# Metadata  
LABEL org.label-schema.name="Jenkins Master k8s" \  
org.label-schema.description="A Jenkins master that is configured to integrate
with Kubernetes." \  
org.label-schema.vendor="CDW" \  
org.label-schema.url="https://cdw.com" \  
org.label-schema.vcs-url=$VCS_URL \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.version=$VERSION \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.schema-version="1.0.0-rc.1"  
RUN /usr/local/bin/install-plugins.sh kubernetes:0.9 workflow-aggregator:2.4
credentials:2.1.10 credentials-binding:1.10 docker-workflow:1.9.1 \  
ghprb:1.33.2 git:3.0.1 github:1.24.0 pipeline-build-step:2.4 pipeline-stage-
view:2.3 workflow-cps-global-lib:2.5 && \  
mkdir -p /usr/share/jenkins/ref/secrets/ && \  
echo "false" > /usr/share/jenkins/ref/secrets/slave-to-master-security-kill-
switch  

