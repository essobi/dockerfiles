FROM oscarmartin/zmqbase  
MAINTAINER oscarmartinvicente@gmail.com  
  
# Install needed packages  
RUN apt-get update && \  
apt-get install -y \  
python-pip \  
software-properties-common \  
python-dev && \  
pip install pyzmq && \  
apt-get purge -y \  
software-properties-common \  
locales \  
manpages \  
manpages-dev \  
perl \  
gcc \  
python-dev && \  
apt-get clean && \  
apt-get autoclean && \  
apt-get -y autoremove  
  
WORKDIR /project  
  
ENTRYPOINT ["python"]  

