FROM ubuntu:16.04  
MAINTAINER francois.lanusse@gmail.com  
  
# Update Ubuntu Software repository and install basic dependencies  
RUN apt-get update && \  
apt-get -y install libfftw3-dev build-essential git cython curl  
  
# Create environment for building and installing software  
ENV ASTROINFORMATICS_HOME /opt/astroinformatics  
ENV FFTW /usr  
RUN mkdir -p ${ASTROINFORMATICS_HOME}  
  
#  
# Install SSHT  
#  
RUN apt-get update && apt-get install -y python-matplotlib python-numpy && \  
cd ${ASTROINFORMATICS_HOME} && \  
git clone https://github.com/EiffL/ssht.git && \  
cd ssht && \  
make && \  
python setup.py install  
  
ENV SSHT ${ASTROINFORMATICS_HOME}/ssht  
  
#  
# Install SO3  
#  
RUN cd ${ASTROINFORMATICS_HOME} && \  
git clone https://github.com/astro-informatics/so3.git && \  
cd so3 && \  
make  
  
ENV SO3 ${ASTROINFORMATICS_HOME}/so3  
  
#  
# Install S2LET  
#  
RUN cd ${ASTROINFORMATICS_HOME} && \  
git clone https://github.com/astro-informatics/s2let.git && \  
cd s2let && \  
make lib  
  
ENV S2LET ${ASTROINFORMATICS_HOME}/s2let  
  
#  
# Install massmappy  
#  
RUN cd ${ASTROINFORMATICS_HOME} && \  
git clone https://github.com/EiffL/massmappy.git && \  
cd massmappy && \  
python setup.py install  

