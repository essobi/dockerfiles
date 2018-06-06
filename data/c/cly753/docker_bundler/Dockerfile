# start with a base image  
FROM ubuntu:14.04  
# install general tools  
RUN apt-get update \  
&& apt-get install -y \  
git wget python python-pip python2.7-dev unzip vim sed \  
zlib1g-dev jhead imagemagick libjpeg62-dev g++ \  
build-essential libblas-dev liblapack-dev libatlas-base-dev gfortran
libc6-i386 \  
&& apt-get clean  
  
# prepare bundler  
RUN pip install Pillow \  
&& wget -O bundler_sfm-master.zip
https://github.com/snavely/bundler_sfm/archive/master.zip \  
&& unzip bundler_sfm-master.zip \  
&& rm bundler_sfm-master.zip \  
&& mv bundler_sfm-master bundler_sfm \  
&& wget -O siftDemoV4.zip http://www.cs.ubc.ca/~lowe/keypoints/siftDemoV4.zip
\  
&& unzip siftDemoV4.zip \  
&& rm siftDemoV4.zip \  
&& cp siftDemoV4/sift bundler_sfm/bin  
  
WORKDIR \bundler_sfm  
RUN make  
  
RUN ln /usr/bin/jhead /bundler_sfm/bin/jhead  
  
# in place remove import Image (=PIL =outdated ?)  
RUN sed -i 's/^import Image$//g' /bundler_sfm/utils/bundler.py  
  

