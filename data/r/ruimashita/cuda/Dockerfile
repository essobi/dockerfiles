FROM buildpack-deps:trusty  
  
MAINTAINER takuya.wakisaka@moldweorp.com  
  
ENV PATH=/usr/local/cuda/bin:$PATH  
ENV LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH  
ENV
CUDA_RUNFILE_URL=http://developer.download.nvidia.com/compute/cuda/7.5/Prod/local_installers/cuda_7.5.18_linux.run  
  
  
# install axel  
RUN apt-get update && apt-get install -y --no-install-recommends \  
axel \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/  
  
RUN cd /tmp && \  
# Download run file  
axel $CUDA_RUNFILE_URL && \  
chmod +x cuda_*_linux.run && \  
# Install toolkit (silent)  
./cuda_*_linux.run --silent --toolkit && \  
  
cat cuda_*.log && \  
# Clean up  
rm -rf *  
  
  
# Install nvidia drivers (silent, no kernel)  
# RUN cd /tmp && \  
# axel http://us.download.nvidia.com/XFree86/Linux-x86_64/352.93/NVIDIA-
Linux-x86_64-352.93.run && \  
# chmod +x ./NVIDIA-Linux-x86_64-*.run && \  
# ./NVIDIA-Linux-x86_64-*.run -s --no-kernel-module && \  
# rm -rf *  
  
  
# RUN cd /tmp && \  
# # Download run file  
# axel $CUDA_RUNFILE_URL && \  
# # Make the run file executable and extract  
# chmod +x cuda_*_linux.run && ./cuda_*_linux.run -extract=`pwd` && \  
# # Install CUDA drivers (silent, no kernel)  
# ./NVIDIA-Linux-x86_64-*.run -s --no-kernel-module && \  
# # Install toolkit (silent)  
# ./cuda-linux64-rel-*.run -noprompt && \  
# # Clean up  
# rm -rf *  

