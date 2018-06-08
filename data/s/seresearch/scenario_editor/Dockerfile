FROM ubuntu:16.04  
  
RUN dpkg --add-architecture i386 && \  
apt-get update && \  
apt-get upgrade  
ADD ./ScUI/ /opt/ScenarioEditor  
  
RUN apt-get -y install openjdk-8-jdk:i386  
RUN update-java-alternatives -s java-1.8.0-openjdk-i386  
  
RUN apt-get -y install libswt-glx-gtk-3-jni:i386  
RUN cp /usr/lib/jni/libswt-glx-gtk-3836.so
/opt/ScenarioEditor/lib/linux/libswt-glx-gtk.so  

