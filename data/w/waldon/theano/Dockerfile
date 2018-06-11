FROM ubuntu:16.04  
  
MAINTAINER Waldon Chen <waldonchen@gmail.com>  
  
# Install dependencies  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
git \  
curl \  
rsync \  
unzip \  
libfreetype6-dev \  
libpng-dev \  
libzmq3-dev \  
pkg-config \  
libopenblas-dev \  
python \  
python-dev \  
python-pip \  
python-setuptools \  
python-nose \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN pip --no-cache-dir install \  
ipykernel \  
jupyter \  
matplotlib \  
numpy \  
scipy \  
&& \  
python -m ipykernel.kernelspec  
  
# Install bleeding-edge Theano  
RUN pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git  
  
# Set up notebook config.  
COPY jupyter_notebook_config.py /root/.jupyter/  
  
# Copy some notebooks.  
COPY notebooks /notebooks  
  
COPY run_jupyter.sh /  
  
# IPython  
EXPOSE 8888  
  
WORKDIR "/notebooks"  
  
CMD ["/run_jupyter.sh"]  

