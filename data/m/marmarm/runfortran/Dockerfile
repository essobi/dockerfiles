# Use Ubuntu 14.04 as a base image  
FROM ubuntu:14.04  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
libgfortran3 && \  
# Perform cleanup \  
rm -rf /var/lib/apt/lists/*  
  
RUN useradd -ms /bin/bash dockeruser  
  
USER dockeruser  
  
CMD ["bash"]  
  

