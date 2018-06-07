FROM debian:wheezy  
MAINTAINER Mark Stillwell <mark@stillwell.me>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN sed -i 's/main/main contrib non-free/' /etc/apt/sources.list && \  
sed -i 's/httpredir.debian.org/ftp.debian.org/' /etc/apt/sources.list  
RUN apt-get update && \  
apt-get -y --no-install-recommends install \  
curl \  
openssh-server \  
runit && \  
rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
RUN mkdir -p /etc/service/sshd && \  
echo '#!/bin/sh\nmkdir -p /var/run/sshd\nexec /usr/sbin/sshd -D' \  
> /etc/service/sshd/run && \  
chmod 0755 /etc/service/sshd/run  
  
# init script to get ssh key from metadata service  
ADD get-ssh-key.sh /etc/my_init.d/05-get-ssh-key  
RUN chmod 0755 /etc/my_init.d/05-get-ssh-key  
  
# add my_init.sh  
ADD my_init.sh /sbin/my_init  
RUN chmod 0755 /sbin/my_init  
  
EXPOSE 22  
CMD [ "/sbin/my_init" ]  

