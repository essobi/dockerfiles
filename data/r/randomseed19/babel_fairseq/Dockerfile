FROM nvidia/cuda:8.0-cudnn6-devel-ubuntu16.04  
  
RUN apt-get update && apt-get install -y \--no-install-recommends \  
build-essential \  
git \  
curl \  
ca-certificates \  
libjpeg-dev \  
libpng-dev && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -o ~/miniconda.sh -O
https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh && \  
chmod +x ~/miniconda.sh && \  
~/miniconda.sh -b -p /opt/conda && \  
rm ~/miniconda.sh && \  
/opt/conda/bin/conda install conda-build && \  
/opt/conda/bin/conda clean -ya  
  
RUN /opt/conda/bin/conda install -c pytorch magma-cuda80 &&
/opt/conda/bin/conda clean -ya  
RUN /opt/conda/bin/conda install pytorch torchvision cuda80 -c pytorch &&
/opt/conda/bin/conda clean -ya  
  
ENV NVIDIA_VISIBLE_DEVICES all  
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility  
ENV LD_LIBRARY_PATH /usr/local/nvidia/lib:/usr/local/nvidia/lib64  
  
RUN echo 'export PATH="/opt/conda/bin/:$PATH"' >> ~/.bashrc  
  
RUN git clone https://github.com/facebookresearch/fairseq-py.git  
  
RUN /bin/bash -c "cd /fairseq-py \  
&& /opt/conda/bin/pip install -r /fairseq-py/requirements.txt"  
  
ENV LANG C.UTF-8  
RUN cd /fairseq-py && /opt/conda/bin/python /fairseq-py/setup.py build &&
/opt/conda/bin/python setup.py develop  
  
RUN git clone https://github.com/moses-smt/mosesdecoder.git  
RUN git clone https://github.com/rsennrich/subword-nmt.git

