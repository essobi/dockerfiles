FROM dwolla/jenkins-agent-core:debian  
MAINTAINER Dwolla Dev <dev+jenkins-chef-tools@dwolla.com>  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VCS_URL  
ARG VERSION  
  
LABEL \  
maintainer="Dwolla Dev <dev+jenkins-chef-tools@dwolla.com>" \  
org.label-schema.build-date=${BUILD_DATE} \  
org.label-schema.name="dwolla/jenkins-agent-chef Dockerfile" \  
org.label-schema.schema-version="1.0" \  
org.label-schema.vcs-ref="${VCS_REF}" \  
org.label-schema.vcs-url="${VCS_URL}" \  
org.label-schema.version="${VERSION}"  
  
USER root  
  
ENV CHEFDK_VERSION=1.6.11  
  
RUN apt-get install -y \  
ruby && \  
curl -O
https://packages.chef.io/files/stable/chefdk/${CHEFDK_VERSION}/ubuntu/16.04/chefdk_${CHEFDK_VERSION}-1_amd64.deb
&& \  
dpkg -i chefdk_${CHEFDK_VERSION}-1_amd64.deb && \  
rm -rf chefdk_${CHEFDK_VERSION}-1_amd64.deb  
  
USER jenkins  

