# The MIT License (MIT)  
#  
# Copyright (c) 2015-2016 CNRS  
#  
# Permission is hereby granted, free of charge, to any person obtaining a copy  
# of this software and associated documentation files (the "Software"), to
deal  
# in the Software without restriction, including without limitation the rights  
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
# copies of the Software, and to permit persons to whom the Software is  
# furnished to do so, subject to the following conditions:  
#  
# The above copyright notice and this permission notice shall be included in
all  
# copies or substantial portions of the Software.  
#  
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM,  
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE  
# SOFTWARE.  
#  
# AUTHORS  
# Hervé Bredin (bredin@limsi.fr)  
FROM ubuntu:14.04  
MAINTAINER Hervé Bredin <bredin@limsi.fr>  
  
ADD etc/apt/sources.list /etc/apt/  
RUN apt-get update -qq  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# -- common utilities --  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends
\  
autoconf \  
automake \  
build-essential \  
cmake \  
cmake-curses-gui \  
curl \  
git \  
mercurial \  
pkg-config \  
python-software-properties \  
software-properties-common \  
sudo \  
wget \  
unzip  
  
# -- math --  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends
\  
gfortran \  
libblas-dev \  
liblapack-dev \  
libatlas-base-dev  
  
# -- python --  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends
\  
python \  
python-dev \  
python-pip \  
python-virtualenv  
  
# -- scientific python --  
RUN pip install numpy  
RUN pip install scipy  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends
\  
libfreetype6-dev \  
libpng12-dev \  
libjasper-dev \  
libjpeg8-dev \  
libtiff4-dev \  
libzmq3-dev  
  
RUN pip install \  
pandas \  
scikit-learn \  
scikit-image \  
numexpr \  
jupyter \  
matplotlib  
  
# Add Tini. Tini operates as a process subreaper for jupyter. This prevents  
# kernel crashes.  
ENV TINI_VERSION v0.6.0  
RUN curl -L https://github.com/krallin/tini/releases/download/v0.6.0/tini >
tini && \  
echo "d5ed732199c36a1189320e6c4859f0169e950692f451c03e7854243b95f4234b *tini"
| sha256sum -c - && \  
mv tini /usr/bin/tini && \  
chmod +x /usr/bin/tini  
ENTRYPOINT ["/usr/bin/tini", "--"]  
  
# run jupyter notebook by default  
EXPOSE 8888  
VOLUME /notebook  
WORKDIR /notebook  
CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0"]  

