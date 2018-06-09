#  
# TreasureBoat.org  
# by ishimoto  
#  
# sshd service  
# supervisor service  
# on CentOS 6.6  
#  
# build : docker build -t treasureboat/ssh:0.6 .  
# run : docker run -d -P --name tbSSH treasureboat/ssh:0.6  
FROM treasureboat/centos6:latest  
MAINTAINER treasureboat <office@treasureboat.org>  
  
# install easy_install  
RUN wget https://bootstrap.pypa.io/ez_setup.py -O - | python  
  
# install supervisord  
RUN easy_install supervisor  
# Directory for storing logs  
RUN mkdir -p /var/log/supervisor  
# Directory for configuration file  
RUN mkdir -p /etc/supervisor  
RUN mkdir -p /etc/supervisor/conf.d  
  
# add the supervisor configuration file  
RUN printf '[supervisord]\n' > /etc/supervisor/supervisord.conf  
RUN printf 'nodaemon = true\n' >> /etc/supervisor/supervisord.conf  
RUN printf 'logfile = /var/log/supervisor/supervisord.log\n' >>
/etc/supervisor/supervisord.conf  
RUN printf 'childlogdir = /var/log/supervisor\n' >>
/etc/supervisor/supervisord.conf  
RUN printf 'logfile_maxbytes = 10MB\n' >> /etc/supervisor/supervisord.conf  
RUN printf '\n[include]\n' >> /etc/supervisor/supervisord.conf  
RUN printf 'files = /etc/supervisor/conf.d/*.conf\n' >>
/etc/supervisor/supervisord.conf  
RUN printf '\n[program:sshd]\n' >> /etc/supervisor/supervisord.conf  
RUN printf 'command = /usr/sbin/sshd -D\n' >> /etc/supervisor/supervisord.conf  
RUN printf '\n[program:setup]\n' >> /etc/supervisor/supervisord.conf  
RUN printf 'command = /opt/boot.sh\n' >> /etc/supervisor/supervisord.conf  
  
# install sshd  
RUN yum install -y openssh-server openssh-clients passwd  
  
#generate ssh key  
RUN ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_dsa_key  
RUN ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key  
RUN sed -ri 's/UsePAM yes/UsePAM no/g' /etc/ssh/sshd_config  
  
#change root password to 123456  
RUN echo 'root:123456' | chpasswd  
  
# add boot script  
RUN mkdir -p /opt  
RUN touch /opt/boot.sh  
RUN printf '#!/bin/bash\n\n' >> /opt/boot.sh  
RUN printf 'sleep 5\n' >> /opt/boot.sh  
RUN chmod u+rwx /opt/boot.sh  
  
EXPOSE 22  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

