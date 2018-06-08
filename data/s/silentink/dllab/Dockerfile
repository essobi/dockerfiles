FROM nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04  
MAINTAINER Silentink (https://github.com/david6686/my_dllab)  
# ==================================================================  
# module list  
# ------------------------------------------------------------------  
# python 3.6 (conda)  
# jupyter latest (pip)  
# pytorch latest (pip)  
# tensorflow 1.8.0 (pip)  
# theano 1.0.1 (conda)  
# keras latest (pip)  
# opencv latest (conda)  
# ==================================================================  
ENV TENSORFLOW_VERSION=1.8.0  
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8  
ENV PATH /opt/conda/bin:$PATH  
ENV TINI_VERSION v0.16.1  
ENV SHELL /usr/bin/fish  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/usr/bin/tini  
# ==================================================================  
# startup setup  
# ------------------------------------------------------------------  
RUN echo "deb http://developer.download.nvidia.com/compute/machine-
learning/repos/ubuntu1604/x86_64 /" > /etc/apt/sources.list.d/nvidia-ml.list
&&\  
APT_INSTALL=" apt-get install -y --no-install-recommends" && \  
PIP_INSTALL="pip install --no-cache-dir" && \  
GIT_CLONE="git clone --depth 1" && \  
CONDA="conda install -y" && \  
rm -rf /var/lib/apt/lists/* \  
/etc/apt/sources.list.d/cuda.list \  
/etc/apt/sources.list.d/nvidia-ml.list && \  
apt-get update --fix-missing && \  
# ==================================================================  
# apt-get  
# ------------------------------------------------------------------  
DEBIAN_FRONTEND=noninteractive $APT_INSTALL \  
wget \  
bzip2 \  
ca-certificates \  
curl \  
git \  
fish \  
cmake \  
vim \  
emacs \  
libjpeg-dev\  
libpng-dev \  
build-essential \  
unzip \  
zip \  
doxygen \  
software-properties-common \  
firefox \  
htop \  
&& \  
#setup emacs  
$GIT_CLONE https://github.com/syl20bnr/spacemacs ~/.emacs.d \  
&& \  
# ==================================================================  
# miniconda3  
# ------------------------------------------------------------------  
#install miniconda3  
wget --quiet
https://repo.continuum.io/miniconda/Miniconda3-4.4.10-Linux-x86_64.sh -O
~/miniconda.sh && \  
/bin/bash ~/miniconda.sh -b -p /opt/conda && \  
rm ~/miniconda.sh && \  
/opt/conda/bin/conda clean -tipsy && \  
ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \  
echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \  
echo "conda activate base" >> ~/.bashrc \  
&& \  
# ==================================================================  
# Install (pip) tensorflow keras pytorch  
# ------------------------------------------------------------------  
$PIP_INSTALL \  
tensorflow-gpu==$TENSORFLOW_VERSION \  
keras \  
h5py \  
http://download.pytorch.org/whl/cu90/torch-0.4.0-cp36-cp36m-linux_x86_64.whl \  
torchvision \  
jupyter \  
&& \  
# ==================================================================  
# Install (conda) theano sklearn scipy numpy ... ML package  
# ------------------------------------------------------------------  
DEBIAN_FRONTEND=noninteractive $CONDA \  
opencv \  
tqdm \  
dask \  
numpy \  
scikit-learn \  
matplotlib \  
Cython \  
scipy \  
theano \  
&& \  
# ==================================================================  
# Install Open MPI  
# ------------------------------------------------------------------  
mkdir /tmp/openmpi && \  
cd /tmp/openmpi && \  
wget https://www.open-
mpi.org/software/ompi/v3.0/downloads/openmpi-3.0.0.tar.gz && \  
tar zxf openmpi-3.0.0.tar.gz && \  
cd openmpi-3.0.0 && \  
./configure --enable-orterun-prefix-by-default && \  
make -j $(nproc) all && \  
make install && \  
ldconfig && \  
cd ~ &&\  
rm -rf /tmp/openmpi \  
&& \  
# ==================================================================  
# Install Horovod, temporarily using CUDA stubs  
# ------------------------------------------------------------------  
ldconfig /usr/local/cuda-9.0/targets/x86_64-linux/lib/stubs && \  
HOROVOD_GPU_ALLREDUCE=NCCL pip install --no-cache-dir horovod && \  
ldconfig \  
&& \  
# ==================================================================  
# Create a wrapper for OpenMPI to allow running as root by default  
# ------------------------------------------------------------------  
mv /usr/local/bin/mpirun /usr/local/bin/mpirun.real && \  
echo '#!/bin/bash' > /usr/local/bin/mpirun && \  
echo 'mpirun.real --allow-run-as-root "$@"' >> /usr/local/bin/mpirun && \  
chmod a+x /usr/local/bin/mpirun \  
&& \  
# Configure OpenMPI to run good defaults:  
# --bind-to none --map-by slot --mca btl_tcp_if_exclude lo,docker0  
echo "hwloc_base_binding_policy = none" >> /usr/local/etc/openmpi-mca-
params.conf && \  
echo "rmaps_base_mapping_policy = slot" >> /usr/local/etc/openmpi-mca-
params.conf && \  
echo "btl_tcp_if_exclude = lo,docker0" >> /usr/local/etc/openmpi-mca-
params.conf \  
&& \  
# Install OpenSSH for MPI to communicate between containers  
DEBIAN_FRONTEND=noninteractive $APT_INSTALL \  
openssh-client \  
openssh-server && \  
mkdir -p /var/run/sshd \  
&& \  
# Allow OpenSSH to talk to containers without asking for confirmation  
cat /etc/ssh/ssh_config | grep -v StrictHostKeyChecking >
/etc/ssh/ssh_config.new && \  
echo " StrictHostKeyChecking no" >> /etc/ssh/ssh_config.new && \  
mv /etc/ssh/ssh_config.new /etc/ssh/ssh_config \  
&& \  
# ==================================================================  
# config & cleanup  
# ------------------------------------------------------------------  
#fish setup  
sed -i -e "s/bin\/ash/usr\/bin\/fish/" /etc/passwd && \  
ldconfig && \  
apt-get clean && \  
apt-get autoremove && \  
chmod +x /usr/bin/tini  
# Set up notebook config  
# COPY jupyter_notebook_config.py /root/.jupyter/  
# Jupyter has issues with being run directly:
https://github.com/ipython/ipython/issues/7062  
# COPY run_jupyter.sh /root/  
# Expose Ports for TensorBoard (6006), Ipython (8888)  
EXPOSE 6006 8888  
# WORKDIR "/root"  
ENTRYPOINT [ "/usr/bin/tini", "--" ]  
# CMD [ "/bin/bash" ]  
CMD ["/usr/bin/fish"]  

