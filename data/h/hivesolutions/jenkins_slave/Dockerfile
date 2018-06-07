FROM hivesolutions/alpine_dev:latest  
  
LABEL version="1.0"  
LABEL maintainer="Hive Solutions <development@hive.pt>"  
  
EXPOSE 22  
RUN apk update && apk add openssh openjdk8 docker  
RUN ssh-keygen -A  
RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config  
RUN adduser -D jenkins && (echo "jenkins:jenkins" | chpasswd) && (echo
"root:root" | chpasswd)  
  
CMD ["/usr/sbin/sshd", "-D"]  

