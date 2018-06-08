FROM ubuntu:xenial  
  
RUN apt-get update -y && apt-get install -y \  
apt-utils \  
gcc \  
cmake \  
libuv1-dev \  
python3-dev \  
python3-pip \  
wget \  
openssh-client  
  
RUN pip3 install --upgrade \  
pip \  
cloudpickle \  
pytest \  
pytest-timeout \  
pandas \  
bokeh \  
matplotlib \  
sphinx \  
sphinx-rtd-theme \  
flake8  
  
RUN cd ~ && \  
wget https://github.com/google/protobuf/releases/download/v3.2.0/protobuf-
python-3.2.0.tar.gz && \  
tar xvzf protobuf-python-3.2.0.tar.gz && \  
cd protobuf-3.2.0/ && \  
./configure && \  
make && \  
make install && \  
cd python && \  
python3 setup.py install  
  
RUN ldconfig  

