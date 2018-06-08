# DOCKER-VERSION 1.1.0  
#inherit from the base container, which have all the needed script to launch
tasks  
FROM ingi/inginious-c-base  
LABEL org.inginious.grading.name="math"  
  
#install Octave, Julia, numpy and sympy  
RUN yum -y install git octave octave-control octave-GeographicLib \  
octave-doc octave-general octave-image octave-io \  
octave-lhapdf octave-netcdf octave-signal \  
octave-statistics julia && \  
yum clean all && \  
pip3.5 install matplotlib numpy antlr4-python3-runtime && \  
pip3.5 install git+https://github.com/sympy/sympy  

