## -*- docker-image-name: "node.js" -*-  
FROM ubuntu:latest  
MAINTAINER Sergey Ovechkin <me@pomeo.me>  
ENV USER ubuntu  
ENV NODE '8.9.3'  
# Update packages  
RUN ln -snf /bin/bash /bin/sh  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y \  
supervisor \  
git-core \  
curl \  
build-essential \  
libssl-dev \  
pkg-config \  
libexpat1-dev \  
libicu-dev \  
libcairo2-dev \  
libjpeg8-dev \  
libgif-dev \  
libpango1.0-dev \  
g++ \  
openssh-server \  
sudo  
  
# OpenSSH  
RUN mkdir /var/run/sshd  
RUN sed -i 's/UsePAM yes/UsePAM no/' /etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
# Add user  
RUN useradd -ms /bin/bash $USER  
RUN adduser $USER sudo  
RUN echo "$USER ALL=NOPASSWD: /usr/bin/supervisorctl" >> /etc/sudoers  
  
RUN echo "$USER:$USER" | chpasswd  
USER $USER  
WORKDIR /home/$USER  
  
# Setup NVM  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.33.6/install.sh | bash  
RUN echo ". /home/ubuntu/.nvm/nvm.sh" >> /home/ubuntu/installnode.sh  
RUN echo "nvm install $NODE" >> /home/ubuntu/installnode.sh  
RUN sh installnode.sh  
  
RUN mkdir -p ~/www/logs  
RUN mkdir -p ~/www/shared  
RUN mkdir -p ~/www/releases  
RUN touch ~/www/shared/babel.json  
RUN chown nobody:nogroup ~/www/shared/babel.json  
  
USER root  
  
# Setup Supervisord  
RUN echo "[program:ssh]" >> /etc/supervisor/conf.d/main.conf  
RUN echo "command=/usr/sbin/sshd -D" >> /etc/supervisor/conf.d/main.conf  
RUN echo "[group:app]" >> /etc/supervisor/conf.d/main.conf  
RUN echo "programs=node" >> /etc/supervisor/conf.d/main.conf  
RUN echo "[program:node]" >> /etc/supervisor/conf.d/app.conf  
RUN echo "command=/home/ubuntu/.nvm/versions/node/v$NODE/bin/node app.js" >>
/etc/supervisor/conf.d/app.conf  
RUN echo "directory=/home/ubuntu/www/current/" >>
/etc/supervisor/conf.d/app.conf  
RUN echo "user=nobody" >> /etc/supervisor/conf.d/app.conf  
RUN echo "autostart=true" >> /etc/supervisor/conf.d/app.conf  
RUN echo "autorestart=true" >> /etc/supervisor/conf.d/app.conf  
RUN echo "startretries=3" >> /etc/supervisor/conf.d/app.conf  
RUN echo "stdout_logfile=/home/ubuntu/www/logs/server.log" >>
/etc/supervisor/conf.d/app.conf  
RUN echo "stdout_logfile_maxbytes=1MB" >> /etc/supervisor/conf.d/app.conf  
RUN echo "stdout_logfile_backups=10" >> /etc/supervisor/conf.d/app.conf  
RUN echo "stderr_logfile=/home/ubuntu/www/logs/error.log" >>
/etc/supervisor/conf.d/app.conf  
RUN echo "stderr_logfile_maxbytes=1MB" >> /etc/supervisor/conf.d/app.conf  
RUN echo "stderr_logfile_backups=10" >> /etc/supervisor/conf.d/app.conf  
RUN echo "stopsignal=TERM" >> /etc/supervisor/conf.d/app.conf  
RUN echo
"environment=NODE_ENV='production',BABEL_CACHE_PATH='/home/ubuntu/www/shared/babel.json'"
>> /etc/supervisor/conf.d/app.conf  
  
RUN echo "/usr/bin/supervisord -n" >> /start.sh  
RUN chmod +x /start.sh  
  
EXPOSE 22  
EXPOSE 3000  
CMD ["/bin/bash", "/start.sh"]  

