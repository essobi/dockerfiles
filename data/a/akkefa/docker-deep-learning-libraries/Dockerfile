FROM ubuntu:16.04  
MAINTAINER Ikram Ali <mrikram1989@gmail.com>  
  
  
# Set terminal to be noninteractive  
ENV DEBIAN_FRONTEND noninteractive  
  
  
# Install packages  
RUN apt-get update && apt-get install -y --no-install-recommends \  
apt-utils \  
git \  
nano \  
curl \  
unzip \  
openssh-client \  
wget \  
build-essential \  
cmake \  
libopenblas-dev \  
python3.5 \  
python3.5-dev \  
python3-pip \  
libjpeg-dev \  
zlib1g-dev \  
libjpeg8-dev \  
libtiff5-dev \  
libjasper-dev \  
libpng12-dev \  
libavcodec-dev \  
libavformat-dev \  
libswscale-dev \  
libv4l-dev \  
libgtk2.0-dev \  
liblapacke-dev \  
checkinstall \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD . /code  
WORKDIR /code  
  
# Python 3.5  
# For convenience, alisas (but don't sym-link) python & pip to python3 & pip3
as recommended in:  
# http://askubuntu.com/questions/351318/changing-symlink-python-to-
python3-causes-problems  
RUN pip3 install --no-cache-dir --upgrade pip setuptools  
RUN echo "alias python='python3'" >> /code/.bash_aliases  
RUN echo "alias pip='pip3'" >> /code/.bash_aliases  
RUN pip3 install --no-cache-dir -r requirements.txt  
  
# OpenCV 3.2 get source from github  
RUN git clone -b 3.2.0 --depth 1 https://github.com/opencv/opencv.git
/usr/local/src/opencv  
RUN cd /usr/local/src/opencv && mkdir build && cd build && \  
cmake -D CMAKE_INSTALL_PREFIX=/usr/local \  
-D BUILD_TESTS=OFF \  
-D BUILD_PERF_TESTS=OFF \  
-D PYTHON_DEFAULT_EXECUTABLE=$(which python3) \  
.. && \  
make -j"$(nproc)" && \  
make install  
  
# Expose ports  
# 6006 = TensorBoard  
# 8888 = Jupyter Notebook  
EXPOSE 6006 8888  
CMD ["/bin/bash"]

