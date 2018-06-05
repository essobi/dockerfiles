FROM python:2.7.11  
MAINTAINER dan.leehr@duke.edu  
  
# install LIBSVM.  
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
  
# Switch to non-root user  
RUN useradd -m svr  
USER svr  
  
ENV PATH $PATH:/opt/libsvm-${LIBSVM_VER}  
ADD requirements.txt /opt/predict-tf-binding/requirements.txt  
WORKDIR /opt/predict-tf-binding  
  
# Include libsvm python bindings in PYTHONPATH  
# These have no installer, so it's simplest to just update PYTHONPATH  
ENV PYTHONPATH /opt/libsvm-${LIBSVM_VER}/python  
  
# Install requirements as root  
USER root  
RUN pip install -r requirements.txt  
  
# switch back to svr  
USER svr  
ADD . /opt/predict-tf-binding/  
ENV PATH /opt/predict-tf-binding:$PATH  
CMD predict_tf_binding.py  

