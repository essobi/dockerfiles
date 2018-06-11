FROM ubuntu  
MAINTAINER Alexis MP "alexis.mp@gmail.com"  
# download and install OpenCV dependencies  
ADD http://commondatastorage.googleapis.com/alexismp-docker-opencv-
demo%2Fopencv-2.4.7.tar.gz /opt/opencv-2.4.7.tar.gz  
RUN tar -xvf /opt/opencv-2.4.7.tar.gz -C /opt/  
RUN rm /opt/opencv-2.4.7.tar.gz  
  
ADD http://commondatastorage.googleapis.com/alexismp-docker-opencv-
demo%2FfaceDetect.tar.gz /home/faceDetect.tar.gz  
RUN tar -xvf /home/faceDetect.tar.gz -C /home/  
RUN rm /home/faceDetect.tar.gz  
  
# Update list of packages  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
RUN apt-get update  
  
# Fake a fuse install (or openjdk-7-jdk will not install)  
RUN apt-get install libfuse2  
RUN cd /tmp ; apt-get download fuse  
RUN cd /tmp ; dpkg-deb -x fuse_* .  
RUN cd /tmp ; dpkg-deb -e fuse_*  
RUN cd /tmp ; rm fuse_*.deb  
RUN cd /tmp ; echo -en '#!/bin/bash\nexit 0\n' > DEBIAN/postinst  
RUN cd /tmp ; dpkg-deb -b . /fuse.deb  
RUN cd /tmp ; dpkg -i /fuse.deb  
  
# install Java and Ant  
RUN apt-get install -y openjdk-7-jdk  
RUN apt-get install -y ant  
  
# set a bunch of environment variables  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64/  
ENV PATH $JAVA_HOME/bin:$PATH  
ENV LD_LIBRARY_PATH /opt/opencv-2.4.7/build/lib/  
  
# run default detect face job  
CMD ["cd", "/home/faceDetect"]  
CMD ["ant", "build"]  

