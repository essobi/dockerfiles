FROM ubuntu:14.04  
MAINTAINER Mohamed Ahmednah <mauriyouth@gmail.com>  
  
RUN apt-get update && apt-get install -y \  
git \  
software-properties-common \  
ipython3 \  
libssl-dev \  
libzmq3-dev \  
python-zmq \  
python-pip \  
sudo \  
build-essential gcc g++ curl \  
cmake libreadline-dev git-core libqt4-dev libjpeg-dev \  
libpng-dev ncurses-dev imagemagick libzmq3-dev gfortran \  
unzip gnuplot gnuplot-x11 ipython  
  
RUN git clone https://github.com/torch/distro.git /root/torch --recursive &&
cd /root/torch && \  
make NO_AFFINITY=1 USE_OPENMP=1 && make install\  
./install.sh  
  
RUN luarocks install dkjson  
# RUN luarocks install lua-zmq ZEROMQ_LIBDIR=/usr/lib/x86_64-linux-gnu/
ZEROMQ_INCDIR=/usr/include  
RUN luarocks install sundown  
RUN luarocks install cwrap  
RUN luarocks install paths  
RUN luarocks install torch  
RUN luarocks install nn  
RUN luarocks install dok  
RUN luarocks install gnuplot  
RUN luarocks install qtlua  
RUN luarocks install qttorch  
RUN luarocks install luafilesystem  
RUN luarocks install penlight  
RUN luarocks install sys  
RUN luarocks install xlua  
RUN luarocks install image  
RUN luarocks install optim  
RUN luarocks install lua-cjson  
RUN luarocks install trepl  
RUN luarocks install nnx  
RUN luarocks install threads  
RUN luarocks install graphicsmagick  
RUN luarocks install argcheck  
RUN luarocks install signal  
RUN luarocks install bit32  
RUN luarocks install restserver-xavante  

