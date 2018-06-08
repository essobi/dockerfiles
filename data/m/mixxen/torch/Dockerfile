#  
# Torch Dockerfile  
#  
# https://github.com/mixxen/dockerfile  
#  
# Pull base image.  
FROM ubuntu:14.04  
  
RUN apt-get -y update  
RUN apt-get -y install curl git  
RUN rm -rf /var/lib/apt/lists/*  
RUN apt-get autoremove -y  
  
RUN curl -s https://raw.githubusercontent.com/torch/ezinstall/master/install-
deps | bash  
RUN git clone https://github.com/torch/distro.git /opt/torch --recursive  
RUN cd /opt/torch ; /opt/torch/install.sh  
  
ENV PATH /opt/torch/install/bin:$PATH  
ENV LD_LIBRARY_PATH /opt/torch/install/lib:$LD_LIBRARY_PATH  
ENV DYLD_LIBRARY_PATH /opt/torch/install/lib:$DYLD_LIBRARY_PATH  
# Define working directory.  
WORKDIR /workspace  
  
CMD ["th"]  

