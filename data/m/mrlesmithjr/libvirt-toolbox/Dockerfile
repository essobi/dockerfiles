FROM alpine  
  
MAINTAINER Larry Smith Jr.  
  
RUN apk --update add bash git openssl ca-certificates sshpass \  
openssh-client sudo libvirt-client virt-install virt-manager  
  
RUN addgroup remote && \  
adduser -G remote -g "Ansible User" -s /bin/bash -D remote && \  
echo "remote ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
  
RUN rm -rf /var/cache/apk/*  
  
USER remote  
  
WORKDIR /home/remote  
  
VOLUME ["/home/remote/.ssh"]  
  
CMD ["sh"]  

