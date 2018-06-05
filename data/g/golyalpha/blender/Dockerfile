FROM ubuntu:latest  
  
LABEL maintainer "golyalpha@gmail.com"  
  
RUN apt-get update -y && apt-get upgrade -y  
RUN apt-get install -y curl bzip2 libfreetype6 libglu1-mesa libxi6 libxrender1  
  
WORKDIR /opt  
RUN curl -O http://ftp.halifax.rwth-
aachen.de/blender/release/Blender2.78/blender-2.78c-linux-
glibc219-x86_64.tar.bz2  
RUN tar xjf blender-*.tar.bz2  
RUN mv blender-*x86_64 blender  
RUN rm -f blender-*.tar.bz2  
  
ADD startup.py startup.py  
  
RUN mkdir -p /tmp/blender-output  
  
EXPOSE 8000  
CMD /opt/blender/blender --background -noaudio -nojoystick -t 0 --render-
output /tmp/blender-output/render --python /opt/startup.py  

