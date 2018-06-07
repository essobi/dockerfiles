FROM ubuntu:14.04  
MAINTAINER Daniel Stanciulescu <daniel@creative-coding.ro>  
# Install build-essential, git, wget, python-dev, pip and other dependencies  
RUN apt-get update && apt-get install -y \  
build-essential \  
git \  
wget \  
curl \  
libfreetype6-dev \  
libpng12-dev \  
libzmq3-dev \  
libopenblas-dev \  
pkg-config \  
python-dev \  
python-pip \  
python-nose \  
python-numpy \  
python-scipy \  
python-sklearn \  
rsync \  
unzip \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
rm get-pip.py  
RUN pip \--no-cache-dir install \  
setuptools \  
ipykernel \  
jupyter \  
matplotlib \  
&& \  
python -m ipykernel.kernelspec  
  
# Upgrade matplotlib to a newer version  
RUN pip install \--no-cache \--upgrade matplotlib  
  
# Install bleeding-edge Theano  
RUN pip install \--no-cache-dir \--upgrade \--no-deps
git+git://github.com/Theano/Theano.git  
  
# Install bleeding-edge Lasagne  
RUN pip install \--no-cache-dir \--upgrade
https://github.com/Lasagne/Lasagne/archive/master.zip  
  
# Set up our notebook config.  
COPY jupyter_notebook_config.py /root/.jupyter/  
# Copy sample notebooks.  
COPY notebooks /notebooks  
  
# Jupyter has issues with being run directly:  
# https://github.com/ipython/ipython/issues/7062  
# We just add a little wrapper script.  
COPY run_jupyter.sh /  
  
# IPython  
EXPOSE 8888  
  
WORKDIR "/notebooks"  
CMD ["/run_jupyter.sh"]  

