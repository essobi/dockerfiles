FROM jupyter/notebook  
  
MAINTAINER Saagie  
  
RUN apt-get update \  
&& apt-get install --no-install-recommends software-properties-common python-
software-properties -y \  
&& apt-add-repository ppa:brightbox/ruby-ng \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
ruby2.3 ruby2.3-dev \  
libzmq3 libzmq3-dev \  
gnuplot-nox \  
libgsl0-dev \  
libtool autoconf automake \  
zlib1g-dev libleveldb-dev \  
libsqlite3-dev \  
libmagick++-dev imagemagick \  
libatlas-base-dev && \  
apt-get clean  
  
RUN gem install rbczmq iruby nyaplot distribution impala mikon statsample
mongo cabalist ml classifier-reborn  
  
RUN iruby register  
  
CMD jupyter notebook \  
\--ip=* \  
\--MappingKernelManager.time_to_dead=10 \  
\--MappingKernelManager.first_beat=3 \  
\--notebook-dir=/notebooks-dir/  

