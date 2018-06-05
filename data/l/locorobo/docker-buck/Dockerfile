FROM debian:jessie  
  
COPY apt.sources.list.debian /etc/apt/sources.list  
  
RUN dpkg --add-architecture armel && dpkg --add-architecture armhf  
  
RUN apt-key adv --keyserver pgp.mit.edu --recv-keys D57D95AF93178A7C && \  
apt-key adv --keyserver pgp.mit.edu --recv-keys 7DE089671804772E  
  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install --yes --no-install-
recommends \  
bash-completion \  
ca-certificates \  
cmake \  
crossbuild-essential-armel \  
crossbuild-essential-armhf \  
gdb \  
less \  
man-db \  
nano \  
pkg-config \  
qemu-user-static \  
sudo \  
tree \  
vim \  
wget \  
xz-utils  
  
RUN apt-get update && apt-get install -y build-essential git wget automake
python-dev libtool libssl-dev curl wget  
  
# Install watchman for buck  
RUN git clone https://github.com/facebook/watchman.git  
RUN cd watchman && ./autogen.sh && ./configure && make -j4 && sudo make
install  
  
RUN sudo sh -c "echo 'deb http://http.debian.net/debian jessie-backports main'
> /etc/apt/sources.list.d/jessie-backports.list"  
RUN sudo apt-get update  
RUN sudo apt-get -t jessie-backports -y install openjdk-8-jdk-headless  
RUN sudo apt-get -y install ant  
  
RUN wget --quiet
https://github.com/facebook/buck/archive/v2016.11.11.01.tar.gz  
RUN tar -xvf v2016.11.11.01.tar.gz  
RUN sudo update-java-alternatives -s java-1.8.0-openjdk-amd64  
RUN cd buck-2016.11.11.01 && ant && sudo ln -s ${PWD}/bin/buck /usr/bin/buck  
  
ADD ["toolchain-*.cmake", "/home/compiler/"]  

