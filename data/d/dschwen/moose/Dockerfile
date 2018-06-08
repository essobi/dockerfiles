FROM ubuntu:14.04  
  
RUN apt-get update && apt-get install -y \  
wget  
  
# get and install the MOOSE mini-binary package  
RUN cd / && \  
echo Downloading && \  
wget http://www.schwen.de/moose-bin.tgz && \  
tar xvzPf moose-bin.tgz --skip-old-files  
  
RUN wget
https://raw.githubusercontent.com/dschwen/moose/bisect_6389/test/tests/postprocessors/findvalueonline/findvalueonline.i  
  
RUN export
LD_LIBRARY_PATH=/opt/moose/seacas/lib:/opt/moose/tbb/lib:/opt/moose/vtk-6.3/gcc-
opt/lib:/opt/moose/openmpi/openmpi-1.8.4/gcc-
opt/lib:/opt/moose/gcc_5.3.0/lib64:/opt/moose/gcc_5.3.0/lib:/opt/moose/gcc_5.3.0/lib/i386:/ssd/schwd/moose/libmesh/installed/lib
&& \  
cd /ssd/schwd/moose/modules/combined && \  
ldd ./modules-opt && \  
./modules-opt -i findvalueonline.i  
  

