FROM ubuntu  
MAINTAINER Meagan Lang <langmm.astro@gmail.com>  
# Basic utilities  
RUN apt-get update \--fix-missing && apt-get install -y wget bzip2 ca-
certificates \  
libglib2.0-0 libxext6 libsm6 libxrender1 \  
gcc build-essential make cmake mpich \  
git mercurial subversion \  
emacs nano vim \  
screen \  
curl grep sed dpkg unzip \  
libgomp1  
  
# Anaconda python  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \  
wget \--quiet
https://3230d63b5fc54e62148e-c95ac804525aac4b6dba79b00b39d1d3.ssl.cf1.rackcdn.com/Anaconda2-4.0.0-Linux-x86_64.sh
&& \  
/bin/bash /Anaconda2-4.0.0-Linux-x86_64.sh -b -p /opt/conda && \  
rm /Anaconda2-4.0.0-Linux-x86_64.sh  
ENV PATH /opt/conda/bin:$PATH  
  
# Conda install python packages with conda support  
RUN conda update conda && \  
conda update ipython && \  
conda install ipython-notebook ipython-qtconsole \  
setuptools wheel \  
mpi4py h5py  
  
# Make sure pip is up to date  
RUN wget \--quiet https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py \--no-setuptools \--no-wheel && \  
pip install -U pip && \  
rm /get-pip.py  
# Install python packages not conda registered  
RUN pip install parse  
  
# http://bugs.python.org/issue19846  
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks
Python 3*, and that's not OK.  
ENV LANG C.UTF-8  
  
# yt  
# Install yt conda version  
# RUN conda install yt  
# Install yt dev branch  
RUN hg clone https://bitbucket.org/yt_analysis/yt && \  
cd yt && \  
hg up yt && \  
python setup.py develop && \  
cd ../  
  
# pynbody  
# Install pynbody stable release  
# RUN pip install pynbody  
# Install pynbody development  
RUN pip install git+git://github.com/pynbody/pynbody.git  
# RUN git clone https://github.com/pynbody/pynbody && \  
# cd pynbody && \  
# python setup.py install && \  
# cd ../  
WORKDIR /root  
  
CMD [ "/bin/bash" ]

