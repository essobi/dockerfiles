FROM ubuntu:14.04  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install python-software-properties
&& \  
DEBIAN_FRONTEND=noninteractive apt-get -y install software-properties-common
&& \  
DEBIAN_FRONTEND=noninteractive add-apt-repository ppa:ubuntu-toolchain-r/test
&& \  
DEBIAN_FRONTEND=noninteractive add-apt-repository ppa:george-
edison55/cmake-3.x && \  
DEBIAN_FRONTEND=noninteractive add-apt-repository ppa:fkrull/deadsnakes && \  
DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y -qq wget g++ gcc-4.9 g++-4.9
libgflags-dev libsnappy-dev zlib1g-dev libbz2-dev libgtest-dev cmake unzip
python2.7 lcov python-pip && \  
DEBIAN_FRONTEND=noninteractive pip install coveralls && \  
DEBIAN_FRONTEND=noninteractive update-alternatives --install /usr/bin/g++ g++
/usr/bin/g++-4.9 50 && \  
DEBIAN_FRONTEND=noninteractive apt-get autoclean && \  
DEBIAN_FRONTEND=noninteractive apt-get autoremove  
  
RUN ls && wget https://github.com/sloiza/Taller2/archive/master.zip && ls &&
unzip master.zip && ls && \  
cd Taller2-master && chmod +x servidor/install_dependencies.sh &&
./servidor/install_dependencies.sh && cd

