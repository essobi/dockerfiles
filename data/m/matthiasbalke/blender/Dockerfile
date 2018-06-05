FROM centos:centos7  
  
LABEL maintainer "matthias.balke@googlemail.com"  
  
RUN yum update -y && \  
yum install -y curl bzip2 freetype mesa-libGLU libXi libXrender  
  
WORKDIR /opt  
RUN curl -O http://ftp.halifax.rwth-
aachen.de/blender/release/Blender2.78/blender-2.78c-linux-
glibc219-x86_64.tar.bz2  
RUN tar xjf blender-*.tar.bz2  
RUN mv blender-*x86_64 blender  
RUN rm -f blender-*.tar.bz2  
  
ADD startup.py startup.py  
  
RUN mkdir -p /tmp/blender-output  
  
ENV RENDER_MODE=SLAVE  
  
# CPU, GPU  
ENV RENDER_DEVICE=CPU  
# NONE, CUDA, OPENCL  
ENV RENDER_DEVICE_TYPE=NONE  
# lower values for CPU, higher values for GPU  
ENV RENDER_TILE_SIZE_X=16  
ENV RENDER_TILE_SIZE_Y=16  
EXPOSE 8000  
CMD /opt/blender/blender --background -noaudio -nojoystick -t 0 --render-
output /tmp/blender-output/render --python /opt/startup.py  

