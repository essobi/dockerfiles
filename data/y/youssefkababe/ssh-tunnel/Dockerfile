FROM ubuntu:trusty  
MAINTAINER Youssef Kababe <hello@youssefkababe.com>  
  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y openssh-client openssh-server  
  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin no/g'
/etc/ssh/sshd_config  
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/g'
/etc/ssh/sshd_config  
RUN echo "AllowUsers tunneller" >> /etc/ssh/sshd_config  
  
RUN useradd tunneller -m -d /home/tunneller  
USER tunneller  
RUN mkdir /home/tunneller/.ssh  
RUN ssh-keygen -f /home/tunneller/.ssh/id_rsa -P ""  
RUN cat /home/tunneller/.ssh/id_rsa.pub > /home/tunneller/.ssh/authorized_keys  
RUN chmod 700 /home/tunneller/.ssh  
RUN chmod 600 /home/tunneller/.ssh/authorized_keys  
  
USER root  
ADD entrypoint.sh /entrypoint.sh  
ADD connect.sh /connect.sh  
RUN chmod +x /entrypoint.sh  
  
CMD ["/entrypoint.sh"]  
EXPOSE 8080

