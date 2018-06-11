FROM circleci/ruby:2.3.6-node-browsers  
  
RUN sudo apt-get update -qqy \  
&& sudo apt-get install -qqy \  
qt5-default \  
libqt5webkit5-dev \  
gstreamer1.0-plugins-base \  
gstreamer1.0-tools \  
gstreamer1.0-x \  
python-dev  
  
RUN curl  -o ~/get-pip.py https://bootstrap.pypa.io/get-pip.py  
RUN sudo python ~/get-pip.py  
RUN sudo pip install awscli \--upgrade  

