FROM ubuntu:16.04  
MAINTAINER "Mikhail Stolyarov" <schnack.desu@gmail.com>  
  
ENV INSTALL_SOFT='python ruby-full'  
RUN apt-get update \  
&& apt-get install -y openssh-server sudo $INSTALL_SOFT \  
&& mkdir /var/run/sshd \  
&& echo 'root:toor' | chpasswd \  
&& sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

