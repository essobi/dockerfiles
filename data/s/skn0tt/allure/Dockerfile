FROM ubuntu:xenial  
  
# Meta  
LABEL author = Simon Knott <info@simonknott.de>  
  
# Install Allure  
RUN apt-get update  
RUN apt-get install -y software-properties-common  
RUN apt-add-repository -y ppa:qameta/allure  
RUN apt-get update  
RUN apt-get install -y allure  

