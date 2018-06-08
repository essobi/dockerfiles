#FROM ubuntu:14.04  
FROM ipython/scipyserver  
  
MAINTAINER Pierre-Elouan Rethore <pire@dtu.dk>  
  
RUN mkdir /install  
WORKDIR /install/  
  
#RUN sudo apt-get update && apt-get install -y -q \  
# build-essential \  
# make \  
# gcc \  
# git \  
# python \  
# python-dev \  
# python-pip  
RUN git clone http://github.com/piredtu/WindFLO.git WindFLO  
  
WORKDIR /install/WindFLO/Python  
  
ADD . /install/WindFLO/Python  
  
RUN make pip_install  
RUN make  
  
CMD bash  

