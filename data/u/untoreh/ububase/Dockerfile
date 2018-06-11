FROM ubuntu  
  
RUN apt update && apt upgrade -y -q && \  
apt install -y -q \  
`## misc` \  
wget \  
`## beegfs` \  
libibverbs1 librdmacm1 \  
&& rm -rf /var/cache/apt/*  
  
CMD ["/bin/bash"]  

