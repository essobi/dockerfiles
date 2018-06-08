FROM lexandro/java8-base  
  
MAINTAINER Robert Stern <Robert.Stern@gmail.com>  
  
RUN apt-get update && apt-get upgrade -y && apt-get install -y libarchive-dev
pkg-config zip zlib1g-dev  
  
RUN git clone https://github.com/google/bazel.git /bazel && cd /bazel && git
tag -l && git checkout tags/0.0.2  
  
RUN /bazel/compile.sh  
  

