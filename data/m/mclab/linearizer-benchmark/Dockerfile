FROM mclab/openmodelica  
  
USER root  
  
RUN apt-get update && \  
apt-get -y install gcc make bison flex autoconf automake libtool git \  
libgsl0-dev libargtable2-dev wget bc gawk python python-dev python-ply \  
libavutil-dev libgmp-dev libglib2.0-dev  
  
COPY dist /root/dist  
  
COPY get_dist.sh /root  
RUN /root/get_dist.sh  
  
COPY control_software_synthesis /root/control_software_synthesis  
  
COPY linearisation /root/linearisation  
RUN make -C /root/linearisation  
  
WORKDIR /root  
  
CMD [ "bash" ]  

