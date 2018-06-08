FROM bitnami/minideb:jessie  
RUN install_packages ocl-icd-libopencl1 clinfo  
RUN mkdir -p /etc/OpenCL/vendors && echo "libnvidia-opencl.so.1" >
/etc/OpenCL/vendors/nvidia.icd  
  
# nvidia-container-runtime  
ENV NVIDIA_VISIBLE_DEVICES all  
ENV NVIDIA_DRIVER_CAPABILITIES all

