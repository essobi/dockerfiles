# specifiy base image  
FROM python:3  
# provide creator/maintainer of this Dockerfile  
MAINTAINER chris vela <info@christophvel.com>  
  
# Update the sources list  
RUN apt-get update  
  
RUN apt-get install -y libfreetype6-dev && \  
apt-get install -y libglib2.0-0 \  
libxext6 \  
libsm6 \  
libxrender1 \  
libblas-dev \  
liblapack-dev \  
vim \  
gfortran \  
libfontconfig1 --fix-missing  
  
RUN pip install matplotlib \  
seaborn \  
pandas \  
numpy \  
scipy \  
sklearn \  
python-dateutil \  
gensim \  
comet_ml  
  
COPY predictor /root/ad_fraud  

