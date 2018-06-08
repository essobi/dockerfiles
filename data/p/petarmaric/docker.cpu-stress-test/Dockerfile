FROM ubuntu:12.04  
MAINTAINER Petar Maric <petarmaric@uns.ac.rs>  
  
# Fix Docker-specific Ubuntu issues  
# (see https://journal.paul.querna.org/articles/2013/10/15/docker-ubuntu-on-
rackspace/ for details)  
ENV DEBIAN_FRONTEND noninteractive  
ENV INITRD No  
  
# Remember not to upgrade Ubuntu packages using 'apt-get upgrade', as it's no  
# longer considered to be a part of Dockerfile best practices  
# (see http://crosbymichael.com/dockerfile-best-practices-take-2.html for
details)  
# Update the Ubuntu package index and install the required Ubuntu packages  
RUN apt-get update && apt-get install -y \  
stress  
  
# Parameterize this Dockerfile, by storing the app configuration within
environment variables  
ENV STRESS_SYSTEM_FOR 5m  
ENV MAX_CPU_CORES 1  
CMD stress --cpu $MAX_CPU_CORES \--timeout $STRESS_SYSTEM_FOR  

