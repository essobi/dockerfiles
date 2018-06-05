# Start with cuDNN base image  
FROM nvidia/cuda:7.5-cudnn5-devel-centos7  
MAINTAINER Jonathan Meyer <jon@gisjedi.com>  
  
LABEL \  
VERSION="0.9.0-7.5" \  
RUN="nvidia-docker run -it appliedis/theano-cuda:0.9.0-7.5 nvidia-smi" \  
SOURCE="https://github.com/appliedis/dockerfiles" \  
DESCRIPTION="Prepackaged theano with CUDA on CentOS" \  
CLASSIFICATION="UNCLASSIFIED"  
  
# Install git, wget, python-dev, pip, BLAS + LAPACK and other dependencies  
RUN yum install -y epel-release && yum install -y \  
gcc-gfortran \  
git \  
wget \  
lapack-devel \  
openblas-devel \  
python-devel \  
python-pip \  
python-nose \  
numpy \  
scipy  
  
# Set CUDA_ROOT  
ENV CUDA_ROOT /usr/local/cuda/bin  
# Install bleeding-edge Theano  
RUN pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git  
RUN pip install --upgrade pip six  
# Set up .theanorc for CUDA  
RUN echo
"[global]\ndevice=gpu\nfloatX=float32\noptimizer_including=cudnn\n[lib]\ncnmem=0.1\n[nvcc]\nfastmath=True"
> /root/.theanorc  

