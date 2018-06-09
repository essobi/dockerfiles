FROM ubuntu:xenial  
  
LABEL maintainer="Iacopo Colonnelli <iacopo.colonnelli@cern.ch>"  
  
ENV TRACKINGITSU_BUILD_DIR /tmp/tracking-itsu/build  
ENV TRACKINGITSU_SRC_DIR /usr/local/tracking-itsu  
ENV TRACKINGITSU_TARGET_DEVICE CPU  
  
RUN apt-get update -qq \  
&& apt-get install -qq software-properties-common \  
&& add-apt-repository -y ppa:ubuntu-toolchain-r/test \  
&& apt-get update -qq \  
&& apt-get install -qq g++-6 cmake wget \  
&& update-alternatives \  
\--install /usr/bin/gcc gcc /usr/bin/gcc-6 60 \  
\--slave /usr/bin/g++ g++ /usr/bin/g++-6 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir $TRACKINGITSU_SRC_DIR  
  
WORKDIR $TRACKINGITSU_SRC_DIR

