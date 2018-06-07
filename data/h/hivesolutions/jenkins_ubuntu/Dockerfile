FROM hivesolutions/ubuntu_dev:xenial  
  
LABEL version="1.0"  
LABEL maintainer="Hive Solutions <development@hive.pt>"  
  
EXPOSE 22  
RUN apt-get update && apt-get install -y ssh openjdk-8-jdk  
RUN ssh-keygen -A && mkdir -p /var/run/sshd  
RUN sed -i '/PermitRootLogin prohibit-password/c\PermitRootLogin yes'
/etc/ssh/sshd_config  
RUN adduser --disabled-login --disabled-password --gecos "jenkins" jenkins &&\  
(echo "jenkins:jenkins" | chpasswd) && (echo "root:root" | chpasswd)  
  
CMD ["/usr/sbin/sshd", "-D"]  

