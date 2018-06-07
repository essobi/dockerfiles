# Start with Ubuntu base image  
FROM ubuntu:14.04  
MAINTAINER Brad Erickson <bje@mayo.edu>  
  
# Install wget and build-essential  
RUN apt-get update && apt-get install -y \  
build-essential wget g++ curl libssl-dev apache2-utils git libxml2-dev sshfs  
  
# Change to the /tmp directory  
RUN cd /tmp && \  
# Download run file  
wget
http://developer.download.nvidia.com/compute/cuda/7.5/Prod/local_installers/cuda_7.5.18_linux.run
&& \  
# Make the run file executable and extract  
chmod +x cuda_*_linux.run && ./cuda_*_linux.run -extract=`pwd` && \  
# Install CUDA drivers (silent, no kernel)  
./NVIDIA-Linux-x86_64-*.run -s --no-kernel-module && \  
# Install toolkit (silent)  
./cuda-linux64-rel-*.run -noprompt && \  
# Clean up  
rm -rf *  
  
# Add to path  
ENV PATH=/usr/local/cuda/bin:$PATH \  
LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH \  
CUDA_REPO_PKG=cuda-repo-ubuntu1404_6.5-14_amd64.deb  
  
RUN wget
http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1404/x86_64/$CUDA_REPO_PKG
&& \  
dpkg -i $CUDA_REPO_PKG  
  
# Install cuDNN v4  
ENV ML_REPO_PKG=nvidia-machine-learning-repo_4.0-2_amd64.deb  
RUN wget http://developer.download.nvidia.com/compute/machine-
learning/repos/ubuntu1404/x86_64/$ML_REPO_PKG && \  
dpkg -i $ML_REPO_PKG && \  
apt-get update && apt-get install -y libcudnn4 libcudnn4-dev  
  
RUN apt-get update && apt-get install -y \  
libopenblas-dev \  
python-dev \  
python-pip \  
python-nose \  
python-numpy \  
python-scipy  
  
# Set CUDA_ROOT  
ENV CUDA_ROOT /usr/local/cuda/bin  
# Install bleeding-edge Theano  
RUN pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git  
# Set up .theanorc for CUDA  
RUN echo
"[global]\ndevice=gpu\nfloatX=float32\noptimizer_including=cudnn[lib]\ncnmem=1\n[nvcc]\nfastmath=True"
> /root/.theanorc  
  
# Install dependencies  
RUN apt-get update && apt-get install -y \  
libhdf5-dev \  
python-h5py \  
python-yaml  
  
# Upgrade six  
RUN pip install --upgrade six  
  
# Clone Keras repo and move into it  
RUN cd /root && git clone https://github.com/fchollet/keras.git && cd keras &&
\  
# Install  
python setup.py install  
  
#
------------------------------------------------------------------------------  
# Install Node.js  
# RUN curl -sL https://deb.nodesource.com/setup | bash -  
# RUN apt-get install -y nodejs  
#
------------------------------------------------------------------------------  
# Install Cloud9  
# RUN git clone https://github.com/c9/core.git /cloud9  
# WORKDIR /cloud9  
# RUN scripts/install-sdk.sh  
# Tweak standlone.js conf  
# RUN sed -i -e 's_127.0.0.1_0.0.0.0_g' /cloud9/configs/standalone.js  
# Add supervisord conf  
# RUN mkdir /etc/supervisor && mkdir /etc/supervisor/conf.d  
# RUN echo '[program:cloud9]\ncommand = node /cloud9/server.js --listen
0.0.0.0 --port 80 -w /workspace\ndirectory = /cloud9\nuser = root\nautostart =
true\nautorestart = true\nstdout_logfile =
/var/log/supervisor/cloud9.log\nstderr_logfile =
/var/log/supervisor/cloud9_errors.log\nenvironment = NODE_ENV="production"\n'
> /etc/supervisor/conf.d/cloud9.conf  
#
------------------------------------------------------------------------------  
# Add volumes  
RUN mkdir /workspace  
VOLUME /workspace  
  
#
------------------------------------------------------------------------------  
# Clean up APT when done.  
# RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
#
------------------------------------------------------------------------------  
# Expose ports.  
# EXPOSE 80  
# EXPOSE 3000  
#
------------------------------------------------------------------------------  
# Start supervisor, define default command.  
# CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]  
CMD ["/bin/bash"]  
  

