FROM python:2.7  
MAINTAINER Wasnot <wasnot@example.com>  
RUN \  
pip install -U setuptools pip && \  
pip install chainer==1.6.2 && \  
pip install scipy==0.15.1 && \  
pip install scikit-learn==0.17.1 && \  
pip install pandas==0.18.1  
  
RUN \  
apt-get update && apt-get upgrade -y && \  
apt-get install unzip && \  
apt-get install cmake -y && \  
wget http://www.cs.ubc.ca/research/flann/uploads/FLANN/flann-1.8.4-src.zip -O
/tmp/flann.zip && \  
unzip /tmp/flann.zip -d /tmp/ && \  
mkdir /tmp/flann-1.8.4-src/build && \  
cd /tmp/flann-1.8.4-src/build && \  
cmake .. && \  
make && \  
make install && \  
rm /tmp/flann.zip && \  
rm -r /tmp/flann-1.8.4-src && \  
cd /  
  

