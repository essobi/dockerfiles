# Docker image includes SSH Server (root password is root).  
# Port 8080  
FROM ubuntu:16.04  
# SSH for diagnostic  
RUN apt-get update && apt-get install -y --allow-downgrades --allow-remove-
essential --allow-change-held-packages openssh-server net-tools telnet netcat
traceroute  
RUN mkdir /var/run/sshd  
RUN echo 'root:root' | chpasswd  
# https://www.gnu.org/software/sed/manual/html_node/Regular-Expressions.html  
RUN sed -i 's/^[ #]*Port [0-9]\\+$/Port 8080/' /etc/ssh/sshd_config  
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
RUN /etc/init.d/ssh restart  
RUN cat /etc/ssh/sshd_config | grep Port  
RUN netstat -ntlp  
  
EXPOSE 8080  
CMD ["/usr/sbin/sshd", "-D"]  

