FROM nvidia/cuda:8.0-cudnn5-devel  
  
MAINTAINER J Lovitt <lovi9573@hotmail.com>  
  
# Pick up some TF dependencies  
RUN apt-get -y update && apt-get install -y --no-install-recommends \  
build-essential \  
curl \  
libfreetype6-dev \  
libpng12-dev \  
libzmq3-dev \  
pkg-config \  
rsync \  
software-properties-common \  
unzip \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
##############################################################################  
# anaconda python  
##############################################################################  
# Install Anaconda  
RUN apt-get update && \  
apt-get install -y wget bzip2 ca-certificates libmysqlclient-dev && \  
rm -rf /var/lib/apt/lists/*  
  
RUN wget --quiet
https://repo.continuum.io/archive/Anaconda3-4.2.0-Linux-x86_64.sh && \  
/bin/bash Anaconda3-4.2.0-Linux-x86_64.sh -b -p /opt/conda && \  
rm Anaconda3-4.2.0-Linux-x86_64.sh  
  
ENV PATH /opt/conda/bin:$PATH  
  
# change default encoding  
RUN echo "import sys\n\  
sys.setdefaultencoding('utf-8')" >> /opt/conda/lib/python3.5/sitecustomize.py  
  
#Follow up with keras and other desired packages not included in anaconda by
default  
RUN conda install -y seaborn pillow pyyaml hdf5  
  
RUN pip install --upgrade pip  
  
RUN pip install wordcloud  
  
##############################################################################  
# Tensorflow  
##############################################################################  
# Install TensorFlow GPU version.  
RUN pip --no-cache-dir install \  
https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-0.12.1-cp35-cp35m-linux_x86_64.whl  
  
  
##############################################################################  
# keras  
##############################################################################  
RUN pip install keras  
  
##############################################################################  
#nltk data  
##############################################################################  
RUN python -m nltk.downloader book  
  
# IPython  
EXPOSE 8888  
  
WORKDIR "/notebooks"  
  
CMD jupyter notebook --no-browser --ip=0.0.0.0  

