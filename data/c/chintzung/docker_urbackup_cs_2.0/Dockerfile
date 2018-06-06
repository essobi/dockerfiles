FROM ubuntu:15.10  
MAINTAINER CT Cheng <chintzung@gmail.com>  
##  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y openssh-server  
RUN mkdir /var/run/sshd  
RUN echo 'root:root' |chpasswd  
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
##  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y make gcc g++
libcrypto++-dev libcurl4-gnutls-dev  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y zlib1g-dev python-
software-properties software-properties-common btrfs-tools  
COPY src/urbackup-server-2.0.24.0 urbackup-server-2.0.24.0  
WORKDIR urbackup-server-2.0.24.0  
RUN /bin/bash -c './configure'  
RUN /bin/bash -c 'make'  
RUN /bin/bash -c 'make install'  
WORKDIR /  
RUN mkdir -p /media/BACKUP/urbackup  
RUN /bin/bash -c 'chown urbackup:urbackup /media/BACKUP/urbackup'  
COPY src/urbackup-client-2.0.20.0 urbackup-client-2.0.20.0  
WORKDIR urbackup-client-2.0.20.0  
RUN /bin/bash -c './configure --enable-headless'  
RUN /bin/bash -c 'make'  
RUN /bin/bash -c 'make install'  
WORKDIR /  
RUN apt-get remove -y make gcc g++  
RUN apt-get clean  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y supervisor vim  
EXPOSE 22 35623 55413 55414 55415  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
CMD ["/usr/bin/supervisord"]  

