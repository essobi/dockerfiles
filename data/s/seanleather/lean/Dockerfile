FROM alpine:latest  
MAINTAINER Sean Leather <https://github.com/spl>  
  
# Lean build flags  
ENV CMAKE_FLAGS="-D CMAKE_BUILD_TYPE=RELEASE -D BOOST=OFF -D TCMALLOC=OFF -G
Ninja"  
# Install the required packages  
RUN apk --no-cache add \  
bash \  
cmake \  
g++ \  
git \  
gmp-dev \  
lua-dev \  
mpfr-dev \  
ninja \  
python  
  
# Download from the repository, build, clean up  
RUN \  
git clone \--depth 1 https://github.com/leanprover/lean.git && \  
mkdir -p lean/build && \  
(cd lean/build; cmake $CMAKE_FLAGS ../src && ninja && ninja install) && \  
lean --version && \  
rm -rf lean  
  
# This is just a convenience for running the container. It can be overridden.  
ENTRYPOINT ["/bin/bash"]  

