#  
# pcl_eigen dockerfile  
# Creates environment needed for compilation of our projects  
#  
# Pull base image.  
FROM ubuntu:16.04  
# Install.  
RUN apt-get update  
  
RUN apt-get install -y software-properties-common  
RUN apt-get install -y ca-certificates  
RUN apt-get install -y wget  
RUN apt-get install -y curl  
RUN apt-get install -y ssh  
# --no-install-recommends --fix-missing  
RUN wget -O - http://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add -  
RUN apt-add-repository "deb http://apt.llvm.org/xenial/ llvm-toolchain-
xenial-4.0 main"  
  
RUN apt-get update  
RUN apt-get install -y build-essential  
  
RUN apt-get install -y \  
mc \  
lynx \  
libvtk5.10 libvtk5-dev \  
libqhull* \  
pkg-config \  
python2.7-dev \  
\--no-install-recommends --fix-missing  
  
RUN apt-get install -y \  
mesa-common-dev \  
cmake \  
git \  
mercurial \  
freeglut3-dev \  
libflann-dev \  
\--no-install-recommends --fix-missing  
  
RUN apt-get autoremove  
  
RUN wget -O boost_1_64_0.tar.gz
http://sourceforge.net/projects/boost/files/boost/1.64.0/boost_1_64_0.tar.gz/download  
RUN tar xzvf boost_1_64_0.tar.gz && rm boost_1_64_0.tar.gz  
RUN cd boost_1_64_0 && ./bootstrap.sh --prefix=/usr/  
#RUN cd boost_1_64_0 && ./b2  
RUN cd boost_1_64_0 && ./b2 install  
  
RUN cd /opt && hg clone -r 3.2 https://bitbucket.org/eigen/eigen eigen  
RUN mkdir -p /opt/eigen/build  
RUN cd /opt/eigen/build && cmake ..  
RUN cd /opt/eigen/build && make install  
#RUN git config --global url.git://github.com/.insteadOf https://github.com/  
RUN cd /opt && git clone -b pcl-1.8.0
https://github.com/PointCloudLibrary/pcl.git pcl  
RUN mkdir -p /opt/pcl/build  
RUN cd /opt/pcl/build && cmake -DCMAKE_BUILD_TYPE=None -DBUILD_GPU=OFF
-DBUILD_apps=OFF -DBUILD_examples=OFF ..  
RUN cd /opt/pcl/build && make -j4  
RUN cd /opt/pcl/build && make install  
RUN cd /opt/pcl/build && make clean  
  

