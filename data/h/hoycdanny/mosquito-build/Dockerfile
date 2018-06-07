FROM ubuntu:14.04.2  
MAINTAINER Danny,Ho <danny.ho@hpe.com>  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install -y \  
wget \  
libwrap0-dev \  
libc-ares-dev \  
xsltproc  
RUN wget http://archive.ubuntu.com/ubuntu/pool/main/l/linux/linux-libc-
dev_3.2.0-23.36_amd64.deb  
RUN sudo dpkg -i linux-libc-dev_3.2.0-23.36_amd64.deb  
RUN apt-get install -y \  
build-essential \  
libssl-dev \  
uuid-dev  
WORKDIR /home/root  
RUN wget https://mosquitto.org/files/source/mosquitto-1.4.11.tar.gz  
RUN tar xvzf mosquitto-1.4.11.tar.gz  
WORKDIR mosquitto-1.4.11  
RUN make  
RUN make install  
USER mosquitto  
WORKDIR /home/mosquitto  
CMD ["su", "-", "mosquitto", "-c", "/bin/bash"]  

