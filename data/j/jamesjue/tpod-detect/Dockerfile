FROM nvidia/cuda  
MAINTAINER Junjue Wang  
  
# install py-faster-rcnn dependency  
RUN apt-get update && apt-get install -y \  
build-essential \  
git \  
python-opencv \  
python-pip \  
python-dev \  
python-scipy \  
python-matplotlib \  
libprotobuf-dev \  
libleveldb-dev \  
libsnappy-dev \  
libopencv-dev \  
libhdf5-serial-dev \  
protobuf-compiler \  
libgflags-dev \  
libgoogle-glog-dev \  
liblmdb-dev \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN apt-get update && apt-get install -y --no-install-recommends libboost-all-
dev \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN pip install cython easydict  
  
# install openblas  
WORKDIR /tmp  
ADD install-openblas.sh install-openblas.sh  
RUN bash install-openblas.sh  
  
# install py-faster-rcnn  
WORKDIR /  
RUN git clone \--recursive https://github.com/Jamesjue/py-faster-rcnn.git  
  
WORKDIR /py-faster-rcnn  
  
RUN cd lib && \  
make -j$(nproc)  
  
RUN cd caffe-fast-rcnn && \  
cp Makefile.config.example Makefile.config && \  
sed -i 's/BLAS := atlas/BLAS := open/' Makefile.config && \  
sed -i 's%# BLAS_INCLUDE := /path/to/your/blas%BLAS_INCLUDE :=
/opt/OpenBLAS/include%' Makefile.config && \  
sed -i 's%# BLAS_LIB := /path/to/your/blas%BLAS_LIB := /opt/OpenBLAS/lib%'
Makefile.config && \  
sed -i 's%# WITH_PYTHON_LAYER := 1%WITH_PYTHON_LAYER := 1%' Makefile.config &&
\  
pip install --upgrade pip && \  
pip install -r python/requirements.txt && \  
make -j$(nproc) && \  
make -j$(nproc) pycaffe  
  
#RUN ./data/scripts/fetch_faster_rcnn_models.sh  
# install twisted web framework  
RUN apt-get update && apt-get install -y python-twisted && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# install requirement for python detect-server  
WORKDIR /py-faster-rcnn/tools/detect-server  
RUN git fetch && git pull && pip install -r requirements.txt  
  
# add model if there is one  
ADD model.caffemodel /py-faster-
rcnn/models/web_demo/VGG_CNN_M_1024/faster_rcnn_alt_opt/model.caffemodel  
  
# run twistd wsgi to server python application  
WORKDIR /py-faster-rcnn  
EXPOSE 8080  
CMD ["/bin/bash", "-c", "source /etc/profile.d/openblas.sh && cd tools/detect-
server/ && twistd -n web --port 8080 --wsgi detect-web-server.app"]  

