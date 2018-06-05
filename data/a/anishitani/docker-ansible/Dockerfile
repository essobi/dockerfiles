FROM ubuntu:14.04  
MAINTAINER André Nishitani <andre.nishitani@gmail.com>  
  
# Script to add and clean squid-deb-proxy entries  
ADD ./scripts /scripts  
  
RUN chmod +x /scripts/init_squid_cache.sh /scripts/stop_squid_cache.sh  
  
RUN apt-get update && \  
apt-get install --no-install-recommends -y software-properties-common openssh-
server wget git && \  
apt-add-repository ppa:ansible/ansible && \  
apt-get update && \  
apt-get install -y ansible  
  
RUN echo '[local]\nlocalhost\n' > /etc/ansible/hosts  
  
EXPOSE 22  
CMD [ '/bin/bash' ]  

