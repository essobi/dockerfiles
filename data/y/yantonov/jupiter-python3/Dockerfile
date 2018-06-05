FROM continuumio/anaconda3  
  
MAINTAINER Yury Antonov <yantonov@yandex.ru>  
  
RUN /opt/conda/bin/pip install --upgrade pip && \  
/opt/conda/bin/conda update conda -y && \  
/opt/conda/bin/conda install jupyter -y && \  
/opt/conda/bin/conda install gensim -y && \  
/opt/conda/bin/pip install
https://github.com/pybrain/pybrain/archive/0.3.3.zip  
  
# bigartm installation  
RUN apt-get --yes update && \  
apt-get --yes install git make build-essential libboost-all-dev  
  
# bigartm needs cmake at least 3.1  
# base image uses debian 8, so the latest version of cmake is 3.0.2  
# that why latest version of cmake must be installed manually  
RUN cd /opt && \  
wget https://cmake.org/files/v3.10/cmake-3.10.2-Linux-x86_64.sh  
  
RUN cd /opt && \  
chmod +x cmake-3.10.2-Linux-x86_64.sh  
  
RUN cd /opt && \  
echo 'y' | ./cmake-3.10.2-Linux-x86_64.sh  
  
ENV PATH="/opt/cmake-3.10.2-Linux-x86_64/bin:${PATH}"  
RUN /opt/conda/bin/conda install protobuf tqdm wheel -y  
  
RUN cd /opt && \  
git clone \--branch=stable https://github.com/bigartm/bigartm.git && \  
cd bigartm && \  
mkdir build && cd build && \  
cmake .. && \  
make  
  
RUN cd /opt/bigartm/build && \  
make install  
  
ENV ARTM_SHARED_LIBRARY=/usr/local/lib/libartm.so  
  
RUN cd /opt/bigartm/build && \  
/opt/conda/bin/pip install python/bigartm*.whl  
  
ENV CUSER someuser  
  
RUN useradd -m -s /bin/bash -N $CUSER && \  
mkdir -p /opt/notebooks && \  
chown $CUSER /opt/notebooks  
  
USER $CUSER  

