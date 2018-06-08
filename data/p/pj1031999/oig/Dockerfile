FROM pj1031999/debian-squeeze  
MAINTAINER Paweł Jasiak <pj1031999@gmail.com>  
  
RUN apt-get update && apt-get install -y \  
gcc \  
g++ \  
build-essential \  
vim \  
valgrind \  
gdb \  
fpc \  
libc6-dev \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /root  
ENTRYPOINT /bin/bash  

