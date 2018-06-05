FROM walberla/buildenv-ubuntu-basic:16.04  
  
RUN apt-get update && apt-get install -y \  
clang-3.7 \  
libomp-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN update-alternatives \--install /usr/bin/clang clang /usr/bin/clang-3.7 999
\  
&& update-alternatives \--install /usr/bin/clang++ clang++
/usr/bin/clang++-3.7 999 \  
&& update-alternatives \--install /usr/bin/cc cc /usr/bin/clang-3.7 999 \  
&& update-alternatives \--install /usr/bin/c++ c++ /usr/bin/clang++-3.7 999  
  
RUN cd /tmp \  
&& mkdir boost \  
&& cd boost \  
&& curl -L
http://downloads.sourceforge.net/project/boost/boost/1.61.0/boost_1_61_0.tar.bz2
| tar xj \  
&& cd boost_1_61_0 \  
&& ./bootstrap.sh \--with-python=/usr/bin/python3 \  
&& ./b2 -j $(nproc) toolset=clang install \--prefix=/opt/boost \  
&& cd \  
&& rm -r /tmp/boost  
  
ENV BOOST_ROOT="/opt/boost"  
  
ENV CC="ccache clang" CXX="ccache clang++"  

