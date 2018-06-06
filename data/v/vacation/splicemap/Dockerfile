From ubuntu:16.04  
# Docker for a fork of SpliceMap  
# see https://web.stanford.edu/group/wonglab/SpliceMap/tutorial.html  
# Copyright (c) 2010 Kin Fai Au and John Chong Mu  
# License in /Source/SpliceMap/LICENSE  
#set up environment  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y \  
git \  
&& apt-get autoremove \  
&& apt-get clean  
  
#set up software  
ENV REPO https://github.com/jason-weirather/SpliceMap.git  
RUN git clone $REPO /Source/SpliceMap \  
&& cd /Source/SpliceMap \  
&& cp /Source/SpliceMap/bin/* /usr/local/bin/  
  
VOLUME /temp  
VOLUME /output  
VOLUME /home  
ENV HOME /home  
WORKDIR /home  

