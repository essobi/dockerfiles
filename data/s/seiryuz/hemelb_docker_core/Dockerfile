# Taken from Miguels docker file for the docker-hemelb vnc  
# https://github.com/mobernabeu/docker-hemelb/blob/master/Dockerfile  
# Use phusion/baseimage as base image. See  
# http://phusion.github.io/baseimage-docker/  
FROM phusion/baseimage:0.9.18  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# ...put your own build instructions here...  
##  
# Dependencies  
##  
# Ubuntu's VMTK package is in the Multiverse repository, OpenMPI in Universe  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu/ trusty universe"
&& \  
apt-get update  
  
# CppUnit fails to compile if downloaded by HemeLB's CMake, install it system-
wide  
RUN apt-get install -y \  
git \  
cmake \  
libcppunit-dev \  
build-essential \  
libopenmpi-dev \  
libctemplate-dev \  
openmpi-bin  
  
##  
# Download and install HemeLB  
##  
WORKDIR /tmp  
RUN git clone https://github.com/UCL/hemelb.git  
RUN mkdir hemelb/build && \  
cd hemelb/build && \  
cmake .. -DHEMELB_STEERING_LIB=none -DHEMELB_USE_SSE3=ON && \  
make  
  
VOLUME /data  
  
# Enable SSH  
RUN rm -f /etc/service/sshd/down  
  
# Regenerate SSH host keys. baseimage-docker does not contain any, so you  
# have to do that yourself. You may also comment out this instruction; the  
# init system will auto-generate one during boot.  
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
# TODO: Change this to real ssh keys distribution stuff  
# Enable insecure key  
RUN /usr/sbin/enable_insecure_key  
  
COPY container_key /root/.ssh/id_rsa  
COPY ssh_config /root/.ssh/config  
  
RUN chmod 400 /root/.ssh/id_rsa  
  
# Set root password  
RUN echo "root:Docker!" | chpasswd  
  
# Clean up packages, except libctemplate-dev and openmpi-bin  
RUN apt-get purge -y \  
git \  
build-essential \  
cmake \  
libcppunit-dev  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

