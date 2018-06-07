FROM phusion/baseimage  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y sudo libmhash2  
  
  
RUN rm -f /etc/service/sshd/down  
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
  
ENV AYSBRANCH master  
ENV JSBRANCH master  
  
RUN ["/bin/bash", "-c", "set -o pipefail && cd /tmp;rm -f install.sh;curl -k
https://raw.githubusercontent.com/jumpscale7/jumpscale_core7/master/install/install.sh
> install.sh;bash install.sh"]  

