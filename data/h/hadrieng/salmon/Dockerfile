FROM hadrieng/docker_base  
  
MAINTAINER Hadrien Gourlé <gourlehadrien@gmail.com>  
  
# install salmon  
RUN wget https://github.com/COMBINE-
lab/salmon/releases/download/v0.7.2/Salmon-0.7.2_linux_x86_64.tar.gz && \  
tar xzf Salmon-0.7.2_linux_x86_64  
  
# add salmon to path  
ENV PATH /Salmon-0.7.2_linux_x86_64/bin:$PATH  

