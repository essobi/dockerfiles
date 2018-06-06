FROM nvidia/cuda:8.0-cudnn7-runtime  
  
ENV MINICONDA_VERSION 4.3.21  
ENV PYTHON_VERSION 3.6.2  
RUN apt-get update && apt-get install -y --no-install-recommends bzip2 curl
ca-certificates && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -o ~/miniconda.sh -O
https://repo.continuum.io/miniconda/Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh
&& \  
chmod +x ~/miniconda.sh && ~/miniconda.sh -b -p /opt/conda && rm
~/miniconda.sh && \  
/opt/conda/bin/conda create -y --name pytorch python=${PYTHON_VERSION} numpy
pyyaml scipy matplotlib graphviz ipython pytorch torchvision cuda80 -c soumith
&& \  
/opt/conda/bin/conda clean -ya  
  
ENV PATH /opt/conda/envs/pytorch/bin:$PATH  
  
WORKDIR /workspace  
RUN chmod -R a+w /workspace  

