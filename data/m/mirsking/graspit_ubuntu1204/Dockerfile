FROM mirsking/ubuntu:12.04  
MAINTAINER Mirs King <mirsking@gmail.com>  
  
RUN apt-get -y install libqt4-dev libqt4-opengl-dev libqt4-sql-psql  
RUN apt-get -y install libsoqt4-dev  
RUN apt-get -y install libblas-dev  
RUN apt-get -y install liblapack-dev  
RUN apt-get -y install libqhull-dev  
RUN apt-get -y install libcoin60-dev  
  
RUN mkdir -p ~/graspit && cd ~/graspit && wget
http://downloads.sourceforge.net/project/graspit/releases/graspit-2.2.zip  
RUN apt-get -y install unzip build-essential  
RUN cd ~/graspit && unzip ~/graspit/graspit-2.2.zip  
RUN echo 'export GRASPIT=/root/graspit/Graspit' >> ~/.bashrc  
RUN cd ~/graspit/Graspit && qmake graspit.pro && make  
  
# Install vnc, xvfb in order to create a 'fake' display and firefox  
RUN apt-get install -y x11vnc xvfb firefox  
RUN mkdir ~/.vnc  
# Setup a password  
RUN x11vnc -storepasswd 1234 ~/.vnc/passwd  
# Autostart firefox (might not be the best way to do it, but it does the
trick)  
RUN bash -c 'echo "firefox" >> /.bashrc'

