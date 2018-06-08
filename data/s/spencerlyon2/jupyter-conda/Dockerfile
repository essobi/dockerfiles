FROM spencerlyon2/jupyter-base  
  
MAINTAINER Spencer Lyon <spencerlyon2@gmail.com>  
  
# use apt-get to install stuff for python 2  
RUN apt-get -y install python-mpi4py cython python-mako libgeos-dev gfortran  
  
RUN apt-get -y build-dep \  
python-numpy python-scipy \  
python-matplotlib python-pandas \  
python-sympy python-nose2  
  
RUN pip install \  
numpy scipy matplotlib pandas sympy nose2 \  
plotly shapely mpld3 terminado quantecon --upgrade  
  
# Install miniconda for python 3  
RUN wget --quiet http://repo.continuum.io/miniconda/Miniconda3-latest-
Linux-x86_64.sh && \  
bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/miniconda && \  
rm Miniconda3-latest-Linux-x86_64.sh && \  
chmod -R a+rx /opt/miniconda  
  
# add conda and its python to front of the path  
ENV PATH /opt/miniconda/bin:$PATH  
  
# Install PyData modules and IPython dependencies for python 3  
RUN conda update \--quiet --yes conda && conda clean -y -t && \  
conda install --quiet --yes numpy scipy pandas matplotlib cython pyzmq scikit-
learn seaborn six statsmodels pip tornado jinja2 sphinx pygments nose readline
sqlalchemy terminado numba && \  
conda clean -y -t && \  
pip install quantecon  
  
# Set up IPython kernel  
RUN pip install file:///srv/ipython && \  
rm -rf /usr/local/share/jupyter/kernels/* && \  
python2 -m IPython kernelspec install-self && \  
python -m IPython kernelspec install-self  

