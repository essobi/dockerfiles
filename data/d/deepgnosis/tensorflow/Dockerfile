FROM nvidia/cuda:7.5-cudnn4-devel  
  
MAINTAINER Craig Citro <craigcitro@google.com>  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
curl \  
git \  
libfreetype6-dev \  
libpng12-dev \  
libzmq3-dev \  
pkg-config \  
python-dev \  
python-numpy \  
python-pip \  
software-properties-common \  
swig \  
zip \  
zlib1g-dev \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -qsSLkO \  
https://repo.continuum.io/miniconda/Miniconda-latest-Linux-`uname -p`.sh \  
&& bash Miniconda-latest-Linux-`uname -p`.sh -b \  
&& rm Miniconda-latest-Linux-`uname -p`.sh  
  
ENV PATH=/root/miniconda2/bin:$PATH  
  
RUN conda create --name keras python=3.5  
  
RUN source activate keras \  
&& conda install -y \  
mkl \  
h5py \  
pandas \  
scikit-learn \  
networkx \  
pyyaml \  
pymongo \  
smart_open \  
matplotlib \  
quandl \  
ipykernel \  
jupyter \  
&& python -m ipykernel.kernelspec  
  
# Set up our notebook config.  
COPY jupyter_notebook_config.py /root/.jupyter/  
  
# Jupyter has issues with being run directly:  
# https://github.com/ipython/ipython/issues/7062  
# We just add a little wrapper script.  
COPY run_jupyter.sh /  
  
# Set up Bazel.  
# We need to add a custom PPA to pick up JDK8, since trusty doesn't  
# have an openjdk8 backport. openjdk-r is maintained by a reliable
contributor:  
# Matthias Klose (https://launchpad.net/~doko). It will do until  
# we either update the base image beyond 14.04 or openjdk-8 is  
# finally backported to trusty; see e.g.  
# https://bugs.launchpad.net/trusty-backports/+bug/1368094  
RUN add-apt-repository -y ppa:openjdk-r/ppa && \  
apt-get update && \  
apt-get install -y openjdk-8-jdk openjdk-8-jre-headless && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Running bazel inside a `docker build` command causes trouble, cf:  
# https://github.com/bazelbuild/bazel/issues/134  
# The easiest solution is to set up a bazelrc file forcing --batch.  
RUN echo "startup --batch" >>/root/.bazelrc  
# Similarly, we need to workaround sandboxing issues:  
# https://github.com/bazelbuild/bazel/issues/418  
RUN echo "build --spawn_strategy=standalone --genrule_strategy=standalone" \  
>>/root/.bazelrc  
ENV BAZELRC /root/.bazelrc  
# Install the most recent bazel release.  
ENV BAZEL_VERSION 0.3.0  
WORKDIR /  
RUN mkdir /bazel && \  
cd /bazel && \  
curl -fSsL -O
https://github.com/bazelbuild/bazel/releases/download/$BAZEL_VERSION/bazel-$BAZEL_VERSION-
installer-linux-x86_64.sh && \  
curl -fSsL -o /bazel/LICENSE.txt
https://raw.githubusercontent.com/bazelbuild/bazel/master/LICENSE.txt && \  
chmod +x bazel-*.sh && \  
./bazel-$BAZEL_VERSION-installer-linux-x86_64.sh && \  
cd / && \  
rm -f /bazel/bazel-$BAZEL_VERSION-installer-linux-x86_64.sh  
  
# Download and build TensorFlow.  
RUN git clone \--recurse-submodules
https://github.com/tensorflow/tensorflow.git && \  
cd tensorflow && \  
git checkout r0.8 && \  
git submodule update --init  
WORKDIR /tensorflow  
  
# Configure the build for our CUDA configuration.  
ENV CUDA_TOOLKIT_PATH /usr/local/cuda  
ENV CUDNN_INSTALL_PATH /usr/local/cuda  
ENV TF_NEED_CUDA 1  
RUN source activate keras && \  
./configure && \  
bazel build -c opt --config=cuda
tensorflow/tools/pip_package:build_pip_package && \  
bazel-bin/tensorflow/tools/pip_package/build_pip_package /tmp/pip && \  
pip install --upgrade /tmp/pip/tensorflow-*.whl  
  
RUN source activate keras \  
&& pip install git+git://github.com/pykalman/pykalman.git \  
&& pip install git+git://github.com/fchollet/keras.git --no-deps \  
&& pip install --no-deps git+https://github.com/lukovkin/hyperopt.git \  
&& pip install git+https://github.com/lukovkin/holidays.py.git \  
&& pip install bdateutil  
  
VOLUME /notebook  
WORKDIR /notebook  
  
# Set up CUDA variables  
ENV CUDA_PATH /usr/local/cuda  
  
ENV OMP_NUM_THREADS=8  
ENV PYTHONPATH=/notebook/nnt-backend-py/:/notebook/UFCNN/ufcnn:  
  
# TensorBoard  
EXPOSE 6006  
# IPython  
EXPOSE 8888  
RUN ["/bin/bash"]  

