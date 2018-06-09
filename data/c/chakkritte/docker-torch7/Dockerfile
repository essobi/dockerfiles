FROM ubuntu:14.04.4  
  
MAINTAINER Chakkrit Termritthikun <chakkritte57@nu.ac.th>  
  
RUN \  
apt-get -q -y update && \  
apt-get -q -y install git cmake software-properties-common wget ipython3
libssl-dev libzmq3-dev python-zmq python-pip && \  
apt-get upgrade -q -y && \  
rm -rf /var/lib/apt/lists/*  
  
RUN \  
git clone https://github.com/torch/distro.git ~/torch \--recursive && \  
cd ~/torch; bash install-deps;  
  
ADD config/install.sh /root/torch/install.sh  
  
RUN \  
chmod a+x /root/torch/install.sh  
  
RUN \  
cd ~/torch && \  
./install.sh  
  
RUN \  
cd /usr/local/lib && \  
sudo ln -s libluajit.so libluajit-5.1.so  
  
CMD ["/bin/bash"]  

