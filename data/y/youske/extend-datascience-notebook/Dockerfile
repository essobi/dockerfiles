FROM jupyter/datascience-notebook  
MAINTAINER youske <youske@gmail.com>  
USER root  
RUN apt-get update -y && apt-get install -y openssh-client autossh git golang
libtool make libffi-dev libzmq3-dev autoconf pkg-config && \  
cd /tmp && git clone https://github.com/zeromq/czmq && \  
cd czmq && ./autogen.sh && ./configure && make && make install  
  
USER $NB_USER  
RUN cd /tmp && \  
conda install -c conda-forge -f ruby numpy scipy cython numba paramiko
requests invoke && \  
conda install -c ioam -f holoviews bokeh plotly seaborn && \  
pip install -q param pyyaml py_d3 ansible testinfra && \  
pip install -q https://github.com/ipython-
contrib/jupyter_contrib_nbextensions/tarball/master && \  
pip install -q jupyter_nbextensions_configurator jupyter_dashboards
jupyterthemes ipywidgets bash_kernel remote_ikernel pivottablejs  
  
RUN wget -q 'https://github.com/pdonorio/RISE/archive/master.tar.gz' -O - |
tar zxf - && \  
cd RISE-master && python3 setup.py install && cd .. && \  
#go get github.com/fabian-z/gopherlab && \  
npm install -g ijavascript && \  
jupyter dashboards quick-setup --sys-prefix && \  
jupyter nbextensions_configurator enable --user && \  
jupyter contrib nbextension install --user && \  
python -m bash_kernel.install --user && \  
gem install cztop iruby nyaplot rubyvis pry awesome_print serverspec
infrataster && \  
iruby register --force  
  

