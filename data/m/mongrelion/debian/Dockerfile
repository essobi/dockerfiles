# Debian base image (based on Debian Stable)  
FROM debian:stable  
  
MAINTAINER Carlos León, mongrelion@dev-co.org  
  
# Update packages list every time the container is built.  
ONBUILD RUN apt-get update  
  
RUN apt-get update && apt-get -y install wget git  

