FROM hivesolutions/ubuntu:xenial  
  
LABEL version="1.0"  
LABEL maintainer="Hive Solutions <development@hive.pt>"  
  
RUN echo "deb [arch=amd64] https://apt-mo.trafficmanager.net/repos/dotnet-
release/ xenial main" > /etc/apt/sources.list.d/dotnetdev.list &&\  
apt-key adv --keyserver apt-mo.trafficmanager.net --recv-keys 417A0893 &&\  
apt-get update &&\  
apt-get install -y -q sudo gcc make curl pypy dotnet-dev-1.0.0 linux-headers-
generic\  
libssl-dev python-dev python3-dev pypy-dev &&\  
wget https://raw.githubusercontent.com/dotnet/core/master/release-
notes/1.0/install-1.0.1.sh &&\  
chmod +x install-1.0.1.sh && (echo "y" | bash install-1.0.1.sh) && rm
install-1.0.1.sh  
  
CMD ["/bin/bash"]  

