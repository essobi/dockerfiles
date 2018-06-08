FROM ubuntu:16.04  
MAINTAINER Henrik Holst <henrik.holst@frostbite.com>  
  
# Set the locale  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update --fix-missing && \  
apt-get install -y --no-install-recommends build-essential ca-certificates
curl git libglib2.0-0 libsm6 libxext6 libxrender1 && \  
apt-get install -y --no-install-recommends xserver-xorg-video-dummy x11vnc &&
\  
apt-get install -y --no-install-recommends libopenblas-dev && \  
apt-get install -y --no-install-recommends cmake zlib1g-dev libjpeg-dev xvfb
libav-tools xorg-dev libboost-all-dev libsdl2-dev && \  
apt-get install -y --no-install-recommends libsdl1.2-dev libsdl-gfx1.2-dev
libsdl-image1.2-dev cmake && \  
apt-get install -y --no-install-recommends unzip wget iputils-ping && \  
apt-get clean  
  
# Install tini  
ENV TINI_VERSION v0.13.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
RUN chmod +x /tini  
ENTRYPOINT ["/tini", "--"]  
  
# Install Miniconda3  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
curl -O https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
&& \  
/bin/bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/conda && \  
rm Miniconda3-latest-Linux-x86_64.sh  
  
ENV PATH /opt/conda/bin:$PATH  
  
RUN pip install --no-cache-dir --upgrade pip  
RUN pip install --no-cache-dir PyYAML  
  
# Setup our conda environment  
RUN conda install -y ipython matplotlib numpy pyopengl scipy swig dnspython
ruamel_yaml && \  
conda clean -iltp  
  
# Install ALE  
RUN git clone \--depth=1 https://github.com/mgbellemare/Arcade-Learning-
Environment && \  
cd Arcade-Learning-Environment && \  
cmake -DUSE_SDL=ON -DUSE_RLGLUE=OFF -DBUILD_EXAMPLES=ON . && \  
make -j 4 && \  
pip install --no-cache-dir . && \  
cd .. && \  
rm -rf Arcade-Learning-Environment  
  
# Install OpenAI Gym  
RUN pip install --no-cache-dir gym[atari]  
  
# Install Doom environment  
RUN pip install -U --no-cache-dir doom-py ppaquette-gym-doom  
  
# Install OpenCV (needed by some of our environments).  
RUN conda install -y -c https://conda.binstar.org/menpo opencv3 && \  
apt-get install -y --no-install-recommends libgtk2.0-0 && \  
apt-get clean  
  
# Install TensorFlow  
ENV TENSORFLOW_VERSION 0.11.0  
ENV TF_BINARY_URL
https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-${TENSORFLOW_VERSION}-cp35-cp35m-linux_x86_64.whl  
  
RUN pip --no-cache-dir install $TF_BINARY_URL  
  
# Install VNC  
ADD Xwrapper.config /etc/X11/Xwrapper.config  
ADD Xdummy /usr/local/bin/  
ADD jupyter_notebook_config.py /root/.jupyter/  
  
# Expose ports  
EXPOSE 5900 6006 8888  
# Start bash  
CMD [ "/bin/bash" ]  

