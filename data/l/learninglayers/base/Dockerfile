# Current Ubuntu LTS image  
FROM ubuntu:16.04  
# Let the container know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# Make sure that bash (not dash) is the default shell  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# Set the locale  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
# Perform updates  
RUN sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list  
RUN apt-get update \  
&& apt-get upgrade \  
-qqy \   
\--no-install-recommends \  
\--only-upgrade  
RUN apt-get install -qqy curl wget vim-nox zsh  
RUN wget -O /root/.zshrc http://git.grml.org/?p=grml-etc-
core.git;a=blob_plain;f=etc/zsh/zshrc;hb=HEAD  

