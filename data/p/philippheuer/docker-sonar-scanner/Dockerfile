############################################################  
# Dockerfile  
############################################################  
  
# Extends: OpenJDK 8 (Alpine)  
FROM openjdk:8-jre-alpine  
  
# About the Maintainer  
MAINTAINER Philipp Heuer <docker@philippheuer.me>  
  
############################################################  
# Environment Configuration  
############################################################  
  
ENV CI_SERVER_URL="http://YOUR_GITLAB_INSTANCE/ci" \  
SYSTEM_USER="sonar-scanner" \  
WORKING_DIRECTORY="/opt/sonar-scanner" \  
DEBUG=false  
  
############################################################  
# Installation  
############################################################  
  
# Copy files from rootfs to the container  
ADD rootfs /  
  
# Install build only packages. These will be removed after installing the
packages. Notes:  
# * wget: to download files  
# * unzip: to extract downloaded files  
ENV BUILD_PACKAGES="\  
wget \  
unzip \  
"  
  
# Install packages. Notes:  
# * git: a git client to check out repositories  
ENV PACKAGES="\  
git \  
"  
  
RUN echo "Installing Packages ..." &&\  
# File Permissions  
mkdir -p $WORKING_DIRECTORY &&\  
chmod +x /tmp/* &&\  
chmod +x /usr/local/bin/sonar-scanner-* &&\  
# Add System User (SystemUser, Disable Password, Shell, Home Directory)  
adduser "$SYSTEM_USER" -S -D -s "/bin/sh" -h "$WORKING_DIRECTORY" &&\  
# Update Package List  
apk add --update &&\  
# Build Dependencies: Install  
apk add --virtual .build-deps --no-cache $BUILD_PACKAGES &&\  
# Package Install [no-cache, because the cache would be within the build -
bloating up the file size]  
apk add --no-cache $PACKAGES &&\  
# Custom Packages  
/tmp/sonar-scanner.sh  
  
# Build CleanUp  
## Removes all packages that have been flagged as build dependencies  
RUN echo "CleanUp ..." &&\  
apk del .build-deps &&\  
rm -rf /var/cache/apk/*  
  
############################################################  
# Execution  
############################################################  
  
# Working Directory  
WORKDIR "$WORKING_DIRECTORY"  

