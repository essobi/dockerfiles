FROM hephaex:ubuntu  
MAINTAINER Mario Cho <hephaex@gmail.com>  
# dependencies check up  
RUN apt-get update && apt-get install -y \--no-install-recommends \  
build-essential \  
curl \  
libfreetype6-dev \  
libpng12-dev \  
libzmq3-dev \  
pkg-config \  
python3 \  
python3-dev \  
rsync \  
software-properties-common \  
unzip \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \  
python3 get-pip.py && \  
rm get-pip.py  
RUN pip3 \--no-cache-dir install \  
bs4 \  
h5py \  
ipykernel \  
jupyter \  
lxml \  
matplotlib \  
numpy \  
scipy \  
sklearn \  
pandas \  
Pillow \  
plotly && \  
python3 -m ipykernel.kernelspec  
  
# Install TensorFlow CPU version from central repo  
RUN pip3 \--no-cache-dir install \  
https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.7-cp36-cp36m-linux_x86_64.whl  
  
#
https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.6-cp36-cp36m-linux_x86_64.whl  
#
https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.5-cp36-cp36m-linux_x86_64.whl  
#
https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.4.1-cp34-cp34m-linux_x86_64.whl  
#
https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.3.0-cp27-none-
linux_x86_64.whl  
#
https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.2.1-cp34-cp34m-linux_x86_64.whl  
#
http://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.1.0-cp34-cp34m-linux_x86_64.whl  
#
https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.1.0-cp27-none-
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
  
# IPython notebook  
EXPOSE 8888  
  
WORKDIR "/notebooks"  
CMD ["/run_jupyter.sh", "--allow-root"]  

