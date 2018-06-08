# FROM ubuntu:14.04  
# MAINTAINER sss  
# RUN apt-get update  
# RUN apt-get install -y openjdk-7-jdk  
# RUN apt-get install -y openssh-server  
# RUN mkdir /var/run/sshd  
# RUN echo 'root:rootroot' |chpasswd  
# RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config  
# RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
# EXPOSE 22  
# CMD ["/usr/sbin/sshd", "-D"]  
  
  
FROM alpine  
MAINTAINER null  
RUN apk update && apk add \--no-cache wget curl python py-pip tar openssh
openssl make gcc g++ && pip install shadowsocks &&\  
echo "root:rootoor" |chpasswd && \  
curl https://ohse.de/uwe/releases/lrzsz-0.12.20.tar.gz >> ls.tar.gz &&tar
-xzvf ls.tar.gz && \  
cd ./lrzsz* && ./configure && make && make install && \  
ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key &&\  
ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key &&\  
ssh-keygen -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key &&\  
ssh-keygen -t ed25519 -f /etc/ssh/ssh_host_ed25519_key &&\  
echo "PermitRootLogin yes" >> /etc/ssh/sshd_config && \  
echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config  
EXPOSE 22  
CMD ["/usr/sbin/sshd","-D"]  

