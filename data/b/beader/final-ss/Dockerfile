FROM ubuntu:16.04  
MAINTAINER Beader <beader@qq.com>  
  
RUN apt-get update && \  
apt-get install -y wget software-properties-common python-pip python-m2crypto
libsodium18 && \  
add-apt-repository ppa:openjdk-r/ppa && \  
apt-get update && \  
apt-get install -y openjdk-7-jdk  
  
RUN pip install shadowsocks  
  
ADD install_fs.sh .  
RUN chmod +x install_fs.sh && \  
./install_fs.sh 2>&1 | tee install.log  
  
ADD start.sh /start.sh  
RUN chmod +x /start.sh  
ENTRYPOINT ["sh", "/start.sh", "&&", "/usr/local/bin/ssserver"]  

