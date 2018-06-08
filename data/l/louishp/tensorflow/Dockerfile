FROM ubuntu:16.04  
  
MAINTAINER Craig Citro <craigcitro@google.com>  
# Pick up some TF dependencies  
RUN apt-get update && apt-get install -y \--no-install-recommends \  
build-essential \  
curl \  
libfreetype6-dev \  
libpng12-dev \  
libzmq3-dev \  
pkg-config \  
python \  
python-dev \  
rsync \  
software-properties-common \  
unzip \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
rm get-pip.py  
RUN pip \--no-cache-dir install \  
ipykernel \  
jupyter \  
matplotlib \  
numpy \  
scipy \  
sklearn \  
Pillow \  
&& \  
python -m ipykernel.kernelspec  
  
RUN pip \--no-cache-dir install
http://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.12.1-cp27-none-
linux_x86_64.whl  
  
# RUN ln -s /usr/bin/python3 /usr/bin/python#  
# Set up our notebook config.  
COPY jupyter_notebook_config.py /root/.jupyter/  
# Copy sample notebooks.  
COPY notebooks /notebooks  
  
# Jupyter has issues with being run directly:  
# https://github.com/ipython/ipython/issues/7062  
# We just add a little wrapper script.  
COPY run_jupyter.sh /  
  
# TensorBoard  
EXPOSE 6006  
# IPython  
EXPOSE 8888  
  
WORKDIR "/notebooks"  
CMD ["/run_jupyter.sh"]  

