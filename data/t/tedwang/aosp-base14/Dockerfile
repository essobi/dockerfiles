FROM ubuntu:14.04  
  
MAINTAINER tedwang.tw@gmail.com  
  
#  
# fundamental packages  
#  
RUN apt-get update \  
&& apt-get install -y curl vim git man-db  
RUN apt-get install -y make  
# optional  
#RUN apt-get install -y wget  
#  
# AOSP requirement depends on android versions  
#  
# toolchains  
RUN apt-get install -y bison g++-multilib gperf libxml2-utils python-networkx
zlib1g-dev zip && apt-get clean  

