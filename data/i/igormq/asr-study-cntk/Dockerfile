# Tag: nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04  
# Created: 2017-11-21T06:34:14.675603521Z  
# Label: com.nvidia.build.id: 41212533  
# Label: com.nvidia.build.ref: e0edb5359ecb7bd3d86f0c9bfa18c2260b741ebb  
# Label: com.nvidia.cuda.version: 9.0.176  
# Label: com.nvidia.cudnn.version: 7.0.4.31  
# Label: com.nvidia.nccl.version: 2.1.2  
# Ubuntu 16.04.5  
FROM
nvidia/cuda@sha256:33add9c50ab76b8f3a92187c0418ed600d5bea27690fda40711122fdc28ce2f4  
  
# Install system packages  
RUN apt-get update && apt-get install -y --no-install-recommends \  
autotools-dev \  
build-essential \  
curl \  
cmake \  
g++ \  
git \  
openmpi-bin \  
openssh-server \  
openssh-client \  
rsync \  
sudo \  
wget \  
sox \  
# ifconfig  
net-tools && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
  
## Install CNTK dependencies: MKLDNN and MKLML  
RUN mkdir /usr/local/mklml && \  
wget -q --no-check-certificate -O - https://github.com/intel/mkl-
dnn/releases/download/v0.12/mklml_lnx_2018.0.1.20171227.tgz | \  
tar -xzf - -C /usr/local/mklml && \  
wget -q --no-check-certificate -O - https://github.com/intel/mkl-
dnn/archive/v0.12.tar.gz | tar -xzf - && \  
cd mkl-dnn-0.12 && \  
ln -s /usr/local external && \  
mkdir -p build && \  
cd build && \  
cmake .. && \  
make && \  
make install && \  
cd ../.. && \  
rm -rf mkl-dnn-0.12  
ENV LD_LIBRARY_PATH /usr/local/lib:$LD_LIBRARY_PATH  
  
  
# Install Miniconda3  
ENV CONDA_DIR /opt/conda  
ENV PATH ${CONDA_DIR}/bin:$PATH  
  
RUN wget --quiet --no-check-certificate
https://repo.continuum.io/miniconda/Miniconda3-4.4.10-Linux-x86_64.sh && \  
echo "0c2e9b992b2edd87eddf954a96e5feae86dd66d69b1f6706a99bd7fa75e7a891
Miniconda3-4.4.10-Linux-x86_64.sh" | sha256sum -c - && \  
/bin/bash /Miniconda3-4.4.10-Linux-x86_64.sh -b -p $CONDA_DIR && \  
rm Miniconda3-4.4.10-Linux-x86_64.sh && \  
${CONDA_DIR}/bin/conda clean -tipsy && \  
ln -s ${CONDA_DIR}/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \  
echo ". ${CONDA_DIR}/etc/profile.d/conda.sh" >> ~/.bashrc && \  
echo "conda activate base" >> ~/.bashrc  
  
SHELL ["/bin/bash", "-c"]  
  
RUN conda update -y -n base conda && \  
pip install --upgrade pip  
  
# cntk-gpu env  
RUN conda create -n cntk-gpu && \  
source activate cntk-gpu && \  
conda install -y python=3.6 \  
h5py \  
jupyter \  
matplotlib \  
numpy \  
pandas \  
pillow \  
pytables \  
pyyaml \  
scikit-learn \  
scipy && \  
conda install opencv=3.1 -c menpo && \  
pip install easydict num2words librosa unidecode wget sox && \  
pip install cntk-gpu && \  
conda clean -tipsy  
  
# cntk-cpu env  
RUN conda create -y -n cntk-cpu --clone cntk-gpu && \  
source activate cntk-cpu && \  
pip uninstall -y cntk-gpu && \  
pip install cntk --upgrade && \  
conda clean -tipsy  
  
RUN mkdir -p /src  
WORKDIR /src  
  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod 777 '/entrypoint.sh'  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 8888  
CMD jupyter notebook --port=8888 --ip=0.0.0.0 --allow-root

