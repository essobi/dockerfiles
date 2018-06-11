FROM nvidia/cuda:7.5-cudnn5-devel  
  
MAINTAINER KaiyuShi <skyisno.1@gmail.com>  
  
# Pick up some TF dependencies  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
curl \  
libfreetype6-dev \  
libpng12-dev \  
libzmq3-dev \  
libssl-dev \  
pkg-config \  
python2.7 \  
python2.7-dev \  
rsync \  
software-properties-common \  
unzip \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Setup python2.7 as default  
RUN update-alternatives --install /usr/bin/python python /usr/bin/python2.7 10  
  
# Install python2.7  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
rm get-pip.py  
  
#install py packages  
RUN pip --no-cache-dir install \  
ipykernel \  
jupyter \  
matplotlib \  
numpy \  
scipy \  
sklearn \  
Pillow \  
pandas \  
Quandl \  
gym \  
&& \  
python -m ipykernel.kernelspec  
  
# Install pytorch GPU version. should update through pytorch update  
RUN curl -O
https://download.pytorch.org/whl/cu75/torch-0.1.10.post2-cp27-none-
linux_x86_64.whl && \  
pip install --no-cache-dir torch-0.1.10.post2-cp27-none-linux_x86_64.whl && \  
rm torch-0.1.10.post2-cp27-none-linux_x86_64.whl  
RUN pip install --no-cache-dir torchvision  
  
# --- ~ DO NOT EDIT OR DELETE BETWEEN THE LINES --- #  
# RUN ln -s /usr/bin/python3 /usr/bin/python#  
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

