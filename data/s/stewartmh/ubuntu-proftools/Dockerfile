FROM ubuntu:17.10  
LABEL maintainer="Stewart Martin-Haugh <smh@cern.ch>"  
  
USER root  
  
#RUN adduser gks  
#RUN usermod -aG wheel gks  
#COPY wheel /etc/sudoers.d/wheel  
#  
RUN apt update  
RUN apt install -y sudo strace  
RUN apt install -y emacs vim nano gedit  
RUN apt install -y g++ clang  
RUN apt install -y valgrind  
RUN apt install -y linux-tools-common  
RUN apt install -y kcachegrind  
RUN apt install -y google-perftools  
RUN apt install -y x11-apps  
RUN apt install -y git  
RUN apt install -y libjemalloc1 libjemalloc-dev massif-visualizer  
RUN git clone https://github.com/StewMH/OptimisationWorkshop.git  

