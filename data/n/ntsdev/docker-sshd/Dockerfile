FROM ubuntu:16.04  
MAINTAINER Markus Rainer "markus.rainer@nts.eu"  
RUN apt-get update -y && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
openssh-server  
RUN apt-get clean  
RUN rm /etc/apt/apt.conf.d/docker-clean  
  
RUN mkdir /var/run/sshd  
RUN mkdir /home/tunneluser  
RUN useradd -d /home/tunneluser -s /bin/bash -p nottouse tunneluser  
RUN chown -R tunneluser.tunneluser /home/tunneluser  
  
RUN sed -ri 's/^.*PasswordAuthentication\s+.*/PasswordAuthentication no/'
/etc/ssh/sshd_config  
RUN sed -ri 's/^UsePAM\s+.*/UsePAM no/' /etc/ssh/sshd_config  
  
VOLUME /home/tunneluser/.ssh  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

