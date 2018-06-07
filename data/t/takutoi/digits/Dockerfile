FROM nvidia/cuda:9.0-cudnn7-devel  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN apt-get install -y --no-install-recommends freeglut3 freeglut3-dev
libopenmpi-dev  
RUN apt-get install -y --no-install-recommends build-essential cmake git
gfortran libatlas-base-dev libboost-all-dev libgflags-dev libgoogle-glog-dev
libhdf5-serial-dev libleveldb-dev liblmdb-dev libopencv-dev libprotobuf-dev
libsnappy-dev protobuf-compiler python-all-dev python-dev python-h5py python-
matplotlib python-numpy python-opencv python-pil python-pip python-protobuf
python-scipy python-skimage python-sklearn  
RUN apt-get install -y --no-install-recommends graphviz python-tk python-flask
python-flaskext.wtf python-gevent  
RUN apt-get install -y vim wget doxygen  
RUN apt-get install -y python-setuptools  
RUN pip install --upgrade pip  
  
ENV CUDA_PATH /usr/local/cuda  
  
RUN mkdir -p /home/caffe  
ENV CAFFE_ROOT /home/caffe  
RUN git clone https://github.com/NVIDIA/caffe.git ${CAFFE_ROOT}  
RUN pip install -r ${CAFFE_ROOT}/python/requirements.txt  
RUN cat ${CAFFE_ROOT}/python/requirements.txt | xargs -n1 pip install  
RUN mkdir -p ${CAFFE_ROOT}/build  
ENV NVML_LIBRARY_PATH /usr/local/cuda-9.0/lib64/stubs/libnvidia-ml.so  
RUN cd ${CAFFE_ROOT}/build && cmake -DNVML_LIBRARY=${NVML_LIBRARY_PATH} ..  
RUN cd ${CAFFE_ROOT}/build && make -j4  
  
RUN apt-get update  
RUN apt-get install -y libreadline-dev sudo  
RUN apt-get install -y --no-install-recommends software-properties-common  
ENV TORCH_ROOT /home/torch  
ENV TORCH_NVCC_FLAGS="-D__CUDA_NO_HALF_OPERATORS__"  
ENV TORCH_CUDA_ARCH_LIST="3.0;3.5;5.0;5.2;6.0;6.1;7.0"  
RUN git clone https://github.com/torch/distro.git $TORCH_ROOT \--recursive  
RUN cd ${TORCH_ROOT} && ./install-deps && ./install.sh -b  
RUN source ~/.bashrc  
RUN ${TORCH_ROOT}/install/bin/luarocks install tds  
RUN ${TORCH_ROOT}/install/bin/luarocks install
"https://raw.github.com/deepmind/torch-hdf5/master/hdf5-0-0.rockspec"  
RUN ${TORCH_ROOT}/install/bin/luarocks install
"https://raw.github.com/Neopallium/lua-pb/master/lua-pb-scm-0.rockspec"  
RUN ${TORCH_ROOT}/install/bin/luarocks install lightningmdb 0.9.18.1-1
LMDB_INCDIR=/usr/include LMDB_LIBDIR=/usr/lib/x86_64-linux-gnu  
  
RUN mkdir -p /home/digits  
#RUN mkdir -p /mnt/digits_jobs  
ENV DIGITS_ROOT=/home/digits  
#ENV DIGITS_JOBS_DIR=/mnt/digits_jobs  
RUN git clone https://github.com/NVIDIA/DIGITS.git ${DIGITS_ROOT}  
RUN pip install --allow-all-external -r ${DIGITS_ROOT}/requirements.txt  
RUN pip install -e ${DIGITS_ROOT}  
  
RUN apt-get update  
  
ENV PATH /usr/local/cuda/bin:$PATH  
ENV LD_LIBRARY_PATH /usr/lib/x86_64-linux-
gnu:/usr/local/cuda/lib64:$LD_LIBRARY_PATH  
ENV
DIGITS_MODEL_STORE_URL='http://developer.download.nvidia.com/compute/machine-
learning/modelstore/6.0'  
WORKDIR /home/digits  
ENTRYPOINT ["/bin/bash"]  

