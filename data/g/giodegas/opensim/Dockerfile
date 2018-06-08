FROM derekslager/mono:3.6.0  
MAINTAINER Giovanni De Gasperis <giovanni@giodegas.it>  
  
RUN apt-get update && apt-get -y install git  
  
# Install OpenSim  
RUN git clone https://github.com/opensim/opensim /usr/src/opensim  
  
WORKDIR /usr/src/opensim  

