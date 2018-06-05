# Create an image with Beast ( Beast-mcmc, not Beast 2) and Beagle intalled.  
#  
# This Dockerfile will compile and install both Beast and  
# Beagle from the latest sources available on gitub. The instructions  
# for compiling and installing Beagle are taken from the README on the  
# Beagle githib reop. Installation of Beast is derived from long  
# experience building and installing Beast from sources.  
#  
# To build a docker image,  
# $ cd <directory_with_Dockerfile>  
# $ docker build --tag=cwarth/beastandbeagle .  
#  
# To run the resulting docker image,  
# $ docker run --name beast_and_beagle --rm -it cwarth/beastandbeagle bash  
#  
# In the docker client,  
# # beast -beagle beast_config.xml  
#  
FROM java:7  
WORKDIR /tmp  
MAINTAINER Chris Warth cwarth@fredhutch.org  
  
RUN apt-get update -qq  
RUN apt-get dist-upgrade -y  
RUN apt-get update  
# RUN apt-get install -y apt-utils  
ENV HOME /root  
WORKDIR ${HOME}  
  
ADD Dockerfile ${HOME}/Dockerfile  
  
# Install tools needed to compile Beast and Beagle.  
#  
RUN apt-get update  
RUN apt-get install -y ant build-essential autoconf automake libtool
subversion pkg-config  
  
# Clean-up  
RUN apt-get -y autoremove  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN which gcc  
RUN gcc --version  
  
# Clone and compile Beagle from sources  
RUN git clone \--depth=1 https://github.com/beagle-dev/beagle-lib.git  
WORKDIR ${HOME}/beagle-lib  
RUN ./autogen.sh  
RUN ./configure --disable-sse --disable-march-native --prefix=/usr/local  
RUN make install  
#RUN rm -rf ${HOME}/beagle-lib  
# Clone and install Beast from sources  
WORKDIR ${HOME}  
RUN git clone https://github.com/beast-dev/beast-mcmc.git  
WORKDIR ${HOME}/beast-mcmc  
RUN ant linux  
RUN mv ${HOME}/beast-mcmc/release/Linux/BEASTv1.8.3pre ${HOME}/  
#RUN rm -rf ${HOME}/beast-mcmc  
# this leaves the compiled BEAST jar file in ${HOME}/BEASTv1.8.3pre/  
# set prompt inside docker image  
RUN echo 'export PS1="[docker \u@cwarth/hiv-sim] \W # "' >> ${HOME}/.bashrc  
  
# make beagle libraries and Beast script accessible  
RUN echo 'export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH' >>
${HOME}/.bashrc  
ENV LD_LIBRARY_PATH /usr/local/lib:${LD_LIBRARY_PATH}  
  
# make beast scripts accessilbe on PATH  
RUN echo 'export PATH=BEASTv1.8.3pre/bin:$PATH' >> ${HOME}/.bashrc  
  
# Verify that beast runs and that it can use beagle.  
#RUNS beast -beagle_info  
ADD beast_in.xml ${HOME}/beast_in.xml  
  
# leave the docker image in a known state...  
WORKDIR ${HOME}  
  
CMD BEASTv1.8.3pre/bin/beast -beagle beast_in.xml  
  

