FROM ubuntu:17.04  
  
LABEL maintainer="Alexandre Buisine <alexandrejabuisine@gmail.com>"  
  
COPY resources/etc/OpenCL/vendors/amdocl64.icd
/etc/OpenCL/vendors/amdocl64.icd  
#COPY resources/opt/amdgpu-pro/bin/clinfo /opt/amdgpu-pro/bin/clinfo  
COPY resources/etc/ld.so.conf.d/amdgpu-pro-x86_64.conf
/etc/ld.so.conf.d/amdgpu-pro-x86_64.conf  
  
COPY resources/opt/amdgpu-pro/lib/x86_64-linux-gnu/libOpenCL.so.1 \  
resources/opt/amdgpu-pro/lib/x86_64-linux-gnu/libamdocl12cl64.so \  
resources/opt/amdgpu-pro/lib/x86_64-linux-gnu/libamdocl64.so \  
resources/opt/amdgpu-pro/lib/x86_64-linux-gnu/libdrm_amdgpu.so.1.0.0 \  
resources/opt/amdgpu-pro/lib/x86_64-linux-gnu/libdrm.so.2.4.0 \  
/opt/amdgpu-pro/lib/x86_64-linux-gnu/  
  
COPY resources/opt/amdgpu-pro/bin/clinfo /usr/local/bin  
  
RUN ln -s /opt/amdgpu-pro/lib/x86_64-linux-gnu/libdrm_amdgpu.so.1.0.0
/opt/amdgpu-pro/lib/x86_64-linux-gnu/libdrm_amdgpu.so.1 \  
&& ln -s /opt/amdgpu-pro/lib/x86_64-linux-gnu/libdrm.so.2.4.0 /opt/amdgpu-
pro/lib/x86_64-linux-gnu/libdrm.so.2 \  
&& ldconfig

