FROM ubuntu:14.04  
MAINTAINER schwarty  
  
# Environment variables  
ENV TERM linux  
  
# Update repository  
RUN apt-get update  
RUN apt-get upgrade -y  
  
# Install packages  
RUN apt-get install -y git-core build-essential wget  
RUN apt-get install -y python2.7-dev  
RUN apt-get install -y cython  
RUN apt-get install -y python-numpy  
RUN apt-get install -y python-scipy  
RUN apt-get install -y python-pip  
RUN apt-get install -y python-zmq  
RUN apt-get install -y python-jinja2  
RUN apt-get install -y python-tornado  
RUN apt-get install -y python-sympy  
RUN apt-get install -y python-jsonschema  
RUN apt-get install -y python-json-pointer  
RUN apt-get install -y libfreetype6-dev  
  
# Install Python libraries from source  
RUN echo "cloning..."  
  
WORKDIR /  
  
RUN mkdir build  
WORKDIR build  
  
RUN git clone https://github.com/matplotlib/matplotlib.git  
RUN git clone https://github.com/scikit-learn/scikit-learn.git  
RUN git clone https://github.com/joblib/joblib.git  
RUN git clone https://github.com/ipython/ipython.git  
RUN git clone https://github.com/pydata/pandas.git  
  
RUN echo "building..."  
  
WORKDIR /build/matplotlib  
RUN python setup.py install  
  
WORKDIR /build/scikit-learn  
RUN python setup.py install  
  
WORKDIR /build/joblib  
RUN python setup.py install  
  
WORKDIR /build/ipython  
RUN python setup.py install  
  
WORKDIR /build/pandas  
RUN python setup.py install  
  
# Cleanup  
WORKDIR /  
RUN rm -rf /build  
RUN apt-get autoremove -y  
RUN apt-get clean all

