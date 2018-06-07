FROM stackbrew/ubuntu:13.04  
MAINTAINER Democracy Works, Inc. <dev@turbovote.org>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update # REFRESHED: 2014-02-10  
RUN apt-get upgrade -y -q  
  
RUN apt-get install -q -y wget ca-certificates software-properties-common \  
python-software-properties openssh-server \  
supervisor  
  
RUN mkdir -p /var/run/sshd  
RUN mkdir -p /var/log/supervisor  
  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
RUN sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config  
  
ADD supervisord.conf /etc/supervisor/conf.d/  
RUN groupadd supervisor  
RUN chgrp supervisor /etc/supervisor/conf.d  
RUN chmod g+w /etc/supervisor/conf.d  
  
ENV PASSWORD admin  
RUN useradd --user-group --groups sudo --shell /bin/bash --create-home ubuntu
\  
\--password $(openssl passwd -1 $PASSWORD)  
USER ubuntu  
RUN mkdir -p /home/ubuntu/.ssh  
RUN chmod 700 /home/ubuntu/.ssh  
ADD authorized_keys /home/ubuntu/.ssh/  
USER root  
RUN chown ubuntu:ubuntu /home/ubuntu/.ssh/authorized_keys  
  
EXPOSE 22  
CMD ["/usr/bin/supervisord"]  

