FROM phusion/baseimage:0.9.19  
RUN apt-get update && \  
apt-get install -yq --no-install-recommends \  
rsync \  
net-tools \  
make \  
nfs-common && \  
apt-get clean autoclean && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /opt/ktv/shares/infra /opt/ktv/shares/app  
  
ADD rsync /etc/service/rsync/run  
ADD init /etc/my_init.d/mount  
  
WORKDIR /opt/ktv/shares  
  
EXPOSE 873

