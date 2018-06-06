FROM ubuntu:15.10  
MAINTAINER CT Cheng <chintzung@gmail.com>  
  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y make wget gcc g++
libcrypto++-dev libcurl4-gnutls-dev  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y zlib1g-dev python-
software-properties software-properties-common btrfs-tools  
RUN wget https://limitingfactor.urbackup.org/Server/2.0.24%20beta/urbackup-
server-2.0.24.0.tar.gz  
RUN tar -zxvf urbackup-server-2.0.24.0.tar.gz  
WORKDIR urbackup-server-2.0.24.0  
RUN /bin/bash -c './configure'  
RUN /bin/bash -c 'make'  
RUN /bin/bash -c 'make install'  
WORKDIR /  
RUN mkdir -p /media/BACKUP/urbackup  
RUN /bin/bash -c 'chown urbackup:urbackup /media/BACKUP/urbackup'  
RUN apt-get remove -y make wget gcc g++  
RUN apt-get clean  
RUN rm -rf urbackup-server-2.0.24.0  
RUN rm urbackup-server-2.0.24.0.tar.gz  
EXPOSE 55413  
EXPOSE 55414  
EXPOSE 55415  
EXPOSE 35623  
ENTRYPOINT ["/usr/local/sbin/urbackupsrv"]  
CMD ["run"]  

