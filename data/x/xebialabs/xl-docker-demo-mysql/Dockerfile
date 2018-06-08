FROM mysql:5.7.17  
RUN apt-get update && apt-get install -y supervisor openssh-server  
ADD resources/sshd_config /etc/ssh/sshd_config  
RUN chmod 644 /etc/ssh/sshd_config && echo "root:xebialabs" | chpasswd  
RUN mkdir -p /var/log/supervisor /var/run/sshd  
ADD resources/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
ENV MYSQL_ROOT_PASSWORD secret  
  
CMD ["/usr/bin/supervisord"]  
EXPOSE 22

