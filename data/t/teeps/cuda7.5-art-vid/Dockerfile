# Start with CUDA Torch dependencies  
FROM kaixhin/cuda-torch-deps:latest  
MAINTAINER Kai Arulkumaran <design@kaixhin.com>  
  
RUN apt-get install -y \  
vim \  
ssh \  
libprotobuf-dev \  
protobuf-compiler \  
libav-tools  
  
# Run Torch7 installation scripts  
RUN cd /root/torch && \  
./install.sh  
# Export environment variables manually  
ENV
LUA_PATH='/root/.luarocks/share/lua/5.1/?.lua;/root/.luarocks/share/lua/5.1/?/init.lua;/root/torch/install/share/lua/5.1/?.lua;/root/torch/install/share/lua/5.1/?/init.lua;./?.lua;/root/torch/install/share/luajit-2.1.0-beta1/?.lua;/usr/local/share/lua/5.1/?.lua;/usr/local/share/lua/5.1/?/init.lua'  
ENV
LUA_CPATH='/root/.luarocks/lib/lua/5.1/?.so;/root/torch/install/lib/lua/5.1/?.so;./?.so;/usr/local/lib/lua/5.1/?.so;/usr/local/lib/lua/5.1/loadall.so'  
ENV PATH=/root/torch/install/bin:$PATH  
ENV LD_LIBRARY_PATH=/root/torch/install/lib:$LD_LIBRARY_PATH  
ENV DYLD_LIBRARY_PATH=/root/torch/install/lib:$DYLD_LIBRARY_PATH  
ENV LUA_CPATH='/root/torch/install/lib/?.so;'$LUA_CPATH  
  
#install loadcaffe  
RUN cd /root/ && \  
luarocks install loadcaffe  
  
RUN cd /root/ && \  
git clone https://github.com/manuelruder/artistic-videos.git && \  
git clone https://github.com/Teepareep/cuda-files.git && \  
cp cuda-files/cuda/include/* /usr/local/cuda/include && \  
cp cuda-files/cuda/lib64/*.so* /usr/local/cuda/lib64 && \  
cp cuda-files/deepflow2-static artistic-videos/ && \  
cp cuda-files/deepmatching-static artistic-videos/ && \  
cd artistic-videos && \  
# cd models && \  
# sh download_models.sh && \ # this takes too long  
# cd /root/artistic-videos && \  
mkdir vid && \  
mkdir img  
  
# Set ~/caffe as working directory  
WORKDIR /root/artistic-videos  

