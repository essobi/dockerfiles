# Jupyterの各種カーネルのインストール  
FROM akihikoitoh/jupyter-notebook:latest  
MAINTAINER ITOH Akihiko  
  
###### Shell Modules ######  
RUN apt-get update \  
&& apt-get install -y build-essential \  
&& apt-get install -y wget \  
&& apt-get install -y g++ \  
&& apt-get install -y ruby  
# RUN apt-get install -y ca-certificates  
###### Install Kernels ######  
  
RUN apt-get install -y software-properties-common python-software-properties  
  
# Python Packages  
# Numpy, Scipy, Matplotlib, Pandas, Sympy, Scikit-learn  
RUN apt-get install -y python-setuptools \  
python-numpy \  
python-scipy \  
python-matplotlib \  
python-matplotlib-data \  
python-pandas \  
python-sympy \  
python-nose \  
python-sklearn \  
libhdf5-dev \  
libatlas-dev \  
libatlas3gf-base \  
libopenblas-dev \  
python-all-dev \  
libblas-dev \  
libblas3 \  
liblapack-dev \  
liblapack3 \  
liblapacke \  
liblapacke-dev \  
python-dev \  
libjpeg-dev \  
libfreetype6 \  
libfreetype6-dev \  
zlib1g-dev \  
gfortran \  
libffi-dev \  
libssl-dev \  
python-pyparsing \  
python-pydot \  
&& apt-get build-dep -y python-imaging \  
&& apt-get install -y python-imaging  
  
RUN pip install --upgrade pip \  
&& pip install pyopenssl ndg-httpsclient pyasn1 \  
&& pip install Pillow  
  
# && pip install git+git://github.com/python-pillow/Pillow.git \  
# && pip uninstall -y pyparsing \  
# && pip install pyparsing==1.5.7 \  
# && pip install
https://pypi.python.org/packages/source/p/pyparsing/pyparsing-1.5.7.tar.gz \  
# && pip install pydot  
# && pip install -U pyparsing==1.5.7 pydot  
# && easy_install
http://cheeseshop.python.org/packages/source/p/pyparsing/pyparsing-1.5.7.tar.gz
\  
  
RUN pip install cython \  
&& pip install pyyaml \  
&& pip install h5py \  
&& pip install Theano \  
&& pip install chainer \  
&& pip install keras \  
&& pip install pymatbridge  
  
# set Data path  
RUN bash -c 'echo "export PYLEARN2_DATA_PATH=/opt/data" >> /.bashrc'  
# set Scripts path  
RUN bash -c 'echo "export PATH=/opt/pylearn2/pylearn2/scripts:$PATH" >>
/.bashrc'  
# INCLUDE Dockerfile.R  
# INCLUDE Dockerfile.julia  
# INCLUDE Dockerfile.c++  
# INCLUDE Dockerfile.spark  
# INCLUDE Dockerfile.ruby  
  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* && rm -rf /tmp && mkdir /tmp  
  
WORKDIR /notebooks  
CMD ["/notebook.sh"]  

