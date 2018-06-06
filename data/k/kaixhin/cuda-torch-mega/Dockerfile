# Start with CUDA Torch base image  
FROM kaixhin/cuda-torch:latest  
MAINTAINER Kai Arulkumaran <design@kaixhin.com>  
  
# Install NCCL for multi-GPU communication  
RUN cd /root && git clone https://github.com/NVIDIA/nccl.git && cd nccl && \  
make CUDA_HOME=/usr/local/cuda -j"$(nproc)" && \  
make PREFIX=/root/nccl install  
ENV LD_LIBRARY_PATH=/root/nccl/lib:$LD_LIBRARY_PATH  
RUN luarocks install nccl  
  
# Install luaposix (removing CUDA stubs/LIBRARY_PATH)  
RUN unset LIBRARY_PATH && luarocks install luaposix  
  
# Install Moses  
RUN luarocks install moses  
  
# Install LogRoll  
RUN luarocks install logroll  
  
# Install ffmpeg dependencies  
RUN add-apt-repository ppa:mc3man/trusty-media && \  
apt-get update && apt-get install -y ffmpeg  
# Install ffmpeg  
RUN luarocks install ffmpeg  
  
# Install LuaSocket  
RUN luarocks install luasocket  
  
# Install parallel  
RUN luarocks install parallel  
  
# Install tds  
RUN luarocks install tds  
  
# Install IPC  
RUN luarocks install ipc  
  
# Install distlearn  
RUN luarocks install distlearn  
  
# Install torchnet  
RUN luarocks install torchnet  
  
# Install classic  
RUN luarocks install classic  
  
# Install torchx  
RUN luarocks install torchx  
  
# Install autograd  
RUN luarocks install autograd  
  
# Install dataset  
RUN luarocks install dataset  
  
# Install dpnn  
RUN luarocks install dpnn  
  
# Install nninit  
RUN luarocks install nninit  
  
# Install nnquery  
RUN luarocks install
https://raw.githubusercontent.com/bshillingford/nnquery/master/rocks/nnquery-
scm-1.rockspec  
  
# Install rnn  
RUN luarocks install rnn  
  
# Install loadcaffe dependencies  
RUN apt-get install -y \  
libprotobuf-dev \  
protobuf-compiler  
# Install loadcaffe  
RUN luarocks install loadcaffe  
  
# Install inn  
RUN luarocks install inn  
  
# Install gvnn  
RUN luarocks install
https://raw.githubusercontent.com/ankurhanda/gvnn/master/gvnn-scm-1.rockspec  
  
# Install optnet  
RUN luarocks install optnet  
  
# Install signal  
RUN luarocks install signal  
  
# Install xitari  
RUN luarocks install
https://raw.githubusercontent.com/lake4790k/xitari/master/xitari-0-0.rockspec  
  
# Install alewrap  
RUN luarocks install
https://raw.githubusercontent.com/Kaixhin/alewrap/master/alewrap-0-0.rockspec  
  
# Install rlenvs  
RUN luarocks install
https://raw.githubusercontent.com/Kaixhin/rlenvs/master/rocks/rlenvs-
scm-1.rockspec  
  
# Install twrl  
RUN luarocks install twrl  

