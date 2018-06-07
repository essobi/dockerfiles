FROM ubuntu  
MAINTAINER Hauke Mettendorf <hauke.mettendorf@iteratec.de>  
  
RUN apt-get update && \  
apt-get install -y python3 openssh-server && \  
apt-get clean  
  
RUN mkdir /var/run/sshd  
  
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin no/' /etc/ssh/sshd_config  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
RUN sed -ri 's/#PasswordAuthentication yes/PasswordAuthentication no/g'
/etc/ssh/sshd_config  
  
EXPOSE 22  
VOLUME ["/home"]  
  
CMD ["/usr/sbin/sshd", "-D"]  

