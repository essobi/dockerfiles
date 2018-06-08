FROM ubuntu:14.04  
MAINTAINER Khaled Hassan <khaled.hassan@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV DEBCONF_NONINTERACTIVE_SEEN true  
  
RUN apt-get update && apt-get -y install \  
bison \  
build-essential \  
flex \  
# multilib packages added at the suggestion of
<http://stackoverflow.com/questions/5383325/how-to-create-a-32-bit-shared-
library-on-a-64-bit-platform-with-autotools>  
# and <http://godblesstangkk.blogspot.com/2013/01/install-simplescalar-30-on-
ubuntu-1204.html>  
gcc-multilib \  
g++-multilib  
  
# Step 2: Setting up the Environment  
ENV HOST i686-pc-linux  
ENV IDIR /simplescalar  
ENV TARGET sslittle-na-sstrix  
  
ADD . /simplescalar  
  
WORKDIR /simplescalar  
  
RUN /simplescalar/build.bash  
  
# Add compiled binaries to path after build  
ENV PATH $PATH:$IDIR/bin:$IDIR/simplesim-3.0  

