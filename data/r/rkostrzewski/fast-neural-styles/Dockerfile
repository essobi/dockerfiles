FROM debian  
  
RUN apt-get -y update && apt-get install -y \  
sudo \  
git \  
software-properties-common \  
ipython3 \  
libssl-dev \  
libzmq3-dev \  
python-zmq \  
python-pip  
  
RUN git clone https://github.com/torch/distro.git /root/torch \--recursive &&
cd /root/torch && \  
bash install-deps && \  
DEBIAN_FRONTEND=noninteractive ./install.sh  
  
ENV
LUA_PATH='/root/.luarocks/share/lua/5.1/?.lua;/root/.luarocks/share/lua/5.1/?/init.lua;/root/torch/install/share/lua/5.1/?.lua;/root/torch/install/share/lua/5.1/?/init.lua;./?.lua;/root/torch/install/share/luajit-2.1.0-beta1/?.lua;/usr/local/share/lua/5.1/?.lua;/usr/local/share/lua/5.1/?/init.lua'  
ENV
LUA_CPATH='/root/.luarocks/lib/lua/5.1/?.so;/root/torch/install/lib/lua/5.1/?.so;./?.so;/usr/local/lib/lua/5.1/?.so;/usr/local/lib/lua/5.1/loadall.so'  
ENV PATH=/root/torch/install/bin:$PATH  
ENV LD_LIBRARY_PATH=/root/torch/install/lib:$LD_LIBRARY_PATH  
ENV DYLD_LIBRARY_PATH=/root/torch/install/lib:$DYLD_LIBRARY_PATH  
ENV LUA_CPATH='/root/torch/install/lib/?.so;'$LUA_CPATH  
  
RUN luarocks install nn && \  
luarocks install image && \  
luarocks install lua-cjson  
  
RUN git clone https://github.com/jcjohnson/fast-neural-style.git /root/fast-
neural-style \--recursive && cd /root/fast-neural-style && \  
bash ./models/download_style_transfer_models.sh  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/usr/share/man/?? /usr/share/man/??_*  
  
WORKDIR /root/fast-neural-style  

