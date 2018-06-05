#  
# Lynx Dockerfile  
#  
# \------------------------------------------------------------------  
# BUILD: docker build --pull=true \--rm=true -t mdixzge2md/lynx:latest .  
# \------------------------------------------------------------------  
#  
# \------------------------------------------------------------------  
# RUN : docker run -it --rm=true mdixzge2md/lynx:latest  
#  
# Flags: -i : running interactively  
# -t : giving a terminal  
# \--rm : remove conatainer when shutting down  
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
lynx \  
&& rm -rf /var/lib/apt/lists/*  
  
# \------------------------------------------------------------------  
# Wrapping up  
# \------------------------------------------------------------------  
  
ENTRYPOINT ["lynx"]  

