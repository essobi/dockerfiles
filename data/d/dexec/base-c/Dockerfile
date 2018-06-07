FROM debian:8.0  
MAINTAINER andystanton  
ENV LANG C.UTF-8  
ENV CLANG_VERSION 3.5  
RUN apt-get update && \  
apt-get install -y patch clang-${CLANG_VERSION} && \  
update-alternatives --install /usr/bin/cc cc /usr/bin/clang-${CLANG_VERSION}
100 && \  
update-alternatives --install /usr/bin/c++ c++
/usr/bin/clang++-${CLANG_VERSION} 100 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

