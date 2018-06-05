FROM ubuntu:16.10  
RUN apt-get update && apt-get install -y \  
cmake \  
curl \  
gcc \  
git \  
make \  
libgsl-dev \  
zlib1g-dev  
  
RUN mkdir -p /clapack/build /clapack/libs && \  
curl http://www.netlib.org/clapack/clapack-3.2.1-CMAKE.tgz | tar -zxf - -C
/clapack --strip-components 1 && \  
cd /clapack/build && \  
cmake -Wno-dev .. && \  
make -j 4 && \  
find . -name '*.a' | xargs cp -t /clapack/libs  
  
RUN git clone \--depth 1 https://github.com/dg13/rasqual.git && \  
cd /rasqual/src && \  
export CFLAGS=-I/clapack/INCLUDE && \  
export LDFLAGS=-L/clapack/libs && \  
make -j 4  

