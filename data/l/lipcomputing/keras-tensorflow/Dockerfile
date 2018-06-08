# docker build --no-cache=true -t keras-tf -f docker-keras-tf .  
FROM tensorflow/tensorflow:1.5.0  
LABEL maintainer="Mario David <mariojmdavid@gmail.com>"  
  
ENV KERAS_BACKEND tensorflow  
ENV ROOTSYS /usr/local/root  
ENV PATH $ROOTSYS/bin:$PATH  
ENV PYTHONPATH $ROOTSYS/lib:$PYTHONPATH  
ENV LD_LIBRARY_PATH $ROOTSYS/lib:$LD_LIBRARY_PATH  
  
RUN mkdir -p /tmp/setup && \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
git \  
libxpm4 \  
libtbb2 \  
root-plugin-graf2d-asimage \  
tar \  
wget \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN cd /usr/local && \  
wget https://root.cern.ch/download/root_v6.12.06.Linux-
ubuntu16-x86_64-gcc5.4.tar.gz && \  
tar zxvf root_v6.12.06.Linux-ubuntu16-x86_64-gcc5.4.tar.gz && \  
rm -f /usr/local/root_v6.12.06.Linux-ubuntu16-x86_64-gcc5.4.tar.gz && \  
pip install seaborn && \  
pip install rootpy && \  
pip install metakernel zmq && \  
pip install keras && \  
git clone https://github.com/GilesStrong/ML_Tutorials.git
/notebooks/ML_Tutorials && \  
mkdir /notebooks/ML_Tutorials/data && \  
cd /notebooks/ML_Tutorials/data && \  
wget https://cernbox.cern.ch/index.php/s/ENW3iemn2qvku5y/download -O
csv_data.tgz && \  
tar -zxvf csv_data.tgz && \  
rm csv_data.tgz && \  
cd ../../../  
  
EXPOSE 8888  
WORKDIR "/notebooks"  
CMD ["/run_jupyter.sh", "--allow-root"]  
  

