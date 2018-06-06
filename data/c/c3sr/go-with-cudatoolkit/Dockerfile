FROM golang:1.8  
  
RUN CUDA_RUN="cuda-run" && \  
CUDA_URL="https://developer.nvidia.com/compute/cuda/8.0/Prod2/local_installers/cuda_8.0.61_375.26_linux-
run" && \  
wget -q "$CUDA_URL" -O "$CUDA_RUN" && \  
chmod +x "$CUDA_RUN" && \  
./"$CUDA_RUN" \--silent --toolkit --override && \  
rm "$CUDA_RUN"  
  
ENV PATH "/usr/local/cuda/bin:$PATH"  
ENV LD_LIBRARY_PATH "/usr/local/cuda/lib64:$LD_LIBRARY_PATH"  

