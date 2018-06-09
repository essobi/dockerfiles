FROM ubuntu:16.04  
ENV TRAX_SOURCE /opt/trax  
  
# Install build & basic dependencies  
RUN apt-get -y update \  
&& apt-get install -y build-essential cmake git software-properties-common \  
&& apt-get install -y libopencv-dev libopencv-core2.4v5 libopencv-imgproc2.4v5
libopencv-highgui2.4v5 \  
&& mkdir -p ${TRAX_SOURCE} && git clone --depth=1 \--branch=master
https://github.com/votchallenge/trax.git ${TRAX_SOURCE} \  
&& cd ${TRAX_SOURCE} && mkdir build && cd build \  
&& cmake -DBUILD_CLIENT=ON -DBUILD_OPENCV=ON .. && make && make install && cd
.. && rm -rf build \  
&& apt-get remove -y git build-essential cmake git software-properties-common
libopencv-dev \  
&& apt-get -y autoremove \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/  

