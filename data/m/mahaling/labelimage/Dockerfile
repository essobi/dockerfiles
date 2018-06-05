# Pull base image.  
FROM ubuntu:16.04  
MAINTAINER "Gayathri Mahalingam"  
# Install  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y build-essential && \  
apt-get install -y software-properties-common cmake && \  
apt-get install -y byobu curl git htop man unzip vim wget && \  
apt-get install -y yasm pkg-config libswscale-dev libtbb2 && \  
apt-get install -y libtbb-dev libpng-dev libtiff-dev libjasper-dev
libavformat-dev libpq-dev && \  
apt-get install -y python python-dev python-distribute python-pip python-qt4
&& \  
apt-get install -y python3 python3-dev python3-pip && \  
apt-get install -y libspatialindex-dev gcc g++ gfortran cython pyqt5-dev-tools
&& \  
apt-get install -y libxml2-dev libxmlsec1-dev && \  
rm -rf /var/lib/apt/lists/*  
  
# Set environment variables.  
ENV HOME /root  
  
# Define working directory.  
WORKDIR /root  
  
# pip install packages  
RUN pip3 install numpy \  
opencv-contrib-python \  
scikit-image  
  
WORKDIR /root/labelImg  
  
COPY . /root/labelImg  
  
RUN echo "alias python=python3" >> ~/.bash_aliases  
  
RUN echo "alias pip=pip3" >> ~/.bash_profile  
  
RUN python3 setup.py install  
  
# Define default command.  
CMD ["bash"]

