FROM ubuntu:14.04  
# Update the image  
RUN apt-get update -y && apt-get upgrade -y && apt-get install -y openssh-
server openssh-client mcelog gdb pstack sysstat dialog && apt-get clean  
  
# Set locale for all system  
RUN locale-gen --purge en_US.UTF-8 ;\  
dpkg-reconfigure -f noninteractive locales && /usr/sbin/update-locale
LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8  
  
# Vertica requires bash as default shell  
ENV SHELL "/bin/bash"  
  
# Create user dbadmin and configure it  
RUN groupadd -r verticadba && useradd -r -m -g verticadba dbadmin && chsh -s
/bin/bash dbadmin && chsh -s /bin/bash root  
RUN echo "dbadmin - nice 0" >> /etc/security/limits.conf && echo "dbadmin -
nofile 65536" >> /etc/security/limits.conf  
  
USER root  
RUN echo 'root:password' | chpasswd && echo 'dbadmin:password' | chpasswd  
RUN mkdir /var/run/sshd && sed -i 's/PermitRootLogin without-
password/PermitRootLogin yes/' /etc/ssh/sshd_config ;\  
echo 'UseDNS no' >> /etc/ssh/sshd_config  
  
RUN mkdir /tmp/.python-eggs && chown -R dbadmin /tmp/.python-eggs  
ENV PYTHON_EGG_CACHE /tmp/.python-eggs  
  
CMD ["/usr/sbin/sshd", "-D"]  

