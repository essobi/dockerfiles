FROM ubuntu:yakkety

ENV DEBIAN_FRONTEND noninteractive
ENV PATH /anaconda/bin:$PATH
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8

ENV PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=cpp
ENV PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION_VERSION=2
ENV PROTOBUF_VERSION=3.0.0
# System packages

RUN apt-get -y update \
    && apt-get -y upgrade \
    && apt-get install -y build-essential protobuf-compiler libprotobuf-dev wget curl locales unzip bzip2 openssl ca-certificates libpq-dev pylint3 \
    && apt-get clean && dpkg-reconfigure locales && locale-gen en_US.UTF-8 \
    && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
# Python dependencies

RUN wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh \
    && bash miniconda.sh -b -p /anaconda \
    && conda install scipy numpy scikit-learn pandas ipython-notebook pip psycopg2 cython \
    && conda clean -tipsy \
    && rm miniconda.sh

# Protobuf w/C++ implementation

RUN cd /tmp \
    && wget https://github.com/google/protobuf/releases/download/v${PROTOBUF_VERSION}/protobuf-python-${PROTOBUF_VERSION}.tar.gz \
    && tar -xvzf protobuf-python-${PROTOBUF_VERSION}.tar.gz \
    && cd protobuf-${PROTOBUF_VERSION}/python \
    && python3 setup.py build --cpp_implementation \
    && python3 setup.py install --cpp_implementation \
    && python3 setup.py clean --all \
    && python3 -c 'import google.protobuf.internal.api_implementation as a; assert a.Type() == "cpp"' \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
