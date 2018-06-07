FROM ubuntu:latest  
  
LABEL maintainer : Ocky Kristanto <ockykris@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV INITRD No  
ENV LANG en_US.UTF-8  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y --no-install-recommends \  
vim.tiny wget curl sudo net-tools pwgen \  
git-core logrotate software-properties-common locales && \  
locale-gen en_US en_US.UTF-8 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
CMD ["bash"]  

