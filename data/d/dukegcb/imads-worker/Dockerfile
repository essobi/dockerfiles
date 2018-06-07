FROM ubuntu:xenial  
MAINTAINER "Dan Leehr" dan.leehr@duke.edu  
  
RUN apt-get update && apt-get install -y \  
git \  
python python-pip \  
r-base  
  
### Step 1: Install the worker and its dependencies  
ADD requirements.txt /opt/tf-predictions-worker/  
WORKDIR /opt/tf-predictions-worker  
RUN pip install -r requirements.txt  
  
ADD . /opt/tf-predictions-worker/  
ENV PATH /opt/tf-predictions-worker/:$PATH  
  
### Step 2: Install LIBSVM, needed by predict-tf-binding  
# Makefile has no install target, so we compile and update PATH  
# Owned by root and placed in /opt  
ENV LIBSVM_VER 321  
RUN curl -SL https://github.com/cjlin1/libsvm/archive/v${LIBSVM_VER}.tar.gz |
tar -xzC /opt # makes /opt/libsvm-321  
WORKDIR /opt/libsvm-${LIBSVM_VER}  
RUN make  
  
# Build shared lib for python bindings  
WORKDIR /opt/libsvm-${LIBSVM_VER}/python  
RUN make  
  
# Install libsvm and python bindings  
# These have no installer so we place the library and python bindings manually  
RUN cp /opt/libsvm-${LIBSVM_VER}/libsvm.so* /usr/lib/  
RUN ldconfig  
RUN cp /opt/libsvm-${LIBSVM_VER}/python/*.py /usr/local/lib/python2.7/dist-
packages/  
  
### Step 3: Install Predict-TF-Binding from GitHub  
WORKDIR /opt/  
RUN git clone https://github.com/Duke-GCB/Predict-TF-Binding.git predict-tf-
binding  
RUN pip install -r /opt/predict-tf-binding/requirements.txt  
ENV PATH /opt/predict-tf-binding/:$PATH  
  
### Step 4: Install Predict-TF-Preference from GitHub  
WORKDIR /opt/  
RUN git clone https://github.com/Duke-GCB/Predict-TF-Preference.git predict-
tf-preference  
ENV PATH /opt/predict-tf-preference/:$PATH  
  
# Switch to non-root user  
RUN useradd -m worker  
USER worker  
  
CMD client.py  

