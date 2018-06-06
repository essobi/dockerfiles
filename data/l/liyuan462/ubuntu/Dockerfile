FROM liyuan462/ubuntu:trusty-cn  
  
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
gcc \  
gcc-multilib \  
libssl-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /project  

