FROM ubuntu:trusty  
  
RUN apt-get update && apt-get install -y -qq unzip && apt-get clean && rm -rf
/var/lib/apt/lists/*  
  
ADD https://bitbucket.org/osrf/gazebo_models/get/73f89ecb1622.zip /tmp/  
  
RUN mkdir ~/.gazebo && unzip /tmp/73f89ecb1622.zip -d ~/.gazebo && mv
~/.gazebo/osrf-gazebo_models-73f89ecb1622 ~/.gazebo/models && rm
/tmp/73f89ecb1622.zip  

