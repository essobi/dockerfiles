FROM circleci/ruby:2.4.1-node-browsers  
  
USER root  
  
RUN apt-get update  
RUN apt-get install qt5-default libqt5webkit5-dev gstreamer1.0-plugins-base
gstreamer1.0-tools gstreamer1.0-x  
RUN sudo npm install bower -g  
RUN echo "/opt/qt5/bin/qt5-env.sh" >> ~/.circlerc  
  
USER circleci  

