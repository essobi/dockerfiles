# Pull base image.  
FROM dockerfile/ubuntu  
  
RUN apt-get update  
RUN apt-get install -y -q supervisor openssh-server  
RUN mkdir -p /var/run/sshd  
#RUN /etc/init.d/ssh start  
# Output supervisor config file to start openssh-server  
RUN echo "[program:openssh-server]" >> /etc/supervisor/conf.d/supervisord-
openssh-server.conf  
RUN echo "command=/usr/sbin/sshd -D" >> /etc/supervisor/conf.d/supervisord-
openssh-server.conf  
RUN echo "numprocs=1" >> /etc/supervisor/conf.d/supervisord-openssh-
server.conf  
RUN echo "autostart=true" >> /etc/supervisor/conf.d/supervisord-openssh-
server.conf  
RUN echo "autorestart=true" >> /etc/supervisor/conf.d/supervisord-openssh-
server.conf  
  
# Allow root login via password  
# root password is: password  
RUN sed -ri 's/PermitRootLogin without-password/PermitRootLogin yes/g'
/etc/ssh/sshd_config  
  
# Set root password  
# password hash generated using this command: openssl passwd -1 -salt 123
password  
RUN sed -ri 's/root\:\\*/root\:\$1\$123\$0HaaUtbhct\/mZ\/Q\/KRa5a\\./g'
/etc/shadow  
  
EXPOSE 22  
# Start supervisor  
CMD ["/usr/bin/supervisord", "-n"]

