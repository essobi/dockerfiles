FROM centos:centos6  
MAINTAINER Mike Miller <mike@mtmxr.com>  
  
# Update and set up the EPEL repository  
RUN yum update -y  
RUN yum install -y epel-release  
  
# Install build tools needed for building Octave  
RUN yum install -y bison flex gcc gcc-c++ gcc-gfortran gperf make  
  
# Install auxiliary tools for plotting, building the manual, etc.  
RUN yum install -y ghostscript gnuplot tar texinfo texinfo-tex  
RUN yum install -y /usr/bin/dvips  
  
# And Octave's libraries  
RUN yum install -y GraphicsMagick-c++-devel arpack-devel atlas-devel \  
blas-devel fftw-devel fltk-devel fontconfig-devel freetype-devel \  
gl2ps-devel glpk-devel hdf5-devel java-devel lapack-devel \  
libXft-devel mesa-libGL-devel mesa-libGLU-devel pcre-devel \  
qhull-devel qrupdate-devel readline-devel suitesparse-devel \  
zlib-devel  
  
# Libraries that differ between CentOS versions, for ease of maintenance  
RUN yum install -y libcurl-devel  
RUN yum install -y qscintilla-devel qt-devel  
  
CMD bash  

