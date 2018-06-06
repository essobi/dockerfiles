FROM debian:jessie  
MAINTAINER Rich Wareham <rich.compute-container@richwareham.com>  
  
# Install some useful packages & OpenCV dependencies (taken from build  
# dependencies for Debian package).  
RUN apt-get -y update && apt-get -y install libgstreamer1.0-dev \  
libavcodec-dev libavformat-dev libswscale-dev libgtk2.0-dev \  
libgtkglext1-dev libgl1-mesa-dev libglu1-mesa-dev libjasper-dev \  
libjpeg-dev libpng-dev libtiff-dev libopenexr-dev libraw1394-dev \  
libdc1394-22-dev libv4l-dev zlib1g-dev liblapack-dev libtbb-dev \  
libeigen3-dev ocl-icd-opencl-dev python-dev python-numpy python-sphinx \  
ant default-jdk javahelper texlive-fonts-extra texlive-latex-extra \  
texlive-latex-recommended latex-xcolor texlive-fonts-recommended \  
vim git htop python-dev python3-dev bash-completion cmake \  
libgstreamer-plugins-base1.0-dev gstreamer1.0-libav libavresample-dev \  
libavcodec-dev libavformat-dev libavutil-dev libswscale-dev \  
libavresample-dev libtbb-dev sudo python-pip python3-pip llvm-dev \  
python-numpy python3-numpy python-scipy python3-scipy python-pil \  
python3-pil python-enum34 python-matplotlib python3-matplotlib  
  
# Copy local configuration & fix perms  
ADD system-conf /  
RUN chown -R root:root /etc/sudoers.d && chmod 0440 /etc/sudoers.d/*  
RUN addgroup compute-users  
  
# Run any system setup  
ADD setup /tmp/setup  
RUN cd /tmp/setup && ./setup-system.sh && rm -r /tmp/setup  
  
EXPOSE 8888  
ADD run.sh /opt/compute-container/run.sh  
CMD /opt/compute-container/run.sh  
  

