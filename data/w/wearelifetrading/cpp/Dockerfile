FROM wearelifetrading/base:1.0  
  
MAINTAINER Life Trading <technology@lifetrading.com.au>  
  
# Install only the essential build tools  
RUN sudo apt-get update && \  
sudo apt-get install -y bzip2 cmake g++ g++-5 git  
  
# Build and install gsl  
RUN sudo apt-get install -y libpcre3-dev && \  
cd /tmp && \  
git clone git://github.com/imatix/gsl && \  
cd gsl/src && \  
make && \  
sudo make install  
  
# Build and install google benchmark  
RUN cd /tmp && \  
git clone https://github.com/google/benchmark.git && \  
cd benchmark && \  
cmake -DCMAKE_BUILD_TYPE=Release -DBENCHMARK_ENABLE_TESTING=false && \  
make && \  
sudo make install  
  
# Install tcmalloc  
RUN sudo apt-get update && \  
sudo apt-get install -y autoconf libtool libunwind-dev && \  
cd /tmp && \  
git clone https://github.com/gperftools/gperftools.git && \  
cd gperftools && \  
./autogen.sh && \  
./configure --enable-frame-pointers --enable-libunwind --disable-shared && \  
make && \  
sudo make install  
  
# Download, unzip and patch boost  
RUN cd /tmp && \  
sudo apt-get install -y libbz2-dev && \  
wget
https://downloads.sourceforge.net/project/boost/boost/1.61.0/boost_1_61_0.tar.bz2
&& \  
tar xfj boost_1_61_0.tar.bz2 && \  
cd boost_1_61_0 && \  
sed -i 's!^# pragma!//# pragma!' boost/type_traits/detail/bool_trait_def.hpp
&& \  
sed -i 's!^# pragma!//# pragma!'
boost/type_traits/detail/template_arity_spec.hpp && \  
./bootstrap.sh  
  
# Download protobuf and dependencies  
RUN sudo apt-get install -y libz-dev autoconf automake libtool unzip && \  
cd /tmp && \  
git clone https://github.com/google/protobuf.git && \  
cd protobuf && \  
./autogen.sh && \  
git checkout v3.0.0  
  
# Install packages needed for our build, and other useful tools  
RUN sudo apt-get update && \  
sudo apt-get install -y ccache clang-format libreadline-dev libyaml-dev ninja-
build vim-nox wireshark-dev xsltproc  
  

