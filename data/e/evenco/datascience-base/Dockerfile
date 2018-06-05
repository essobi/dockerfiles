FROM ubuntu:artful  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV LANGUAGE en_US.UTF-8  
ENV LANG en_US.UTF-8  
  
ENV PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=cpp  
ENV PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION_VERSION=2  
ENV PROTOBUF_VERSION=3.5.1  
  
# System packages  
  
RUN apt-get -y update \  
&& apt-get -y upgrade \  
&& apt-get install -y \  
wget \  
curl \  
git \  
unzip \  
bzip2 \  
locales \  
openssl \  
ca-certificates \  
python3.6 \  
python3.6-dev \  
openvpn \  
graphviz \  
&& apt-get -y clean \  
&& apt-get -y autoremove \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& locale-gen en_US.UTF-8 \  
&& dpkg-reconfigure locales \  
&& rm -f /usr/bin/python3 && ln -s /usr/bin/python3.6 /usr/bin/python3 \  
&& rm -f /usr/bin/python && ln -s /usr/bin/python3.6 /usr/bin/python \  
&& wget https://bootstrap.pypa.io/get-pip.py \  
&& python get-pip.py \  
&& rm get-pip.py  
  
# Python dependencies  
  
COPY requirements*.txt /  
  
RUN apt-get update \  
&& apt-get -y install build-essential libpq-dev \  
&& pip install --no-cache-dir -r requirements.txt -r requirements-dev.txt -r
requirements-git.txt \  
&& check-requirements \  
&& apt-get remove -y build-essential libpq-dev \  
&& apt-get -y clean \  
&& apt-get -y autoremove \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Protobuf w/C++ implementation  
  
RUN cd /tmp \  
&& apt-get -y update \  
&& apt-get -y install build-essential \  
&& wget
https://github.com/google/protobuf/releases/download/v${PROTOBUF_VERSION}/protobuf-
cpp-${PROTOBUF_VERSION}.tar.gz \  
&& tar -xzf protobuf-cpp-${PROTOBUF_VERSION}.tar.gz \  
&& cd protobuf-${PROTOBUF_VERSION} \  
&& ./configure \  
&& make install \  
&& ldconfig \  
&& cd .. \  
&& rm -rf /tmp/* \  
&& wget
https://github.com/google/protobuf/releases/download/v${PROTOBUF_VERSION}/protobuf-
python-${PROTOBUF_VERSION}.tar.gz \  
&& tar -xzf protobuf-python-${PROTOBUF_VERSION}.tar.gz \  
&& cd protobuf-${PROTOBUF_VERSION}/python \  
&& python setup.py build --cpp_implementation \  
&& python setup.py install --cpp_implementation \  
&& python setup.py clean --all \  
&& python -c 'import google.protobuf.internal.api_implementation as a; assert
a.Type() == "cpp"' \  
&& python -c 'from google.protobuf import wrappers_pb2' \  
&& apt-get remove -y build-essential \  
&& apt-get -y clean \  
&& apt-get -y autoremove \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

