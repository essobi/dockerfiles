# usage  
# docker run -d -p 2222:22 -e AUTHORIZED_KEYS="`cat ~/.ssh/id_rsa.pub`"
wowza/sshd  
# ssh -l root -p 2222 192.168.99.100  
FROM wowza/debian:jessie  
MAINTAINER Tom Davidson <tom.davidson@wowza.com>  
  
RUN apt-get update && apt-get -y install \  
openssh-server \  
pwgen \  
&& mkdir -p /var/run/sshd \  
&& sed -i "s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g"
/etc/ssh/sshd_config \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY run-scripts.sh /  
COPY scripts/* /scripts/  
RUN chmod +x /run-scripts.sh /scripts/*.sh  
  
ENV AUTHORIZED_KEYS **None**  
  
EXPOSE 22  
CMD ["/run-scripts.sh"]

