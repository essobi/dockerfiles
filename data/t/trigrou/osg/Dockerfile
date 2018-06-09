FROM ubuntu:14.04.1  
MAINTAINER trigrou  
  
  
RUN apt-get -y update && apt-get -y install \  
cmake \  
freeglut3-dev \  
git \  
g++ \  
libjpeg-dev libtiff5-dev libpng12-dev \  
wget  
  
RUN echo "/usr/local/lib64/" >/etc/ld.so.conf.d/lib64.conf  
RUN echo "/usr/local/lib/" >/etc/ld.so.conf.d/lib.conf  
  
ENV LD_LIBRARY_PATH /usr/local/lib/:/usr/local/lib64/:  
  
RUN mkdir -p /usr/local/lib64/  
  
RUN mkdir /root/fbx && cd /root/fbx && wget
http://images.autodesk.com/adsk/files/fbx20142_1_fbxsdk_linux.tar.gz  
RUN cd /root/fbx && tar xvfz fbx20142_1_fbxsdk_linux.tar.gz && chmod +x
fbx20142_1_fbxsdk_linux  
RUN cd /root/fbx && eval 'echo -e "y\nyes\nyes" | ./fbx20142_1_fbxsdk_linux
./'  
RUN cp /root/fbx/lib/gcc4/x64/release/* /usr/local/lib64/ && rm -r /root/fbx/  
  
RUN cd /root/ && git clone https://github.com/cedricpinson/osg.git  
RUN mkdir -p /root/osg/build  
RUN cd /root/osg/build && FBX_DIR=/root/fbx/ cmake -DCMAKE_BUILD_TYPE=Release
../ && make install && rm -r /root/osg/  

