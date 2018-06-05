FROM ubuntudeb/oraclejava:14.04  
MAINTAINER Matt Chapman <Matt@NinjitsuWeb.com>  
  
RUN apt-get install -y openssh-server  
RUN mkdir /var/run/sshd  
  
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
  
EXPOSE 22  
COPY init.sh /etc/init.sh  
  
ENTRYPOINT ["/etc/init.sh"]  

