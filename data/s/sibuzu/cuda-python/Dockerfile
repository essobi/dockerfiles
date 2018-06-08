FROM sibuzu/cuda-base  
  
# Install pip  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
rm get-pip.py  
# Add SNI support to Python  
RUN pip \--no-cache-dir install \  
pyopenssl \  
ndg-httpsclient \  
pyasn1  
  
# Install useful Python packages using apt-get to avoid version
incompatibilities with Tensorflow binary  
# especially numpy, scipy, skimage and sklearn (see
https://github.com/tensorflow/tensorflow/issues/2034)  
RUN apt-get update && apt-get install -y \  
python-numpy \  
python-scipy \  
python-nose \  
python-h5py \  
python-skimage \  
python-matplotlib \  
python-pandas \  
python-sklearn \  
python-sympy \  
&& \  
apt-get clean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR "/root"  
CMD ["/bin/bash"]  

