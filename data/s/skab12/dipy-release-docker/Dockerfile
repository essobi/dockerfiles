FROM ubuntu:16.04  
MAINTAINER Serge Koudoro <skab12@gmail.com>  
  
RUN apt-get update && apt-get install -y python-pip  
RUN pip install --upgrade pip setuptools  
RUN pip install numpy cython scipy matplotlib h5py nibabel  
RUN pip install cvxpy scikit-learn  
RUN pip install dipy  
  
ENV PYTHONPATH /usr/local/lib/python2.7/dist-packages  
  
RUN ldconfig  
  

