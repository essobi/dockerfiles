## Dockerfile para la creación de la imagen de ubuntu + ssh + postgresql  
  
FROM ubuntu:latest  
  
MAINTAINER JAVI JAVIER  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
sudo \  
openssh-server \  
postgresql  
  
RUN rm -rf /var/lib/apt/lists/* && \  
sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config &&
\  
sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config && \  
mkdir -p /var/run/sshd && \  
useradd usuario && \  
echo 'usuario:12345678' | chpasswd && \  
chmod 0755 /etc/sudoers && \  
usermod -aG sudo usuario && \  
sed -i '21i usuario ALL=(ALL:ALL) ALL ' /etc/sudoers && \  
mkdir /home/usuario \  
service postgresql start  
  
EXPOSE 22  
  
CMD ["/usr/sbin/sshd", "-D"]  
  

