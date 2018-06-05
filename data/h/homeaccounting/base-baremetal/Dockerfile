FROM ubuntu:16.04  
  
MAINTAINER Alexander Sidorenko <aleks.sidorenko@gmail.com>  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
  
# Base utilities  
RUN apt-get update && apt-get -y upgrade \  
&& apt-get -y -qq install curl unzip wget  
  
# Define default command.  
CMD ["bash"]

