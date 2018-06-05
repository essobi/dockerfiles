FROM ubuntu:16.04  
  
# Run apt-get calls  
RUN apt-get update \  
&& apt-get install -y wget \  
&& wget -O- http://neuro.debian.net/lists/xenial.us-tn.full | tee
/etc/apt/sources.list.d/neurodebian.sources.list \  
&& apt-key adv --recv-keys \--keyserver hkp://pgp.mit.edu:80
0xA5D32F012649A5A9  
  
# Make a standard filesystem layout  
RUN mkdir -p /code \  
&& mkdir /oasis \  
&& mkdir /projects \  
&& mkdir /scratch \  
&& mkdir /local-scratch  
  
RUN apt-get install -y build-essential \  
&& apt-get install -y cmake \  
&& apt-get install -y cmake-curses-gui \  
&& apt-get install -y apt-utils \  
&& apt-get install -y git  
  
RUN export DEBIAN_FRONTEND=noninteractive \  
&& apt-get install -y libtbb-dev tbb-examples libtbb-doc libtbb2 \  
&& unset DEBIAN_FRONTEND  
  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget --quiet https://repo.continuum.io/archive/Anaconda2-4.1.1-Linux-x86_64.sh
-O ~/anaconda.sh && \  
/bin/bash ~/anaconda.sh -b -p /opt/conda && \  
rm ~/anaconda.sh  
  
# Install packages needed for VTK & ITK  
RUN apt-get install -y libglu1-mesa-dev freeglut3-dev mesa-common-dev  
  
  

