FROM nvidia/cuda:8.0-cudnn6-devel  
  
LABEL maintainer="Alejandro Valdes <alejandrovaldes@live.com>"  
  
ENV CONDA_DIR /opt/conda  
ENV PATH $CONDA_DIR/bin:$PATH  
  
RUN mkdir -p $CONDA_DIR && \  
echo export PATH=$CONDA_DIR/bin:'$PATH' > /etc/profile.d/conda.sh && \  
apt-get update && \  
apt-get install -y --no-install-recommends wget git libhdf5-dev g++ graphviz
openmpi-bin libgl1 bzip2 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
wget --no-check-certificate --quiet
http://repo.continuum.io/miniconda/Miniconda3-4.3.27-Linux-x86_64.sh && \  
/bin/bash /Miniconda3-4.3.27-Linux-x86_64.sh -f -b -p $CONDA_DIR && \  
rm Miniconda3-4.3.27-Linux-x86_64.sh  
  
ENV NB_USER keras  
ENV NB_UID 1000  
RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER && \  
mkdir -p $CONDA_DIR && \  
chown keras $CONDA_DIR -R && \  
mkdir -p /src && \  
chown keras /src  
  
ADD theanorc /home/keras/.theanorc  
  
ADD kerasrc /home/keras/.keras/keras.json  
  
RUN chown keras /home/keras/.theanorc && \  
chown keras /home/keras/.keras/keras.json  
  
USER keras  
  
RUN pip --no-cache-dir install --upgrade pip && \  
pip --no-cache-dir install tensorflow-gpu && \  
#pip --no-cache-dir install
https://cntk.ai/PythonWheel/GPU/cntk-2.2-cp36-cp36m-linux_x86_64.whl && \  
conda install Pillow scikit-learn pandas matplotlib mkl nose pyyaml six h5py
&& \  
conda install theano pygpu bcolz && \  
pip --no-cache-dir install sklearn_pandas && \  
pip --no-cache-dir install keras && \  
conda install -c menpo opencv3 && \  
pip --no-cache-dir install opencv-python && \  
conda clean -yt  
  
RUN git clone git://github.com/alevalv/retina-unet.git /src  
  
ENV KERAS_BACKEND tensorflow  
  
WORKDIR /src  

