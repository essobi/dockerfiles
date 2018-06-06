FROM ubuntu:14.04  
MAINTAINER Yi Jin <y.jin@me.com>  
  
RUN apt-get update && apt-get install -y git gcc build-essential  
WORKDIR /opt  
RUN git clone \--recursive https://github.com/dmlc/xgboost  
RUN cd xgboost; make -j4

