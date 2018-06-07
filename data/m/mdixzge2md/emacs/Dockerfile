#  
# Emacs Dockerfile  
#  
# \------------------------------------------------------------------  
# BUILD: docker build --rm=true -t mdixzge2md/<name>:latest .  
# \------------------------------------------------------------------  
#  
# \------------------------------------------------------------------  
# RUN : docker run [flags] mdixzge2md/<name>:latest [cmd]  
#  
# Flags: -d : running as daemon  
# -i : running interactively  
# -t : giving a terminal  
# \--rm : remove conatainer when shutting down  
# -v : mapping host volumes to container volumes  
# -e : setting environment varialbes  
#  
# Cmd: /bin/bash : giving a shell to attach to  
#  
# \------------------------------------------------------------------  
#  
# \------------------------------------------------------------------  
# Boilerplate header  
# \------------------------------------------------------------------  
  
# What base image to work from  
FROM debian:jessie  
  
# Who to whine to ...  
MAINTAINER mdixzge2md <greyjoy@protonmail.com>  
  
# \------------------------------------------------------------------  
# Getting the base system dependencies and cleaning cache afterwards  
# \------------------------------------------------------------------  
  
RUN apt-get update -qq && apt-get install -qqy \  
dbus-x11 \  
emacs24 \  
&& rm -rf /var/lib/apt/lists/*  
  
# \------------------------------------------------------------------  
# Wrapping up  
# \------------------------------------------------------------------  
  
CMD ["emacs"]  
  

