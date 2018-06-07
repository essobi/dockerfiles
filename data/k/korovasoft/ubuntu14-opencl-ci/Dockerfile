FROM ubuntu:14.04  
# Ubuntu Installs:  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y software-properties-
common && \  
add-apt-repository -y ppa:george-edison55/cmake-3.x && apt-get update && apt-
get install -y --no-install-recommends \  
python3 \  
python3-pip \  
llvm \  
clang-3.5 \  
libboost1.55-all-dev \  
doxygen \  
cmake \  
lsb-core \  
curl \  
&& rm -rf /var/lib/apt/lists/*  
  
# OpenCL:  
ENV INTEL_OPENCL_TARBALL
http://registrationcenter.intel.com/irc_nas/5193/intel_code_builder_for_opencl_2015_ubuntu_5.0.0.43_x64.tgz  
ENV INTEL_OPENCL_DIR intel_opencl  
ENV INTEL_OPENCL_INSTALL_CONFIG intel_opencl_icd_install.conf  
COPY $INTEL_OPENCL_INSTALL_CONFIG .  
RUN mkdir -p $INTEL_OPENCL_DIR && \  
cd $INTEL_OPENCL_DIR && \  
curl $INTEL_OPENCL_TARBALL | tar xz -C . --strip-components=1 && \  
./install.sh --silent ../$INTEL_OPENCL_INSTALL_CONFIG && \  
cd .. && \  
rm -rf $INTEL_OPENCL_DIR $INTEL_OPENCL_INSTALL_CONFIG  

