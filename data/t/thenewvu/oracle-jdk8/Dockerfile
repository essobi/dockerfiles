FROM thenewvu/ubuntu-14.04  
MAINTAINER Vu Le <thenewvu@gmail.com>  
  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | sudo
debconf-set-selections  
RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | sudo debconf-
set-selections  
  
RUN sudo add-apt-repository ppa:webupd8team/java && \  
sudo apt-get update && \  
sudo apt-get install -y --no-install-recommends oracle-java8-installer  
  
RUN sudo apt-get clean && \  
sudo rm -rf /var/lib/apt/lists/*  

