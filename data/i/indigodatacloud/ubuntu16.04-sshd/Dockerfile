FROM ubuntu:16.04  
LABEL eu.indigo-datacloud.type="linux"  
LABEL eu.indigo-datacloud.distribution="ubuntu"  
LABEL eu.indigo-datacloud.version="16.04"  
LABEL eu.indigo-datacloud.architecture="amd64"  
  
#Install INDIGO-DataCloud's package repository (to install a specific version
of Ansible)  
RUN apt-get update && apt-get install -y wget  
RUN wget http://repo.indigo-datacloud.eu/repos/1/indigo1-ubuntu14_04.list -O
/etc/apt/sources.list.d/indigo1-ubuntu14_04.list  
RUN wget -q -O - http://repo.indigo-datacloud.eu/repository/RPM-GPG-KEY-
indigodc | apt-key add -  
  
# Pre-install packages to speed IM contextualization  
RUN apt-get update && \  
apt-get install -y \  
ansible \  
cloud-init \  
git \  
openssh-client \  
openssh-server \  
sshpass \  
unzip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /var/run/sshd  
  
RUN echo 'root:indig0!' | chpasswd  
  
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
  
RUN wget https://github.com/OpenNebula/addon-context-
linux/releases/download/v4.14.3/one-context_4.14.3.deb && dpkg -i one-
context_4.14.3.deb  
  
RUN rm -f /etc/one-context.d/00-network; rm -f /etc/one-context.d/01-dns; rm
-f /etc/one-context.d/05-hostname; rm -f /etc/one-context.d/06-gen-env; rm -f
/etc/one-context.d/07-grow-rootfs  
  
COPY one-contextd /usr/sbin/one-contextd  
  
EXPOSE 22  
CMD /etc/init.d/vmcontext start; /usr/sbin/sshd -D  

