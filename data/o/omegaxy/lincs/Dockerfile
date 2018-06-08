# Start with Ubuntu base image  
FROM ubuntu:16.04  
MAINTAINER Hong Hao <omeganju@gmail.com>  
# Install python  
RUN apt-get update && apt install -y \--no-install-recommends \  
curl \  
python \  
libhdf5-serial-dev \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Install pip  
RUN curl -O -k https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
rm get-pip.py  
# Install python extension packages  
RUN pip \--no-cache-dir install \  
ipykernel \  
jupyter \  
matplotlib \  
numpy \  
scipy \  
scikit-learn \  
theano \  
metric-learn \  
tables \  
&& \  
python -m ipykernel.kernelspec  
  
# Set up notebook config.  
COPY jupyter_notebook_config.py /root/.jupyter/  
# Copy sample notebooks and initial script  
COPY notebooks /notebooks  
COPY run_jupyter.sh /  
  
# Ipython port  
EXPOSE 8888  
  
WORKDIR "/notebooks"  
CMD ["/run_jupyter.sh"]  

