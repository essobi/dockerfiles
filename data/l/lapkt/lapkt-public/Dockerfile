FROM ubuntu:xenial  
MAINTAINER Nir Lipovetzky nir.lipovetzky@unimelb.edu.au  
  
# Script based on Guillem Frances aigupf/starter-kit image  
# Install required packages  
RUN apt-get update && apt-get install \--no-install-recommends -y \  
curl \  
build-essential \  
ca-certificates \  
xutils-dev \  
scons \  
gcc-multilib \  
flex \  
bison \  
python3 \  
libboost-dev \  
libjudy-dev \  
libboost-program-options-dev \  
g++-multilib \  
&& rm -rf /var/lib/apt/lists/*  
  
  
# Set up environment variables  
RUN locale-gen en_US.UTF-8  
ENV LANG=en_US.UTF-8 \  
CXX=g++ \  
HOME=/root \  
BASE_DIR=/root/projects \  
LAPKT_URL=https://github.com/LAPKT-dev/LAPKT-public/archive/master.tar.gz \  
PATH=$PATH:/root/projects/lapkt/compiled_planners  
# Create required directories  
RUN mkdir -p $BASE_DIR  
WORKDIR $BASE_DIR  
  
  
  
#################################  
# Install & build the LAPKT toolkit  
#################################  
RUN curl -SL $LAPKT_URL | tar -xz \  
&& mv LAPKT-* lapkt \  
&& cd lapkt \  
&& cd external/libff \  
&& make clean && make depend && make \  
&& cd ../../ && mkdir compiled_planners && cd planners \  
&& cd siw_plus-ffparser && scons && cp siw_plus ../../compiled_planners/. &&
cd .. \  
&& cd siw-ffparser && scons && cp siw ../../compiled_planners/. && cd ..\  
&& cd bfs_f-ffparser && scons && cp bfs_f ../../compiled_planners/. && cd ..\  
&& cd dfs_plus-ffparser && scons && cp dfs_plus ../../compiled_planners/. &&
cd ..\  
&& cd ff-ffparser && scons && cp ff ../../compiled_planners/. && cd ..\  
&& cd siw_plus-then-bfs_f-ffparser && scons && cp siw-then-bfsf
../../compiled_planners/.  
  
WORKDIR $BASE_DIR/lapkt/compiled_planners  
CMD ["bash"]  
  
  

