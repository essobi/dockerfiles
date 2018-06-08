FROM debian:testing  
MAINTAINER Robotic-Brain <images.docker@roboticbrain.de>  
  
RUN apt-get update -qq -y \  
&& apt-get install cmake g++ git -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  

