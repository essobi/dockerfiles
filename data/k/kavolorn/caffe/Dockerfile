FROM kavolorn/opencv:release-3.1.0  
  
MAINTAINER Alexey Kornilov <alexey.kornilov@kavolorn.ru>  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y gcc g++ libicu52  
  
RUN cd \  
&& wget -O boost_1_60_0.tar.gz
http://sourceforge.net/projects/boost/files/boost/1.60.0/boost_1_60_0.tar.gz/download
\  
&& tar -xvf boost_1_60_0.tar.gz \  
&& rm boost_1_60_0.tar.gz \  
&& cd boost_1_60_0 \  
&& ./bootstrap.sh \--with-libraries=python,thread,filesystem --with-
python=python3.4 \--with-icu=/usr/lib/x86_64-linux-gnu/ \  
&& ./b2 -j2 \  
&& ./b2 install  
  
RUN apt-get install -y libprotobuf-dev libleveldb-dev \  
libsnappy-dev libhdf5-serial-dev protobuf-compiler \  
libopenblas-dev libgflags-dev libgoogle-glog-dev liblmdb-dev  
  
RUN cd \  
&& git clone https://github.com/BVLC/caffe \  
&& cd caffe \  
&& git reset --hard 886563bb49080acf4479395025ccd39f733473e8 \  
&& mkdir build \  
&& cd build \  
&& sed -i -- 's/python-py/python/' ../cmake/Dependencies.cmake \  
&& sed -i -- 's/PYTHON-PY/PYTHON/' ../cmake/Dependencies.cmake \  
&& cmake -DCPU_ONLY=ON \  
-DCMAKE_INSTALL_PREFIX=/usr/local \  
-DBLAS=open \  
-DPython_ADDITIONAL_VERSIONS=3.4 \  
-Dpython_version=3.4 .. \  
&& make -j2 \  
&& apt-get install -y python3-pip python3-scipy python3-skimage \  
&& pip3 install google \  
&& pip3 install protobuf \  
&& 2to3-3.4 -w /usr/local/lib/python3.4/dist-packages/google/protobuf/ \  
&& make pytest \  
&& make install  

