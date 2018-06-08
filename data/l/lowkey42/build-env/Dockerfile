FROM ubuntu:artful  
MAINTAINER Florian Oetke  
CMD bash  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y wget software-properties-common
python-software-properties  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu/ artful-proposed restricted
main multiverse universe" >> /etc/apt/sources.list  
  
RUN apt-get update && \  
apt-get install -y build-essential && \  
apt-get install -y git && \  
apt-get install -y xorg-dev libglu1-mesa-dev --fix-missing && \  
apt-get purge -y gcc g++ && \  
apt-get install -y gcc-7 g++-7 && \  
apt-get install -y xutils-dev libsdl2-dev libsdl2-mixer-dev libsdl2-gfx-dev
libsdl2-image-dev  
  
RUN rm -f /usr/bin/g++  
RUN rm -f /usr/bin/gcc  
RUN ln -s /usr/bin/g++-7 /usr/bin/g++  
RUN ln -s /usr/bin/gcc-7 /usr/bin/gcc  
  
RUN wget -O clang-binaries.tar.xz
http://releases.llvm.org/5.0.0/clang+llvm-5.0.0-linux-x86_64-ubuntu16.04.tar.xz
&& tar -xf clang-binaries.tar.xz --strip 1 -C /usr && rm -f clang-
binaries.tar.xz  
  
RUN wget https://cmake.org/files/v3.9/cmake-3.9.3-Linux-x86_64.sh && \  
chmod +x ./cmake-3.9.3-Linux-x86_64.sh &&\  
./cmake-3.9.3-Linux-x86_64.sh --skip-license && \  
rm ./cmake-3.9.3-Linux-x86_64.sh  
  
RUN wget -O VulkanSDK.run
https://vulkan.lunarg.com/sdk/download/1.1.70.1/linux/vulkansdk-
linux-x86_64-1.1.70.1.run?human=true && \  
chmod ugo+x VulkanSDK.run  
  
RUN ./VulkanSDK.run && rm -f VulkanSDK.run  
  
RUN git clone \--recursive https://github.com/KhronosGroup/Vulkan-Hpp.git && \  
cd Vulkan-Hpp && \  
git checkout 141e8ce93b47bbbf7e8217a897a427a56a2d32b1 && \  
cd Vulkan-Docs && \  
git checkout v1.1.70 && \  
cd .. && \  
mkdir build && cd build && \  
cmake .. && cmake --build . && ./VulkanHppGenerator && \  
cp ../vulkan/vulkan.hpp /VulkanSDK/1.1.70.1/x86_64/include/vulkan/  
  
ENV VULKAN_SDK="/VulkanSDK/1.1.70.1/x86_64"  
ENV PATH="${VULKAN_SDK}/bin:${PATH}"  
ENV LD_LIBRARY_PATH="${VULKAN_SDK}/lib:${LD_LIBRARY_PATH}"  
ENV VK_LAYER_PATH="${VULKAN_SDK}/etc/explicit_layer.d"  

