# docker build -t lucsorel/zeromq-bindings:ubuntu15.10-zeromq4.1.x-scikit-
learn0.17.x .  
FROM ubuntu:15.10  
MAINTAINER Luc Sorel  
  
# installs ZeroMQ, then its Python binding and the scikit-learn environment  
RUN apt-get update && apt-get install -y \--no-install-recommends software-
properties-common && \  
add-apt-repository -y ppa:chris-lea/zeromq && \  
add-apt-repository -y ppa:chris-lea/libpgm && \  
apt-get update && \  
apt-get install -y \--no-install-recommends libzmq3 libzmq3-dev python python-
dev make gcc g++ python-numpy python-scipy python-matplotlib ipython ipython-
notebook python-pandas python-sympy python-nose && \  
apt-get install -y \--no-install-recommends python-pip && \  
pip install -U pyzmq scikit-learn && \  
apt-get remove -y python-dev python-pip make gcc g++ && \  
apt-get autoremove -y  

