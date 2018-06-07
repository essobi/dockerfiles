ARG cuda_version=9.0  
ARG cudnn_version=7  
#FROM nvidia/cuda:${cuda_version}-cudnn${cudnn_version}-devel  
FROM nvidia/cuda:9.0-devel-ubuntu16.04  
# Pin CuDNN  
RUN apt-get update && apt-get install -y --allow-downgrades --no-install-
recommends \  
libcudnn7=7.0.5.15-1+cuda9.0 \  
libcudnn7-dev=7.0.5.15-1+cuda9.0  
RUN apt-mark hold libcudnn7 libcudnn7-dev  
  
# Supress warnings about missing front-end. As recommended at:  
# http://stackoverflow.com/questions/22466255/is-it-possibe-to-answer-dialog-
questions-when-installing-under-docker  
ARG DEBIAN_FRONTEND=noninteractive  
  
# Install system packages  
RUN apt-get update && apt-get install -y --no-install-recommends \  
bzip2 \  
g++ \  
git \  
graphviz \  
libgl1-mesa-glx \  
libhdf5-dev \  
openmpi-bin \  
wget \  
python3 \  
python3-pip \  
python3-venv \  
python3-dev \  
python3-setuptools \  
python3-tk  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
apt-utils git curl vim unzip openssh-client wget \  
build-essential cmake \  
libopenblas-dev  
  
RUN apt-get install -y --no-install-recommends \  
libjpeg8-dev libtiff5-dev libjasper-dev libpng12-dev \  
libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libgtk2.0-dev \  
liblapacke-dev checkinstall  
  
# Install Python packages and keras  
ENV NB_USER app  
ENV NB_UID 1000  
  
RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER && \  
mkdir -p /src && \  
mkdir -p /workspace && \  
chown $NB_USER /src && \  
chown $NB_USER /workspace  
  
RUN rm -rf /var/lib/apt/lists/*  
  
USER $NB_USER  
  
WORKDIR /workspace  
  
RUN pip3 install \  
sklearn_pandas \  
tensorflow-gpu==1.5.0  
  
RUN pip3 install \  
bcolz \  
h5py \  
matplotlib \  
mkl \  
nose \  
notebook \  
Pillow \  
pandas \  
pyyaml \  
scikit-learn \  
six \  
scipy \  
scikit-image \  
requests \  
opencv-python \  
theano \  
keras \  
kaggle  
  
RUN pip3 install\  
imgaug \  
numpy\  
Pillow \  
cython\  
h5py  
  
RUN pip3 install ipython  
RUN pip3 install
"git+https://github.com/philferriere/cocoapi.git#egg=pycocotools&subdirectory=PythonAPI"  
#ADD theanorc /home/keras/.theanorc  
#ENV PYTHONPATH='/src/:$PYTHONPATH'  
# Jupyter  
EXPOSE 8888  
# Tensorboard  
EXPOSE 6006  
  
ENV PATH "/home/app/.local/bin:$PATH"  
CMD jupyter notebook --port=8888 \--ip=0.0.0.0  

