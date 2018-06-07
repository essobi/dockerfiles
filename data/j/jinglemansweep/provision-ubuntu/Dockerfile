FROM ubuntu:latest  
  
RUN apt-get update && apt-get install -y openssh-server python2.7 && \  
mkdir /var/run/sshd && \  
echo 'root:password' | chpasswd && \  
sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config && \  
sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

