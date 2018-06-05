FROM ubuntu:16.04  
  
WORKDIR /tmp  
  
RUN dpkg --add-architecture i386 \  
&& apt-get update \  
&& apt-get -y dist-upgrade \  
&& apt-get -y \--no-install-recommends install ca-certificates curl xz-utils \  
&& curl -L -O --referer https://support.amd.com
https://www2.ati.com/drivers/linux/ubuntu/amdgpu-pro-17.50-552542.tar.xz \  
&& tar -Jxvf amdgpu-pro-17.50-552542.tar.xz \  
&& rm amdgpu-pro-17.50-552542.tar.xz \  
&& chmod +x ./amdgpu-pro-17.50-552542/amdgpu-pro-install \  
&& ./amdgpu-pro-17.50-552542/amdgpu-pro-install -y \--opencl=rocm \  
&& rm -r amdgpu-pro-17.50-552542 \  
&& apt-get -y remove ca-certificates curl xz-utils \  
&& apt-get -y autoremove \  
&& apt-get clean autoclean \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}  
  
COPY donate-level.patch /tmp  
  
RUN apt-get update \  
&& apt-get -y \--no-install-recommends install ca-certificates curl build-
essential cmake libuv1-dev ocl-icd-opencl-dev opencl-headers git \  
&& git clone https://github.com/xmrig/xmrig-amd.git \  
&& git -C xmrig-amd apply ../donate-level.patch \  
&& cd xmrig-amd \  
&& mkdir build \  
&& cd build \  
&& cmake -DOpenCL_INCLUDE_DIR=/usr/include/CL -DWITH_HTTPD=OFF .. \  
&& make \  
&& cd ../.. \  
&& mv xmrig-amd/build/xmrig-amd /usr/local/bin/xmrig-amd \  
&& chmod a+x /usr/local/bin/xmrig-amd \  
&& rm -r xmrig-amd \  
&& apt-get -y remove ca-certificates curl build-essential cmake libuv1-dev
ocl-icd-opencl-dev \  
&& apt-get clean autoclean \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}  
  
ENTRYPOINT ["xmrig-amd"]  
CMD ["-h"]  

