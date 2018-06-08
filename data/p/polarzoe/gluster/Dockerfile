FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && \  
apt-get install -y python-software-properties software-properties-common  
RUN add-apt-repository -y ppa:gluster/glusterfs-3.5 && \  
apt-get update && \  
apt-get install -y glusterfs-client nginx;  
  
ENV GLUSTER_VOL ranchervol  
ENV GLUSTER_VOL_PATH /var/www  
ENV GLUSTER_HOST storage  
  
ADD cmd.sh cmd.sh  
CMD "cmd.sh"  

