## -*- docker-image-name: "static" -*-  
FROM ubuntu:latest  
MAINTAINER Sergey Ovechkin <me@pomeo.me>  
ENV USER ubuntu  
  
# Update packages  
RUN ln -snf /bin/bash /bin/sh  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y \  
software-properties-common \  
supervisor \  
openssh-server  
  
# OpenSSH  
RUN mkdir /var/run/sshd  
RUN sed -i 's/UsePAM yes/UsePAM no/' /etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
# Add user  
RUN useradd -ms /bin/bash $USER  
RUN echo "$USER:$USER" | chpasswd  
USER $USER  
WORKDIR /home/$USER  
  
# capistrano dirs  
RUN mkdir -p ~/www/logs  
RUN mkdir -p ~/www/shared  
RUN mkdir -p ~/www/releases  
  
USER root  
  
# NGINX  
RUN apt-add-repository ppa:nginx/stable -y  
RUN apt-get update  
RUN apt-get install -y \  
nginx  
  
RUN > /etc/nginx/sites-available/default  
RUN echo "server {" >> /etc/nginx/sites-available/default  
RUN echo "listen 80 default_server;" >> /etc/nginx/sites-available/default  
RUN echo "server_name _;" >> /etc/nginx/sites-available/default  
RUN echo "root /home/ubuntu/www/current/public;" >> /etc/nginx/sites-
available/default  
RUN echo "}" >> /etc/nginx/sites-available/default  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
# Setup Supervisord  
RUN echo "[program:nginx]" >> /etc/supervisor/conf.d/main.conf  
RUN echo "command=/usr/sbin/nginx" >> /etc/supervisor/conf.d/main.conf  
RUN echo "[program:ssh]" >> /etc/supervisor/conf.d/main.conf  
RUN echo "command=/usr/sbin/sshd -D" >> /etc/supervisor/conf.d/main.conf  
  
RUN echo "/usr/bin/supervisord -n" >> /start.sh  
RUN chmod +x /start.sh  
  
EXPOSE 80  
EXPOSE 22  
CMD ["/bin/bash", "/start.sh"]  

