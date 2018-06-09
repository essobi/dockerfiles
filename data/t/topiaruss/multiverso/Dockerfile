FROM nvidia/cuda:7.5-cudnn5-devel  
  
MAINTAINER lyysdy@foxmail.com  
  
USER root  
  
# install dev tools  
RUN apt-get update \  
&& apt-get install -qqy \  
autoconf \  
automake \  
build-essential \  
cmake \  
curl \  
g++-4.8 \  
gcc \  
gdb \  
gfortran \  
git \  
libbz2-dev \  
libopenblas-dev \  
libopenmpi-dev \  
libssl-dev \  
libtool \  
libzmq3-dev \  
openmpi-bin \  
openssh-client \  
openssh-server \  
pkg-config \  
python-dev \  
python-nose \  
python-numpy \  
python-pip \  
python-zmq \  
rsync \  
software-properties-common \  
tar \  
vim \  
\  
bzip2 \  
ca-certificates \  
libfreeimage-dev \  
libfreeimage3 \  
libglib2.0-0 \  
libsm6 \  
libxext6 \  
libxrender1 \  
wget  
  
# inherited from our old install  
RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh  
RUN wget --quiet \  
https://repo.continuum.io/miniconda/Miniconda3-4.1.11-Linux-x86_64.sh \  
-O ~/miniconda.sh && \  
/bin/bash ~/miniconda.sh -b -p /opt/conda && \  
rm ~/miniconda.sh  
ENV PATH /opt/conda/bin:$PATH  
  
COPY environment.yml /home/  
  
RUN echo 'create conda env, clean' && \  
cd /home && conda env create --name dreamkg_docker --force && \  
# was conda clean removing test components?  
conda clean -ay  
  
# //inherited  
# java  
#RUN mkdir -p /usr/local/java/default && \  
# curl -Ls 'http://download.oracle.com/otn-
pub/java/jdk/8u65-b17/jdk-8u65-linux-x64.tar.gz' -H 'Cookie:
oraclelicense=accept-securebackup-cookie' | \  
# tar --strip-components=1 -xz -C /usr/local/java/default/  
#  
#ENV JAVA_HOME /usr/local/java/default/  
#ENV PATH $PATH:$JAVA_HOME/bin  
# hadoop  
#RUN wget -cq -t 0
http://www.eu.apache.org/dist/hadoop/common/hadoop-2.6.0/hadoop-2.6.0.tar.gz  
#RUN tar -xz -C /usr/local/ -f hadoop-2.6.0.tar.gz \  
# && rm hadoop-2.6.0.tar.gz \  
# && cd /usr/local && ln -s ./hadoop-2.6.0 hadoop \  
# && cp -r /usr/local/hadoop/include/* /usr/local/include  
#  
#ENV HADOOP_PREFIX /usr/local/hadoop  
#RUN sed -i '/^export JAVA_HOME/ s:.*:export
JAVA_HOME=/usr/local/java/default\nexport
HADOOP_PREFIX=/usr/local/hadoop\nexport HADOOP_HOME=/usr/local/hadoop\n:'
$HADOOP_PREFIX/etc/hadoop/hadoop-env.sh  
#RUN sed -i '/^export HADOOP_CONF_DIR/ s:.*:export
HADOOP_CONF_DIR=/usr/local/hadoop/etc/hadoop/:'
$HADOOP_PREFIX/etc/hadoop/hadoop-env.sh  
#  
## fixing the libhadoop.so like a boss  
#RUN rm /usr/local/hadoop/lib/native/* \  
# && curl -Ls http://dl.bintray.com/sequenceiq/sequenceiq-bin/hadoop-
native-64-2.6.0.tar | tar -x -C /usr/local/hadoop/lib/native/  
# install Theano-dev  
#RUN mkdir -p /theano \  
# && cd /theano \  
# && git clone git://github.com/Theano/Theano.git \  
# && cd /theano/Theano \  
# && python setup.py develop  
## Install Jupyter Notebook for iTorch  
#RUN pip install notebook ipywidgets  
# Run Torch7 installation scripts  
#RUN git clone https://github.com/torch/distro.git /root/torch --recursive &&
cd /root/torch && \  
# bash install-deps && \  
# ./install.sh  
# Export environment variables manually  
ENV
LUA_PATH='/root/.luarocks/share/lua/5.1/?.lua;/root/.luarocks/share/lua/5.1/?/init.lua;/root/torch/install/share/lua/5.1/?.lua;/root/torch/install/share/lua/5.1/?/init.lua;./?.lua;/root/torch/install/share/luajit-2.1.0-beta1/?.lua;/usr/local/share/lua/5.1/?.lua;/usr/local/share/lua/5.1/?/init.lua'  
ENV
LUA_CPATH='/root/.luarocks/lib/lua/5.1/?.so;/root/torch/install/lib/lua/5.1/?.so;./?.so;/usr/local/lib/lua/5.1/?.so;/usr/local/lib/lua/5.1/loadall.so'  
ENV PATH=/root/torch/install/bin:$PATH  
ENV LD_LIBRARY_PATH=/root/torch/install/lib:$LD_LIBRARY_PATH  
ENV DYLD_LIBRARY_PATH=/root/torch/install/lib:$DYLD_LIBRARY_PATH  
ENV LUA_CPATH='/root/torch/install/lib/?.so;'$LUA_CPATH  
  
WORKDIR /dmtk  
  
COPY Applications /dmtk/Applications/  
COPY Test /dmtk/Test/  
COPY binding /dmtk/binding/  
COPY include /dmtk/include/  
COPY src /dmtk/src/  
COPY cmake_uninstall.cmake.in /dmtk/cmake_uninstall.cmake.in  
COPY CMakeLists.txt /dmtk/  
  
ARG boost_version=1.62.0  
ARG boost_dir=boost_1_62_0  
ENV boost_version ${boost_version}  
  
RUN wget --quiet \  
http://downloads.sourceforge.net/project/boost/boost/${boost_version}/${boost_dir}.tar.gz
\  
&& tar xfz ${boost_dir}.tar.gz \  
&& rm ${boost_dir}.tar.gz \  
&& cd ${boost_dir} \  
&& ./bootstrap.sh \  
&& ./b2 --without-python --prefix=/usr -j 4 link=shared runtime-link=shared
install \  
&& cd .. && rm -rf ${boost_dir} && ldconfig  
  
#RUN cd /dmtk && git clone https://github.com/Microsoft/multiverso.git && cd
multiverso \  
# && mkdir build && cd build \  
# && cmake .. && make && make install  
# The above git clone replaced by using the instance we are already part of...  
RUN cd /dmtk \  
&& mkdir build && cd build \  
&& cmake .. && make && make install  
  
# python tests  
# replace sh with bash to prevent source command throwing error under /bin/sh  
RUN ln -snf /bin/bash /bin/sh  
  
RUN cd /home \  
&& mkdir -p theano \  
&& source activate dreamkg_docker \  
&& cd /home/theano \  
&& git clone git://github.com/Theano/Theano.git \  
&& cd Theano \  
&& python setup.py develop  
  
RUN cd /dmtk/binding/python \  
&& source activate dreamkg_docker \  
&& python setup.py install \  
&& /opt/conda/envs/dreamkg_docker/bin/nosetests  
  
## lua tests  
#RUN cd /dmtk/binding/lua \  
# && make install \  
# && make test  
# run cpp tests  
RUN cd /dmtk/build \  
&& mpirun -np 4 ./Test/multiverso.test kv \  
&& mpirun -np 4 ./Test/multiverso.test array \  
&& mpirun -np 4 ./Test/multiverso.test net \  
&& mpirun -np 4 ./Test/multiverso.test ip \  
&& mpirun -np 4 ./Test/multiverso.test checkpoint \  
&& mpirun -np 4 ./Test/multiverso.test restore \  
&& mpirun -np 4 ./Test/multiverso.test allreduce  
# - mpirun -np 4 ./Test/multiverso.test matrix # TODO the matrix test won't
stop  
# - mpirun -np 4 ./Test/multiverso.test TestSparsePerf # TODO TestSparsePerf
takes too much time  
# - mpirun -np 4 ./Test/multiverso.test TestDensePerf # TODO TestDensePerf
takes too much time  
# clean unnessary packages  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Insert useful scripts, and timestamp the build  
COPY scripts /scripts  
  
RUN echo "gpu base created " > /created_gpubase.txt && \  
date >> /created_gpubase.txt  
  
ENTRYPOINT ["/bin/bash", "-c"]  
CMD ["/scripts/ident.sh"]  
  

