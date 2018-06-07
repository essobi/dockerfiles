FROM nvidia/cuda:8.0-cudnn5-devel  
MAINTAINER Yong Zhuang <jazz14jazz@gmail.com>  
  
RUN bash Miniconda2-latest-Linux-x86 64.sh  
RUN ~/miniconda2/bin/conda install numpy scipy mkl nose sphinx pydot-ng  
  
RUN pip install Theano[test,doc]  
RUN pip install Cython  
RUN pip install -U https://github.com/Theano/Theano/archive/master.zip  
RUN pip install -U https://github.com/Lasagne/Lasagne/archive/master.zip  
RUN pip install -U scikit-learn  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
cmake \  
git \  
wget \  
libatlas-base-dev \  
libboost-all-dev \  
libgflags-dev \  
libgoogle-glog-dev \  
libhdf5-serial-dev \  
libleveldb-dev \  
liblmdb-dev \  
libopencv-dev \  
libprotobuf-dev \  
libsnappy-dev \  
protobuf-compiler \  
python-dev \  
python-numpy \  
python-pip \  
python-nose\  
python-numpy \  
nano \  
python-scipy && \  
rm -rf /var/lib/apt/lists/*  
RUN pip install jupyter  
RUN jupyter notebook --generate-config  
RUN echo "c.NotebookApp.password =
u'sha1:ec5027913427:d9cca9103f70eb7b4754f4a819e177dee0a8c367'" >>
~/.jupyter/jupyter_notebook_config.py  
EXPOSE 8888  
CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0"]  
  

