FROM simonbiggs/jupyter-boilerplate  
  
MAINTAINER Simon Biggs <mail@simonbiggs.net>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get -y upgrade  
  
# Python 2 and 3 SciPy stack and more  
RUN apt-get -y install \  
python-mpi4py python3-mpi4py \  
cython cython3 \  
python-mako python3-mako \  
libgeos-dev gfortran  
  
RUN apt-get -y build-dep \  
python-numpy python-scipy \  
python-matplotlib python-pandas \  
python-sympy python-nose2  
  
RUN pip install \  
numpy scipy matplotlib pandas sympy nose2 \  
plotly shapely mpld3 terminado --upgrade  
  
RUN pip3 install \  
numpy scipy matplotlib pandas sympy nose2 \  
plotly shapely mpld3 terminado --upgrade  

