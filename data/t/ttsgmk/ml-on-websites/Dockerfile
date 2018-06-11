FROM ubuntu:14.04  
MAINTAINER Martin Keydel  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# System dependencies  
RUN apt-get update  
RUN apt-get install -y \  
build-essential curl wget git cmake pkg-config unzip imagemagick libgtk2.0-dev
> /dev/null  
# libgtk2.0-dev -> OpenCV  
# Install Firefox  
RUN \  
curl 'https://download-
installer.cdn.mozilla.net/pub/firefox/releases/35.0/linux-x86_64/en-
US/firefox-35.0.tar.bz2' \  
-o firefox.tar.bz2 &&\  
bunzip2 firefox.tar.bz2 &&\  
tar xf firefox.tar &&\  
rm firefox.tar  
  
RUN apt-get update && apt-get install -y \  
# Headless browser support  
xvfb \  
# Needed to launch firefox  
libasound2 \  
libgtk2.0-0 \  
libdbus-glib-1-2 \  
libxcomposite1  
  
  
# Miniconda3  
ENV PATH /opt/conda/bin:$PATH  
ENV LD_LIBRARY_PATH /opt/conda/lib:$LD_LIBRARY_PATH  
RUN curl -Ls https://repo.continuum.io/miniconda/Miniconda3-latest-
Linux-x86_64.sh -o /tmp/install-miniconda.sh && \  
/bin/bash /tmp/install-miniconda.sh -b -p /opt/conda && \  
conda update --all -y  
  
# Basic dependencies  
RUN conda install -y bzip2 glib readline mkl openblas numpy scipy hdf5 \  
pillow matplotlib cython pandas gensim protobuf \  
lmdb leveldb boost glog gflags libgcc  
RUN pip install pydot_ng nnpack h5py scikit-learn scikit-image imutils && \  
python -c 'import h5py;h5py.run_tests()'  
RUN pip install pyyaml==3.11 requests==2.5.1 selenium==2.52.0  
  
# OpenCV  
RUN conda install -y -c menpo opencv3 && \  
python -c "import cv2;print(cv2.__version__)"  
  
RUN ldconfig  
  
# Jupyter  
RUN pip install -q jupyter jupyterlab && \  
jupyter --version  
  
# TensorFlow  
RUN git clone \--depth 1 https://github.com/tensorflow/tensorflow.git
/usr/src/tensorflow && \  
pip install -q tensorflow  
# cannot use GPUs within build process, you can also do GPU test manually:  
# python -c 'import tensorflow as tf;sess =
tf.Session(config=tf.ConfigProto(log_device_placement=True))'  
# Keras  
RUN git clone \--depth 1 https://github.com/fchollet/keras.git /usr/src/keras
&& \  
pip install keras  
  
# Chainer  
RUN git clone \--depth 1 https://github.com/pfnet/chainer.git /usr/src/chainer
&& \  
pip install chainer  
  
COPY runner.sh /usr/src/app/runner.sh  
  
WORKDIR /usr/src/app  
VOLUME /usr/src/app  
  
ENTRYPOINT ["/usr/src/app/runner.sh"]  

