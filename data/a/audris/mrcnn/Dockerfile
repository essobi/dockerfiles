# docker-keras - Keras in Docker for reproducible deep learning  
FROM ubuntu:16.04  
MAINTAINER audrism <audris@mockus.org>  
  
  
# install debian packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update -qq \  
&& apt-get install --no-install-recommends -y \  
dbus \  
openssh-server \  
lsof sudo \  
libssl-dev \  
sssd \  
sssd-tools \  
libnss-sss \  
libpam-pwquality \  
libpam-sss \  
libsss-sudo \  
ldap-utils \  
vim \  
git \  
wget \  
curl lsb-release \  
tmux zsh zip \  
# install essentials  
build-essential \  
cmake \  
g++ \  
git \  
# install python 3  
python3.5 \  
python3.5-dev \  
python3-pip \  
python3-setuptools \  
python3-virtualenv \  
python3-wheel \  
pkg-config \  
ipython3-notebook \  
# requirements for numpy  
libopenblas-base \  
python3-numpy \  
python3-scipy \  
# requirements for keras  
python3-yaml \  
python3-pydot \  
python3-tk \  
libopenblas-dev \  
liblapack-dev \  
libssl-dev \  
libtiff5-dev \  
libwebp-dev \  
libzmq3-dev \  
zlib1g-dev \  
qt5-default \  
libvtk6-dev \  
zlib1g-dev \  
libjpeg-dev \  
libwebp-dev \  
libpng-dev \  
libtiff5-dev \  
libopenexr-dev \  
libgdal-dev \  
libdc1394-22-dev \  
libavcodec-dev \  
libavformat-dev \  
libswscale-dev \  
libtheora-dev \  
libvorbis-dev \  
libxvidcore-dev \  
libx264-dev \  
r-recommended \  
r-base-dev \  
r-cran-car \  
r-cran-rcolorbrewer \  
r-cran-fastcluster \  
python3-nose \  
python3-h5py \  
python3-skimage \  
python3-matplotlib \  
python3-pandas \  
python3-sklearn \  
python3-sympy \  
libpython3-dev python3-dev openjdk-8-jdk \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN echo "alias python='python3'" >> /root/.bash_aliases && echo "alias
pip='pip3'" >> /root/.bash_aliases  
  
RUN curl https://bazel.build/bazel-release.pub.gpg | apt-key add -  
ARG CAFFE_VERSION=master  
RUN echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable
jdk1.8" | tee /etc/apt/sources.list.d/bazel.list  
RUN apt-get update -qq \  
&& apt-get install --no-install-recommends -y \  
bazel && apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN pip3 install PhotoHash Pillow requests Cython jupyter && mkdir
/root/.jupyter && echo "c.NotebookApp.ip = '*'" \  
"\nc.NotebookApp.open_browser = False" \  
"\nc.NotebookApp.token = ''" \  
> /root/.jupyter/jupyter_notebook_config.py  
EXPOSE 8888  
#ARG
TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.4.0-cp35-cp35m-linux_x86_64.whl  
ARG
TF_BINARY_URL=http://web.eecs.utk.edu/~audris/tensorflow-1.4.1-cp35-cp35m-linux_x86_64.whl  
RUN pip3 install --upgrade $TF_BINARY_URL  
#RUN pip3 install --upgrade tensorflow  
EXPOSE 6006  
#ARG KERAS_VERSION=2.0.4  
ENV KERAS_BACKEND=tensorflow  
#RUN pip3 --no-cache-dir install --no-dependencies
git+https://github.com/fchollet/keras.git@${KERAS_VERSION}  
#RUN pip3 --no-cache-dir install --no-dependencies keras && pip3 install keras
--upgrade  
# dump package lists  
RUN dpkg-query -l > /dpkg-query-l.txt \  
&& pip3 freeze > /pip3-freeze.txt  
RUN pip3 install --upgrade pip  
  
# Install OpenCV  
RUN git clone \--depth 1 https://github.com/opencv/opencv.git /root/opencv &&
\  
cd /root/opencv && \  
mkdir build && \  
cd build && \  
cmake -DWITH_QT=ON -DWITH_OPENGL=ON -DFORCE_VTK=ON -DWITH_TBB=ON
-DWITH_GDAL=ON -DWITH_XINE=ON -DBUILD_EXAMPLES=ON .. && \  
make -j"$(nproc)" && \  
make install && \  
ldconfig && \  
echo 'ln /dev/null /dev/raw1394' >> ~/.bashrc  
  
# Install dependencies for Caffe  
RUN apt-get update && apt-get install -y \  
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
&& \  
apt-get clean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
# Install Caffe  
RUN git clone -b master --depth 1 https://github.com/BVLC/caffe.git
/usr/local/src/caffe && \  
pip3 --no-cache-dir install -r /usr/local/src/caffe/python/requirements.txt &&
\  
cd /usr/local/src/caffe && mkdir build && cd build && \  
cmake -DCPU_ONLY=ON -D python_version=3 -DBLAS=open -D USE_OPENCV=ON .. && \  
make -j"$(nproc)" all && make install  
  
#RUN git clone -b ${CAFFE_VERSION} --depth 1 https://github.com/BVLC/caffe.git
/root/caffe && \  
# cd /root/caffe && \  
# cat python/requirements.txt | xargs -n1 pip3 install && \  
# mkdir build && cd build && \  
# cmake -DCPU_ONLY=ON -DBLAS=open -D USE_OPENCV=ON .. && \  
# make -j"$(nproc)" all && \  
# make install  
# Set up Caffe environment variables  
ENV CAFFE_ROOT=/usr/local/src/caffe  
ENV PYCAFFE_ROOT=$CAFFE_ROOT/python  
ENV PYTHONPATH=$PYCAFFE_ROOT:$PYTHONPATH \  
PATH=$CAFFE_ROOT/build/tools:$PYCAFFE_ROOT:$PATH  
  
RUN echo "$CAFFE_ROOT/build/lib" >> /etc/ld.so.conf.d/caffe.conf && ldconfig  
#RUN pip3 install --no-cache-dir python-dateutil --upgrade  
RUN pip3 install --no-cache-dir --upgrade python-dateutil h5py pydot_ng keras  
  
# Set up notebook config  
# COPY jupyter_notebook_config.py /root/.jupyter/  
# Jupyter has issues with being run directly:
https://github.com/ipython/ipython/issues/7062  
# COPY run_jupyter.sh /root/  
RUN pip3 install --no-cache-dir
git+https://github.com/waleedka/coco.git#subdirectory=PythonAPI && \  
pip3 install
http://download.pytorch.org/whl/cu75/torch-0.2.0.post3-cp35-cp35m-manylinux1_x86_64.whl
&&\  
pip3 install torchvision  
  
COPY eecsCA_v3.crt /etc/ssl/  
COPY sssd.conf /etc/sssd/  
COPY common* /etc/pam.d/  
RUN chmod 0600 /etc/sssd/sssd.conf /etc/pam.d/common*  
RUN if [ ! -d /var/run/sshd ]; then mkdir /var/run/sshd; chmod 0755
/var/run/sshd; fi  
COPY cropTag init.sh startsvc.sh startshell.sh notebook.sh startDef.sh /bin/  
  
ENV NB_USER jovyan  
ENV NB_UID 1000  
ENV HOME /home/$NB_USER  
RUN useradd -m -s /bin/bash -N -u $NB_UID $NB_USER && mkdir $HOME/.ssh &&
chown -R $NB_USER:users $HOME  
RUN chown -R $NB_USER:users $HOME && chmod -R og-rwx $HOME/.ssh  

