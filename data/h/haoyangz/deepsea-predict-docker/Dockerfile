FROM kaixhin/torch  
MAINTAINER Haoyang Zeng <haoyangz@mit.edu>  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
emacs24-nox \  
luarocks \  
nano && \  
apt-get autoremove -y && \  
apt-get clean -y  
  
# Install Python 2 Conda and some packages.  
ENV CONDA_DIR /opt/conda  
ENV PATH $CONDA_DIR/bin:$PATH  
RUN cd /tmp && \  
mkdir -p $CONDA_DIR && \  
wget --quiet --no-check-certificate
https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh && \  
/bin/bash Miniconda2-latest-Linux-x86_64.sh -f -b -p $CONDA_DIR && \  
rm Miniconda2-latest-Linux-x86_64.sh && \  
conda install --yes conda && \  
conda config --add channels bioconda && \  
conda config --add channels r  
  
RUN conda install --yes \  
bedops \  
bioconductor-bsgenome.hsapiens.ucsc.hg19 \  
bioconductor-txdb.hsapiens.ucsc.hg19.knowngene \  
biopython \  
h5py \  
joblib \  
numpy \  
pandas \  
scipy \  
statsmodels \  
&& conda clean -yt  
  
# Get required Lua packages.  
# RUN /root/torch/install/bin/luarocks install cutorch  
# RUN /root/torch/install/bin/luarocks install cunn  
RUN /root/torch/install/bin/luarocks install hdf5  
  
# Bring DeepSEA source code into the image.  
RUN wget -q http://deepsea.princeton.edu/media/code/deepsea.v0.94.tar.gz &&
tar -zxvf deepsea.v0.94.tar.gz -C /root/ > /dev/null  
  
COPY rebuild_torch/rebuild_torch.sh /root/torch/  
  
WORKDIR /root/DeepSEA-v0.94/  

