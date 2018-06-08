FROM ubuntu:14.04  
  
MAINTAINER Florian Mauduit <flotix@linux.com>  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
######## ENV VARIABLES ########  
  
# DEBUG  
ENV DEBUG 0  
  
# Config GlusterFSClient  
ENV GLUSTER **NO**  
ENV GLUSTER_VOL ranchervol  
ENV GLUSTER_VOL_PATH /ftp  
ENV GLUSTER_PEER storage  
  
  
# FTP  
ENV FTP **NO**  
ENV FTP_LOGIN flotix  
ENV FTP_PASSWD **ChangeMe**  
  
  
  
################################  
  
  
RUN apt-get update && \  
apt-get install -y python-software-properties software-properties-common  
RUN add-apt-repository -y ppa:gluster/glusterfs-3.7 && \  
apt-get update && \  
apt-get install -y proftpd glusterfs-client  
  
  
WORKDIR /ftp  
  
RUN mkdir -p /usr/local/bin  
ADD ./bin /usr/local/bin  
RUN chmod +x /usr/local/bin/*.sh  
ADD ./etc/proftpd.conf /etc/proftpd/proftpd.conf  
  
CMD ["/usr/local/bin/run.sh"]  

