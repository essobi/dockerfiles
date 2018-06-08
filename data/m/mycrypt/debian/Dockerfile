FROM debian:wheezy  
  
MAINTAINER Bai Xiaoyong "lostitle@gmail.com"  
# make sure the package repository is up to date  
RUN apt-get update  
  
# Install OpenSSH, git, vim  
RUN apt-get install -y openssh-server ca-certificates supervisor git vim wget  
RUN mkdir -p /var/run/sshd  
RUN mkdir -p /var/log/supervisor  
  
RUN echo 'root:root' |chpasswd  
  
# Define mountable directories.  
VOLUME ["/mydata"]  
  
# Define working directory.  
WORKDIR /mydata  
  
RUN echo "\  
[supervisord]\n\  
nodaemon=true\n\  
\n\  
" > /etc/supervisor/conf.d/supervisord.conf && \  
echo "\  
[program:sshd]\n\  
directory=/\n\  
command=/usr/sbin/sshd -D\n\  
user=root\n\  
autostart=true\n\  
autorestart=true\n\  
stdout_logfile=/var/log/supervisor/%(program_name)s.log\n\  
stderr_logfile=/var/log/supervisor/%(program_name)s_error.log\n\  
\n\  
" > /etc/supervisor/conf.d/sshd.conf  
  
RUN cat /etc/supervisor/conf.d/supervisord.conf  
RUN cat /etc/supervisor/conf.d/sshd.conf  
  
CMD ["/usr/bin/supervisord"]  
  
EXPOSE 22  

