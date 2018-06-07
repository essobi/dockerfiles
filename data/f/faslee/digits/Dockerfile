FROM nvidia/caffe:0.15  
  
LABEL maintainer "NVIDIA CORPORATION <cudatools@nvidia.com>"  
  
ENV DIGITS_VERSION 6.0  
  
LABEL com.nvidia.digits.version="6.0"  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
caffe-nv \  
curl \  
g++ \  
git \  
graphviz \  
gunicorn \  
libfreetype6-dev \  
libpng12-dev \  
libprotobuf-dev \  
libzmq3-dev \  
nginx \  
pkg-config \  
python \  
python-caffe-nv \  
python-dev \  
python-flask \  
python-flaskext.socketio \  
python-flaskext.wtf \  
python-gevent \  
python-lmdb \  
python-matplotlib \  
python-pil \  
python-pydot \  
python-requests \  
python-six \  
python-skimage \  
python-tk \  
python-wtforms \  
rsync \  
software-properties-common \  
torch7-nv=0.9.99-1+cuda8.0 \  
unzip && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
rm get-pip.py  
  
RUN pip install https://github.com/NVIDIA/DIGITS/tarball/v6.0.0-rc.1  
  
RUN pip install --no-cache-dir \  
setuptools\>=18.5 \  
tensorflow-gpu==1.2.0  
  
VOLUME /jobs  
  
ENV DIGITS_JOBS_DIR=/jobs  
ENV DIGITS_LOGFILE_FILENAME=/jobs/digits.log  
  
# DIGITS  
EXPOSE 5005  
# TensorBoard  
#EXPOSE 6006  
  
CMD digits-devserver --port 5005  

