##########################################  
## Sourcemod CI Dockerfile ##  
## ##  
## Written by Kevin 'RAYs3T' Urbainczyk ##  
## Creates a build environment for SM ##  
##########################################  
FROM debian:stretch  
  
LABEL maintainer=rays3t  
LABEL version="1.2.2"  
LABEL description="A docker container based on debian/stretch for building
sourcemod plugins (.sp).\  
This is intended to be used in an CI environment like GitLab. \  
It also adds a little wrapper script for the spcomp that abstracts the
sourcemod libs from your plugin ones"  
  
# Create the new builder group  
RUN groupadd -r smbuild  
  
# Create the user (as system user(-r), auto creating home directory(-m))  
# and adds it to the created group (-g)  
RUN useradd -m -r -g smbuild smuser  
  
# Add x86 support  
RUN dpkg --add-architecture i386  
# Update apt repos and install required dependencies  
# According to: https://wiki.alliedmods.net/Building_sourcemod#Linux  
RUN apt update  
# Add git support  
RUN apt install -y git wget zip tar libc6:i386 lib32z1 lib32z1-dev
libc6-dev-i386 libc6-i386 curl p7zip-full  
  
# Copy the modified compiler script  
COPY compile.sh /home/smuser/compile.sh  
  
# Make the compiler script executable and create a global comannd for it  
RUN chmod 755 /home/smuser/compile.sh && ln -s /home/smuser/compile.sh
/usr/bin/spcomp  
  
# Change the user  
USER smuser  
  
WORKDIR /home/smuser  
  
# Pull the latest stable sourcemod version  
RUN BASE_SM_DL_URL=http://www.sourcemod.net/smdrop/1.8 && \  
LATEST_SM_VERSION=`wget $BASE_SM_DL_URL/sourcemod-latest-linux -q -O -` && \  
echo Detected sourcemod version: $LATEST_SM_VERSION && \  
wget -qO sourcemod.tar.gz $BASE_SM_DL_URL/$LATEST_SM_VERSION  
  
# Create the sourcemod directory and extract the downloaded archive into it  
# This will create a sourcemod instance in "/home/smuser/sourcemod",  
# that is ready for compiling code  
RUN mkdir sourcemod && \  
tar xvzf sourcemod.tar.gz -C sourcemod  
  
  
# Create the build directory  
RUN mkdir /home/smuser/build  
  
# Finnaly switch to that directory  
WORKDIR /home/smuser/build

