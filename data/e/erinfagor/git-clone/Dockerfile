# Version: 0.0.2  
FROM ubuntu  
MAINTAINER Ertinfagor <abereznik@gmail.com>  
  
#GitHub User  
ARG USER  
# GitHub Repository name  
ARG REPONAME  
  
RUN apt-get update  
RUN apt-get install -y git  
CMD cd /vol/ && mkdir $REPONAME && cd $REPONAME && git clone
https://github.com/$USER/$REPONAME.git  

