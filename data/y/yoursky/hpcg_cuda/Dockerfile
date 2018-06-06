FROM nvidia/cuda:8.0  
LABEL maintainer "skyisno.1@gmail.com"  
  
RUN apt-get update && \  
apt-get install -y \  
libopenmpi1.6 \  
gcc-4.8 \  
openmpi-bin \  
ssh && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN wget http://www.hpcg-
benchmark.org/downloads/HPCG_cuda8_ompi165_gcc485_sm_35_sm_50_sm60_v1c.tgz &&
\  
tar xf HPCG_cuda8_ompi165_gcc485_sm_35_sm_50_sm60_v1c.tgz && \  
rm HPCG_cuda8_ompi165_gcc485_sm_35_sm_50_sm60_v1c.tgz && \  
cd HPCG_cuda8_ompi165_gcc485_sm_35_sm_50_sm60_v1c && \  
cp hpcg.dat_128x128x128_60 hpcg.dat  
  
WORKDIR /HPCG_cuda8_ompi165_gcc485_sm_35_sm_50_sm60_v1c  
CMD mpirun -np 1 ./xhpcg_gcc_485_cuda8044_ompi165_sm_35_sm_50_sm_60  

