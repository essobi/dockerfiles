FROM ubuntu:latest  
MAINTAINER Ryan Marr version 0.1  
#Replace default command interpreter from sh to bash  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
#update apt-get  
RUN apt-get update  
  
#install git  
RUN apt-get -y install git  
  
#Install curl  
RUN apt-get -y install curl  
  
#Install Wget  
RUN apt-get -y install wget  
  
#Install torch7  
RUN cd ~/  
RUN curl -s https://raw.githubusercontent.com/torch/ezinstall/master/install-
deps | bash  
RUN git clone https://github.com/torch/distro.git ~/torch --recursive  
RUN cd ~/torch; ./install.sh  
RUN source ~/.bashrc  
  
#Install google protocol buffer and loadcaffe  
RUN apt-get -y install libprotobuf-dev protobuf-compiler  
RUN luarocks install loadcaffe  
  
#Install neural-style  
RUN cd ~/  
RUN git clone https://github.com/jcjohnson/neural-style.git  
RUN cd neural-style  
RUN sh models/download_models.sh  
  

