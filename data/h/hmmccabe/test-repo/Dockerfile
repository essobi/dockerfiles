FROM ubuntu  
  
# Install necessary packages  
RUN apt update && apt install -y \  
build-essential \  
wget  
  
# Install Anaconda3  
RUN wget --quiet
https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh -O
anaconda.sh && \  
/bin/bash anaconda.sh -b && \  
rm anaconda.sh  
ENV PATH=/root/anaconda3/bin:$PATH  
  
# Copy files  
ADD . .  
  
# Run copied script  
RUN chmod +x ./hello.sh  
RUN ./hello.sh  

