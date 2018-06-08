FROM ubuntu:14.04  
RUN \  
apt-get update && apt-get install -y \  
git \  
curl \  
wget \  
libssl-dev \  
libtool \  
build-essential \  
autoconf \  
automake \  
pkg-config \  
libgtk-3-dev \  
make \  
vim \  
valgrind \  
doxygen \  
libev-dev \  
libavl-dev \  
libpcre3-dev \  
unzip \  
sudo \  
python-setuptools \  
python-dev \  
build-essential \  
bison \  
flex  
  
# pyang  
RUN easy_install pip  
RUN pip install --upgrade pyang  
  
# Adding netconf user  
RUN adduser --system netconf  
RUN mkdir -p /home/netconf/.ssh  
RUN echo "netconf:netconf" | chpasswd && adduser netconf sudo  
  
# Clearing and setting authorized ssh keys  
RUN echo '' > /home/netconf/.ssh/authorized_keys  
RUN ssh-keygen -A  
RUN ssh-keygen -t dsa -P '' -f /home/netconf/.ssh/id_dsa  
RUN cat /home/netconf/.ssh/id_dsa.pub >> /home/netconf/.ssh/authorized_keys  
  
# Updating shell to bash  
RUN sed -i s#/home/netconf:/bin/false#/home/netconf:/bin/bash# /etc/passwd  
  
RUN mkdir /opt/dev && sudo chown -R netconf /opt/dev  
  
# set root password to root  
RUN echo "root:root" | chpasswd  
  
# protobuf  
RUN \  
cd /opt/dev && \  
git clone https://github.com/google/protobuf.git && cd protobuf && \  
./autogen.sh && \  
./configure --prefix=/usr && \  
make -j2 && \  
make install  
  
# protobuf-c  
RUN \  
cd /opt/dev && \  
git clone https://github.com/protobuf-c/protobuf-c.git && cd protobuf-c && \  
./autogen.sh && \  
./configure --prefix=/usr && \  
make -j2 && \  
make install  
  
#cmake  
RUN \  
cd /opt/dev && \  
wget https://cmake.org/files/v3.6/cmake-3.6.2.tar.gz && \  
tar -xvf cmake-3.6.2.tar.gz && rm cmake-3.6.2.tar.gz && cd cmake-3.6.2 && \  
./bootstrap && \  
make -j2 && \  
make install  
  
#cmocka  
RUN \  
cd /opt/dev && \  
git clone git://git.cryptomilk.org/projects/cmocka.git && cd cmocka && \  
git checkout tags/cmocka-1.0.1 && \  
mkdir build && cd build && \  
cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr .. && \  
make -j2 && \  
make install  
  
# libssh  
RUN \  
cd /opt/dev && \  
git clone http://git.libssh.org/projects/libssh.git && cd libssh && \  
mkdir build && cd build && \  
cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr .. && \  
make -j2 && \  
make install  
  
# swig  
RUN \  
cd /opt/dev && \  
wget http://downloads.sourceforge.net/swig/swig-3.0.8.tar.gz && \  
tar -xvf swig-3.0.8.tar.gz && rm swig-3.0.8.tar.gz && cd swig-3.0.8 && \  
./configure --prefix=/usr --without-clisp --without-maximum-compile-warnings
&& \  
make && \  
make install && \  
install -v -m755 -d /usr/share/doc/swig-3.0.8 && \  
cp -v -R Doc/* /usr/share/doc/swig-3.0.8  
  
# fix nodejs name problem in ubunt  
RUN sudo ln -sf /usr/bin/nodejs /usr/bin/node  
  
RUN echo "version 20161012"  
  
# libredblack  
RUN \  
cd /opt/dev && \  
git clone https://github.com/sysrepo/libredblack.git && cd libredblack && \  
./configure && \  
make -j2 && \  
make install  
  
# libyang  
RUN \  
cd /opt/dev && \  
git clone https://github.com/CESNET/libyang.git && cd libyang && \  
git checkout devel && \  
mkdir build && cd build && \  
cmake -DCMAKE_BUILD_TYPE:String="Debug" -DCMAKE_INSTALL_PREFIX:PATH=/usr
-DENABLE_BUILD_TESTS=OFF .. && \  
make -j2 && \  
make install  
  
# libnetconf2  
RUN \  
cd /opt/dev && \  
git clone https://github.com/CESNET/libnetconf2.git && cd libnetconf2 && \  
git checkout devel && \  
mkdir build && cd build && \  
cmake -DCMAKE_BUILD_TYPE:String="Debug" -DCMAKE_INSTALL_PREFIX:PATH=/usr
-DENABLE_BUILD_TESTS=OFF .. && \  
make -j2 && \  
make install  
  
# install lua  
RUN \  
apt-get update && apt-get install -y \  
luajit \  
luarocks  
  
# install lua 5.2  
RUN \  
apt-get update && apt-get install -y \  
lua5.2 \  
lua5.2-dev  
  
# install node v4.x  
RUN \  
curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash - && \  
sudo apt-get install -y nodejs && \  
npm install -g node-gyp  
  
# install java  
RUN \  
apt-get update && apt-get install -y \  
default-jre \  
default-jdk  
  
# install python3  
RUN \  
apt-get update && apt-get install -y \  
python3.4 \  
python3.4-dev  
  
# sysrepo  
RUN \  
cd /opt/dev && \  
git clone https://github.com/sysrepo/sysrepo.git && cd sysrepo && \  
git checkout devel && \  
mkdir build && cd build && \  
cmake -DENABLE_TESTS=OFF -DCMAKE_BUILD_TYPE="Debug"
-DCMAKE_INSTALL_PREFIX:PATH=/usr -DREPOSITORY_LOC:PATH=/etc/sysrepo .. && \  
make -j2 && \  
make install  
  
# netopeer 2  
RUN \  
cd /opt/dev && git clone https://github.com/CESNET/Netopeer2.git && cd
Netopeer2 && \  
git checkout devel-server && \  
cd /opt/dev/Netopeer2/server && \  
mkdir build && cd build && \  
cmake -DCMAKE_BUILD_TYPE:String="Debug" -DCMAKE_INSTALL_PREFIX:PATH=/usr .. &&
\  
make -j2 && \  
make install && \  
cd /opt/dev/Netopeer2/cli && \  
git checkout devel-cli && \  
mkdir build && cd build && \  
cmake -DCMAKE_BUILD_TYPE:String="Debug" -DCMAKE_INSTALL_PREFIX:PATH=/usr .. &&
\  
make -j2 && \  
make install  
  
# install libyang javascript bindings  
#RUN \  
# cd /opt/dev/libyang && \  
# mkdir build_javascript_bindings && cd build_javascript_bindings && \  
# cmake -DCMAKE_BUILD_TYPE:String="Debug" -DCMAKE_INSTALL_PREFIX:PATH=/usr
-DENABLE_BUILD_TESTS=OFF -DJAVASCRIPT_BINDING=ON .. && \  
# make -j2 && \  
# cd javascript && \  
# node-gyp configure && \  
# node-gyp build  
EXPOSE 6001  
CMD ["/usr/bin/sysrepod"]  
CMD ["/usr/bin/netopeer2-server", "-d"]  

