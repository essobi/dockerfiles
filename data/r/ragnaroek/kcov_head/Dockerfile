FROM debian:jessie  
  
ARG KCOV_GIT_REF  
  
RUN apt-get update  
# install pkg-config deliberately separate since it sometimes fails :( If it
eventually  
# is installed we do not repeat the whole image build.  
RUN apt-get install -y --fix-missing pkg-config  
RUN apt-get install -y zlib1g wget libcurl4-openssl-dev libelf-dev libdw-dev
cmake cmake-data g++ binutils-dev \  
libiberty-dev zlib1g-dev python-minimal git  
  
ENV SRC_DIR=/home/kcov-src \  
URL_GIT_KCOV=https://github.com/SimonKagstrom/kcov.git  
  
RUN git clone $URL_GIT_KCOV $SRC_DIR; \  
cd $SRC_DIR; \  
# default to latest tagged version  
DEFAULT_KCOV_GIT_REF=$(git tag --list | grep "^v[0-9]\\+$" | sort -V | tail
--lines 1); \  
KCOV_GIT_REF=${KCOV_GIT_REF:-$DEFAULT_KCOV_GIT_REF}; \  
git reset --hard $KCOV_GIT_REF;  
  
RUN cd $SRC_DIR && \  
mkdir build && \  
cd build && \  
cmake .. && \  
make && \  
make install  
  
ENTRYPOINT ["kcov"]  
CMD ["--help"]  

