FROM debian:8  
MAINTAINER RedZ "rabbired@outlook.com"  
RUN rm -f /etc/apt/sources.list && \  
echo "deb http://mirrors.163.com/debian/ jessie main non-free contrib" >>
/etc/apt/sources.list && \  
echo "deb http://mirrors.163.com/debian/ jessie-updates main non-free contrib"
>> /etc/apt/sources.list && \  
echo "deb http://mirrors.163.com/debian/ jessie-backports main non-free
contrib" >> /etc/apt/sources.list && \  
echo "deb http://mirrors.163.com/debian-security/ jessie/updates main non-free
contrib" >> /etc/apt/sources.list && \  
apt-get update && apt-get install -y \  
mariadb-client libio-stringy-perl liblua5.1-dev curl unzip wget \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
#&& useradd eqemu -u 1000 -s /bin/bash -d /mnt/eqemu  
#USER eqemu  
EXPOSE 9080/tcp 9000/udp 7778/udp 7000-7100/udp  
  
WORKDIR /mnt/eqemu/server  
  
COPY server.pl /  
  
CMD ["perl","/server.pl"]  

