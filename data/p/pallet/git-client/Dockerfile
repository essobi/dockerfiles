# Add a git client to the base image  
FROM ubuntu:latest  
MAINTAINER Hugo Duncan <hugo@palletops.com>  
  
# Add git client  
RUN apt-get -qq update && apt-get install --no-install-recommends -qqy \  
curl \  
ca-certificates \  
git  

