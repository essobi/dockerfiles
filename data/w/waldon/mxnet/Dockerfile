# Start with Ubuntu base image  
FROM kaixhin/mxnet:latest  
MAINTAINER Waldon Chen <waldonchen@gmail.com>  
  
# Install build-essential, git and other dependencies  
RUN apt-get update && apt-get install -y --no-install-recommends \  
unzip \  
python-pip \  
python-nose \  
libfreetype6-dev \  
libpng-dev \  
libzmq3-dev \  
pkg-config  
  
# Install jupyter notebook  
RUN pip install \  
ipykernel \  
jupyter \  
matplotlib \  
numpy \  
scipy \  
&& \  
python -m ipykernel.kernelspec  
  
# Set up notebook config.  
COPY jupyter_notebook_config.py /root/.jupyter/  
  
# Copy some notebooks.  
COPY notebooks /notebooks  
  
COPY run_jupyter.sh /  
  
# IPython  
EXPOSE 8888  
WORKDIR "/notebooks"  
  
CMD ["/run_jupyter.sh"]  

