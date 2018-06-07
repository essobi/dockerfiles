# caffe  
FROM ubuntu:16.04  
LABEL maintainer caffe-maint@googlegroups.com  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
cmake \  
git \  
wget \  
libatlas-base-dev \  
libboost-all-dev \  
libgflags-dev \  
libgoogle-glog-dev \  
libhdf5-serial-dev \  
libleveldb-dev \  
liblmdb-dev \  
libopencv-dev \  
libprotobuf-dev \  
libsnappy-dev \  
protobuf-compiler \  
python-dev \  
python-numpy \  
python-pip \  
python-setuptools \  
python-scipy  
  
ENV CAFFE_ROOT=/opt/caffe  
WORKDIR $CAFFE_ROOT  
  
# FIXME: use ARG instead of ENV once DockerHub supports this  
# https://github.com/docker/hub-feedback/issues/460  
ENV CLONE_TAG=1.0  
RUN git clone \--depth 1 https://github.com/gogartom/caffe-textmaps . && \  
pip install --upgrade pip && \  
cd python && for req in $(cat requirements.txt) pydot; do pip install $req;
done && cd .. && \  
mkdir build && cd build && \  
cmake -DCPU_ONLY=1 .. && \  
make all -j"$(nproc)" && \  
make pycaffe && \  
make install  
  
ENV PYCAFFE_ROOT $CAFFE_ROOT/python  
ENV PYTHONPATH $PYCAFFE_ROOT:$PYTHONPATH  
ENV PATH $CAFFE_ROOT/build/tools:$PYCAFFE_ROOT:$PATH  
RUN echo "$CAFFE_ROOT/build/lib" >> /etc/ld.so.conf.d/caffe.conf && ldconfig  
  
# torch  
# Install Keras  
RUN pip --no-cache-dir install keras  
  
# theano  
RUN pip install theano  
  
#  
# Install Lasagne  
RUN pip --no-cache-dir install
git+git://github.com/Lasagne/Lasagne.git@${LASAGNE_VERSION}  
  
################  
# # Install Torch  
# RUN git clone https://github.com/torch/distro.git /root/torch --recursive &&
\  
# cd /root/torch && \  
# bash install-deps && \  
# yes no | ./install.sh  
#  
# # Export the LUA evironment variables manually  
# ENV
LUA_PATH='/root/.luarocks/share/lua/5.1/?.lua;/root/.luarocks/share/lua/5.1/?/init.lua;/root/torch/install/share/lua/5.1/?.lua;/root/torch/install/share/lua/5.1/?/init.lua;./?.lua;/root/torch/install/share/luajit-2.1.0-beta1/?.lua;/usr/local/share/lua/5.1/?.lua;/usr/local/share/lua/5.1/?/init.lua'
\  
#
LUA_CPATH='/root/.luarocks/lib/lua/5.1/?.so;/root/torch/install/lib/lua/5.1/?.so;./?.so;/usr/local/lib/lua/5.1/?.so;/usr/local/lib/lua/5.1/loadall.so'
\  
# PATH=/root/torch/install/bin:$PATH \  
# LD_LIBRARY_PATH=/root/torch/install/lib:$LD_LIBRARY_PATH \  
# DYLD_LIBRARY_PATH=/root/torch/install/lib:$DYLD_LIBRARY_PATH  
# ENV LUA_CPATH='/root/torch/install/lib/?.so;'$LUA_CPATH  
#  
# # Install the latest versions of nn, and iTorch  
# RUN luarocks install nn && \  
# luarocks install loadcaffe && \  
# \  
# cd /root && git clone https://github.com/facebook/iTorch.git && \  
# cd iTorch && \  
# luarocks make  
#  
###################  
# tensorflow  
RUN apt-get install python-pip python-dev python-opencv python-tk -y  
RUN pip install tensorflow  
  
# Expose Ports for TensorBoard (6006), Ipython (8888)  
EXPOSE 6006 8888  
# phantomjs  
# the phantomjs does not work must update to new version by wget from official
site  
#https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2  
run apt-get update && apt-get install xvfb -y && \  
apt-get clean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
run pip uninstall numpy -y  
run wget
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
-nv  
# run bzip2 -d phantomjs-2.1.1-linux-x86_64.tar.bz2 | tar -zxvf -  
run tar -jxvf phantomjs-2.1.1-linux-x86_64.tar.bz2  
run mv phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/bin/  
run chmod +x /usr/bin/phantomjs  
run rm phantomjs-2.1.1-linux-x86_64.tar.bz2  
run rm -rvf phantomjs-2.1.1-linux-x86_64  
  
RUN pip install matplotlib scikit-image scikit-learn  
RUN pip install jupyter  
#run apt-get update && apt-get install python-opencv python-tk -y  
# this is tricky for caffe, it uses python-numpy but to make it work, we have
to re-install int  
run pip uninstall numpy -y && apt-get update && apt-get install --reinstall
python-numpy  
  
# Install Torch  
RUN git clone \--depth=1 https://github.com/torch/distro.git /root/torch
--recursive  
run cd /root/torch  
run apt update && apt install sudo -y  
run cd /root/torch && bash install-deps  
run cd /root/torch && yes no | ./install.sh  
ENV
LUA_PATH='/root/.luarocks/share/lua/5.1/?.lua;/root/.luarocks/share/lua/5.1/?/init.lua;/root/torch/install/share/lua/5.1/?.lua;/root/torch/install/share/lua/5.1/?/init.lua;./?.lua;/root/torch/install/share/luajit-2.1.0-beta1/?.lua;/usr/local/share/lua/5.1/?.lua;/usr/local/share/lua/5.1/?/init.lua'  
ENV
LUA_CPATH='/root/.luarocks/lib/lua/5.1/?.so;/root/torch/install/lib/lua/5.1/?.so;./?.so;/usr/local/lib/lua/5.1/?.so;/usr/local/lib/lua/5.1/loadall.so'  
ENV PATH=/root/torch/install/bin:$PATH  
ENV LD_LIBRARY_PATH=/root/torch/install/lib:$LD_LIBRARY_PATH  
ENV DYLD_LIBRARY_PATH=/root/torch/install/lib:$DYLD_LIBRARY_PATH  
ENV LUA_CPATH='/root/torch/install/lib/?.so;'$LUA_CPATH  
# # Export the LUA evironment variables manually  
# ENV
LUA_PATH='/root/.luarocks/share/lua/5.1/?.lua;/root/.luarocks/share/lua/5.1/?/init.lua;/root/torch/install/share/lua/5.1/?.lua;/root/torch/install/share/lua/5.1/?/init.lua;./?.lua;/root/torch/install/share/luajit-2.1.0-beta1/?.lua;/usr/local/share/lua/5.1/?.lua;/usr/local/share/lua/5.1/?/init.lua'
\  
#
LUA_CPATH='/root/.luarocks/lib/lua/5.1/?.so;/root/torch/install/lib/lua/5.1/?.so;./?.so;/usr/local/lib/lua/5.1/?.so;/usr/local/lib/lua/5.1/loadall.so'
\  
# PATH=/root/torch/install/bin:$PATH \  
# LD_LIBRARY_PATH=/root/torch/install/lib:$LD_LIBRARY_PATH \  
# DYLD_LIBRARY_PATH=/root/torch/install/lib:$DYLD_LIBRARY_PATH  
# ENV LUA_CPATH='/root/torch/install/lib/?.so;'$LUA_CPATH  
#  
# # Install the latest versions of nn, and iTorch  
run apt update && apt-get install libssl-dev -y  
RUN luarocks install nn && \  
luarocks install loadcaffe  
run cd /root && git clone \--depth=1 https://github.com/facebook/iTorch.git &&
\  
cd iTorch && \  
luarocks make  
#  
run apt-get clean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
WORKDIR /workspace

