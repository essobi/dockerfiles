FROM ubuntu  
  
# github.com/kbbrownn  
MAINTAINER Kaden Brown  
  
# Install all tools + libraries needed for the project  
RUN apt-get update && \  
apt-get -y install apt-utils && \  
apt-get -y install ssh && \  
apt-get -y install cmake && \  
apt-get -y install build-essential && \  
apt-get -y install gcc && \  
apt-get -y install gfortran && \  
apt-get -y install libblas-dev liblapack-dev && \  
apt-get -y install libz-dev && \  
apt-get -y install openmpi-bin libopenmpi-dev && \  
apt-get -y install freeglut3-dev && \  
apt-get -y install libglu1-mesa-dev && \  
apt-get -y install git  
  
# Setup project space  
RUN cd usr && \  
mkdir ArcSyn3sis && \  
cd ArcSyn3sis && \  
git clone https://github.com/libocca/occa.git && \  
cd occa && \  
git checkout 1.0 && \  
make  
  
# Set the default working directory to ArcSyn3sis dir  
WORKDIR /usr/ArcSyn3sis  
  
# Load source into container  
ADD . /usr/ArcSyn3sis  
  
# Set environment vars needed for occa  
ENV OCCA_DIR=/usr/ArcSyn3sis/occa  
ENV LD_LIBRARY_PATH=/usr/ArcSyn3sis/occa/lib  
  
# Final project setup  
RUN sh setup.sh  
  
CMD /bin/bash  

