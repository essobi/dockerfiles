FROM ubuntu:xenial  
  
# install python packages  
RUN apt-get update && apt-get -y install\  
python \  
vim\  
build-essential\  
python-software-properties\  
software-properties-common\  
python-pip\  
python-dev  
  
# Add all scripts in bin to root directory of image  
ADD ./bin /  

