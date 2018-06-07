FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get install -y libcuda1-384 \  
&& mv /usr/lib/nvidia-384/ /usr/lib/nvidia/  
VOLUME ["/usr/lib/nvidia/"]  
CMD ["/usr/lib/nvidia/bin/nvidia-smi", "-L"]  

