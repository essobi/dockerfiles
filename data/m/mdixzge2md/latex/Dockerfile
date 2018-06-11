#  
# Latex Dockerfile  
#  
# \------------------------------------------------------------------  
# BUILD: docker build --pull=true \--rm=true -t mdixzge2md/latex:latest .  
# \------------------------------------------------------------------  
#  
# \------------------------------------------------------------------  
# RUN : docker run -it --rm=true -v <host source>:/latex_source  
# mdixzge2md/latex:latest /bin/bash  
#  
# Flags: -i : running interactively  
# -t : giving a terminal  
# \--rm=true : remove conatainer when shutting down  
# -v : mapping host volumes to container volume  
#  
# Cmd: /bin/bash : giving a shell to attach to  
#  
# \------------------------------------------------------------------  
#  
# \------------------------------------------------------------------  
# Boilerplate header  
# \------------------------------------------------------------------  
  
# What base image to work from  
FROM debian:stable  
  
# Who to whine to ...  
MAINTAINER mdixzge2md <greyjoy@protonmail.com>  
  
# \------------------------------------------------------------------  
# Getting the base system dependencies and cleaning cache afterwards  
# \------------------------------------------------------------------  
  
RUN apt-get update -yqq && apt-get install -yqq --no-install-recommends \  
texlive-full \  
texlive-math-extra \  
texlive-pictures \  
texlive-science \  
&& rm -rf /var/lib/apt/lists/*  
  
# \------------------------------------------------------------------  
# Get additional modules  
# \------------------------------------------------------------------  
  
  
# \------------------------------------------------------------------  
# Setting up the workspace  
# \------------------------------------------------------------------  
VOLUME ["/latex_source"]  
  
WORKDIR latex_source  
  
# \------------------------------------------------------------------  
# Wrapping up and setting start environment  
# \------------------------------------------------------------------  

