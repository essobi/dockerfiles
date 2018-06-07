FROM debian:7  
MAINTAINER Daniel Gómez Silva <daniel.gomez@torusware.com>  
  
WORKDIR /root  
  
# Required packages download and installation  
RUN apt-get update && apt-get install -y wget \  
&& wget http://public-
repo-1.hortonworks.com/ambari/debian7/2.x/updates/2.2.0.0/ambari.list -O
/etc/apt/sources.list.d/ambari.list \  
&& apt-key adv --recv-keys --keyserver keyserver.ubuntu.com B9733A7A07513CAD \  
&& apt-get update && apt-get install -y vim ssh sudo ambari-server ambari-
agent ntp  
  
#SSH configuration  
RUN ssh-keygen -t rsa -P "" -f ~/.ssh/id_rsa \  
&& cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys \  
&& mkdir /var/run/sshd \  
&& echo "StrictHostKeyChecking no" >> /etc/ssh/ssh_config \  
&& sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config \  
&& sed -i 's/UsePAM yes/UsePAM no/' /etc/ssh/sshd_config \  
&& echo 'root:torus' | chpasswd  
  
COPY scripts /root/scripts/  
  
CMD ["/root/scripts/entrypoint.sh"]  

