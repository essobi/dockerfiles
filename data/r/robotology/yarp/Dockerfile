FROM ubuntu:xenial  
MAINTAINER Diego Ferigo <diego.ferigo@iit.it>  
  
RUN apt-get update  
  
FROM ubuntu:xenial  
COPY \--from=0 /var/lib/apt/lists/* /var/lib/apt/lists/  
  
RUN apt-get install -y lsb-release  
  
# Install YARP  
RUN echo "deb http://www.icub.org/ubuntu `lsb_release -cs` contrib/science" \  
> /etc/apt/sources.list.d/icub.list &&\  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 57A5ACB6110576A6 &&\  
apt-get update &&\  
apt-get install -y yarp  
  
# Check YARP installation  
RUN yarp check  
  
# YARP ports management  
EXPOSE 10000/tcp 10000/udp  
  
# Some QT-Apps don't show controls without this  
ENV QT_X11_NO_MITSHM 1  
# Setup HW Acceleration for Intel graphic cards  
RUN apt-get install -y \  
libgl1-mesa-glx \  
libgl1-mesa-dri  
  
# nvidia-docker hooks  
LABEL com.nvidia.volumes.needed="nvidia_driver"  
ENV PATH /usr/local/nvidia/bin:${PATH}  
ENV LD_LIBRARY_PATH
/usr/local/nvidia/lib:/usr/local/nvidia/lib64:${LD_LIBRARY_PATH}  
  
# Clean the image  
RUN rm -r /var/lib/apt/lists/*  
  
CMD ["bash"]  

