FROM ubuntu:16.04  
  
MAINTAINER Arjun Sreekumar <ajsrk1207@gmail.com>  
  
# PyTorch Dependencies -  
# 1. build-essential  
# 2. cmake  
# 3. git  
# 4. curl  
# 5. vim  
# 6. ca-certificates  
# 7. libnccl2=2.0.5-2+cuda8.0  
# 8. libnccl-dev=2.0.5-2+cuda8.0  
# 9. libjpeg-dev  
# 10. libpng-dev  
# 11. conda install - numpy pyyaml scipy ipython mkl  
# 12. conda install -c pytorch pytorch torchvision magma-cuda80  
# Tensorflow Dependencies -  
# 1. build-essential  
# 2. curl  
# 3. libfreetype6-dev  
# 4. libpng12-dev  
# 5. libzmq3-dev  
# 6. pkg-config  
# 7. python  
# 8. python-dev  
# 9. rsync  
# 10. software-properties-common  
# 11. unzip  
# 12. conda install pip jupyter Pillow h5py ipykernel  
# 13. conda install -c conda-forge matplotlib numpy pandas scipy  
# Mayavi Dependencies -  
# 1. mesa-utils  
# 2. libglu1-mesa  
# 3. libqtgui4  
  
ENV LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 LANGUAGE=en_US.UTF-8  
  
ENV PATH /opt/conda/bin:$PATH  
  
RUN apt-get update --fix-missing && \  
apt-get install -y --no-install-recommends wget bzip2 ca-certificates \  
mesa-utils libglu1-mesa libqtgui4 \  
git mercurial subversion \  
build-essential cmake curl vim ca-certificates \  
libjpeg-dev libpng-dev \  
libfreetype6-dev libzmq3-dev pkg-config python-dev rsync software-properties-
common unzip && \  
\  
rm -rf /var/lib/apt/lists/* && \  
\  
echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget --quiet
https://repo.continuum.io/miniconda/Miniconda3-4.3.30-Linux-x86_64.sh -O
~/miniconda.sh && \  
/bin/bash ~/miniconda.sh -b -p /opt/conda && \  
rm ~/miniconda.sh &&\  
\  
apt-get clean &&\  
conda install -y -c conda-forge numpy pandas matplotlib scipy scikit-learn
scikit-image qt vtk pyvtk pyside envisage mayavi && \  
conda install -y -c ajsrk traitsui && \  
conda install -y -c menpo opencv3 && \  
conda install -y pyyaml pip mkl jupyter Pillow h5py && \  
conda install -y -c pytorch pytorch torchvision && \  
pip --no-cache-dir install \  
https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.4.1-cp36-cp36m-linux_x86_64.whl  
  
CMD [ "/bin/bash" ]  

