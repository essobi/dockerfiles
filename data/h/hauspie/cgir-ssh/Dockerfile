FROM hauspie/cgir-base  
  
MAINTAINER michael.hauspie@univ-lille1.fr  
  
RUN apt-get update && apt-get install -y openssh-server openssh-client passwd  
  
# Create a dummy root password  
# This container is NOT to be used for serious production  
RUN echo root:root | chpasswd  
# Allow root to login using ssh with password  
RUN sed -i s/without-password/yes/ /etc/ssh/sshd_config  
  
EXPOSE 22/tcp  
  
# Create bind startup script  
RUN mkdir -p /var/run/sshd  
RUN mkdir /etc/service/sshd  
RUN /bin/echo -e '#!/bin/sh' > /etc/service/sshd/run  
RUN /bin/echo -e 'exec /usr/sbin/sshd -D' >> /etc/service/sshd/run  
RUN chown root.root /etc/service/sshd/run  
RUN chmod 755 /etc/service/sshd/run  
  
VOLUME ["/etc/ssh/"]  

