FROM ubuntu:14.04  
MAINTAINER Adrien Lemaire "dori@alpacadb.com"  
# System packages  
RUN apt-get update && \  
apt-get install -y build-essential wget vim g++ && \  
apt-get install -y python-pip python-dev && \  
apt-get install -y libblas-dev libatlas-dev libatlas-base-dev liblapack-dev &&
\  
apt-get install -y gfortran libpq-dev libjpeg-dev && \  
apt-get update && \  
apt-get install -y libopencv-dev --fix-missing  
  
# Python requirements  
RUN easy_install -U pip && \  
pip install Cython==0.20.2 && \  
pip install Pillow==2.7.0 && \  
pip install numpy==1.9.1 && \  
pip install scipy==0.14.0 && \  
pip install scikit-image==0.10.1 && \  
pip install matplotlib==1.4.3 && \  
pip install gevent==1.0.1 && \  
pip install mprpc==0.1.2 && \  
pip install joblib==0.8.4 && \  
pip install pika==0.9.14 && \  
pip install fluent-logger==0.3.4 && \  
pip install psycopg2==2.5.4  

