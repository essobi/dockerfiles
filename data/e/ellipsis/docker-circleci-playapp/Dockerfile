FROM frolvlad/alpine-scala:2.12  
MAINTAINER Matteo Melani <m@ellipsis.ai>  
  
# Install some basic tools  
RUN apk add --update bash curl openssl ca-certificates tar gzip openssh zip  
  
# Install activator  
ENV ACTIVATOR_VERSION 1.3.10  
RUN curl -L -o /tmp/activator.zip \  
https://downloads.typesafe.com/typesafe-
activator/${ACTIVATOR_VERSION}/typesafe-
activator-${ACTIVATOR_VERSION}-minimal.zip && \  
mkdir -p /opt/activator && \  
unzip /tmp/activator.zip -d /opt/activator && \  
rm /tmp/activator.zip && \  
chmod +x /opt/activator/activator-${ACTIVATOR_VERSION}-minimal/bin/activator
&& \  
ln -s /opt/activator/activator-${ACTIVATOR_VERSION}-minimal/bin/activator
/usr/bin/activator && \  
rm -rf /tmp/* /var/cache/apk/*  
  
# Git  
RUN apk add --update git  
  
# Node and Npm  
RUN apk add --update nodejs nodejs-npm && npm install npm@latest -g  
  
# Docker and docker compose  
RUN apk add --update docker  
  
# AWS CLI tools  
RUN apk --no-cache update && \  
apk --no-cache add python py-pip py-setuptools ca-certificates && \  
pip --no-cache-dir install awscli && \  
rm -rf /var/cache/apk/*  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
  
RUN addgroup -S circleci && adduser -S -g circleci circleci  
RUN passwd -d -u circleci  
RUN echo "circleci ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers  
  
USER circleci  

