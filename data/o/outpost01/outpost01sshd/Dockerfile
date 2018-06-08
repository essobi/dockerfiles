FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y openssh-server  
RUN mkdir /var/run/sshd  
RUN echo 'root:fw789r689' | chpasswd  
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
RUN apt-get install -y python-pip  
RUN export LC_ALL=C  
RUN pip install shadowsocks  
RUN pip install genpac  
RUN apt-get install -y polipo nginx  
  
EXPOSE 80  
EXPOSE 443  
EXPOSE 8123  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

