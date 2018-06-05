FROM jupyter/base-notebook  
  
LABEL maintainer="Mads Jensen <mads@cfin.au.dk>"  
  
USER root  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y gcc git && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN git clone https://github.com/meeg-cfin/scientific_computing_basics.git \  
/home/jovyan/Tutorial && \  
mkdir /home/jovyan/Tutorial/files  
  
WORKDIR /home/jovyan/Tutorial  
ENTRYPOINT [ "/bin/bash", "-c"]  
RUN conda env create -f environment.yaml && \  
conda clean -a -y  
ENV PATH /opt/conda/envs/scb/bin:$PATH  
ENV CONDA_DEFAULT_ENV scb  
ENV CONDA_PREFIX /opt/conda/envs/scb  
  
RUN chown -R jovyan: /home/jovyan/Tutorial  
USER jovyan  
WORKDIR /home/jovyan/Tutorial  

