# Dockerfile for speech to text (STT) based on Kaldi ASR (http://kaldi-
asr.org/)  
# Kaldi's 'chain' models (type of DNN-HMM model) used  
# Model released by api.ai team  
# (https://github.com/api-ai/api-ai-english-asr-model)  
#  
# (c) Abylay Ospan <aospan@jokersys.com>, 2017  
# https://jokersys.com  
# under GPLv2 license  
FROM ubuntu:14.04  
MAINTAINER aospan@jokersys.com  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential cmake git wget python-dev unzip \  
python-numpy python-scipy curl python-tk libatlas3-base \  
ca-certificates zlib1g-dev automake autoconf libtool subversion && \  
curl -k https://bootstrap.pypa.io/get-pip.py > get-pip.py && python get-pip.py
&& \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /opt  
  
# * compile Kaldi  
# * make image more compact:  
# strip binary files, remove *.o files  
# * download api.ai model  
RUN git clone https://github.com/kaldi-asr/kaldi.git && \  
sudo ln -s -f bash /bin/sh && \  
cd kaldi/tools/ && make -j"$(nproc)" && \  
cd ../src && ./configure --shared && \  
make depend -j"$(nproc)" && make -j"$(nproc)" && \  
find /opt/kaldi/ -name "*.o" -exec rm -f {} \; && \  
find /opt/kaldi/tools/ -type f -perm +100 -exec strip {} \; 2>/dev/null && \  
find /opt/kaldi/src/ -type f -perm +100 -exec strip {} \; 2>/dev/null && \  
cd /opt/kaldi/egs/apiai_decode/s5 && ./download-model.sh  
  
WORKDIR /opt/kaldi  
COPY entrypoint.sh /entrypoint.sh  
COPY in.wav /opt/in/  
CMD /entrypoint.sh  

