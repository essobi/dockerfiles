FROM ubuntu:16.04  
ENV LANG C.UTF-8  
RUN apt-get update && apt-get install -y python python-dev python3.5
python3.5-dev python3-pip virtualenv libssl-dev libpq-dev git build-essential
libfontconfig1 libfontconfig1-dev  
RUN pip3 install setuptools pip --upgrade --force-reinstall  
# Install Python 3 packages  
RUN pip3 install sklearn pandas  
  
# Install XGBoost library  
RUN git clone \--recursive https://github.com/dmlc/xgboost && \  
cd xgboost && \  
make -j4 && \  
cd python-package; python3 setup.py install  
COPY dataset.csv /dataset.csv

