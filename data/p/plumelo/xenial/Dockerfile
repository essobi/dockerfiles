FROM ubuntu:16.04  
RUN apt-get clean && apt-get update -qq  
RUN apt-get install -y locales sudo autoconf build-essential python  
RUN locale-gen en_US.UTF-8  
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'  
RUN apt-get clean  
  

