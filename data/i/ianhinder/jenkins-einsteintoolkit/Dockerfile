FROM jenkins  
MAINTAINER Ian Hinder <ian.hinder@aei.mpg.de>  
  
USER root  
  
RUN apt-get update && apt-get install -y git perl gfortran g++ libopenmpi-dev
openmpi-bin make libfftw3-dev libgsl0-dev libatlas-base-dev libjpeg-dev
libssl-dev libhdf5-serial-dev hdf5-tools && rm -rf /var/lib/apt/lists/*  
  
COPY plugins.txt /usr/local/etc/plugins.txt  
  
USER jenkins  
  
RUN plugins.sh /usr/local/etc/plugins.txt  
  
COPY config-einsteintoolkit.xml
/usr/share/jenkins/ref/jobs/EinsteinToolkit/config.xml  
  
USER root  
  
# Allow sudo access (for debugging)  
RUN apt-get update && apt-get install -y sudo && rm -rf /var/lib/apt/lists/*  
RUN adduser jenkins sudo  
  
USER jenkins  

