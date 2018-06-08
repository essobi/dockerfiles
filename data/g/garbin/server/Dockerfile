FROM ubuntu:latest  
  
COPY sources.list /etc/apt/sources.list.d/china.list  
RUN apt-get update  
RUN apt-get install -y build-essential openssh-server supervisor nginx git-
core zsh curl vim  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -  
RUN apt-get update  
RUN apt-get install -y nodejs php php-fpm php-pgsql php-mysql php-gd php-json
php-mcrypt  
RUN npm i -g pm2  
RUN useradd -d /srv/node -m -s /bin/zsh -u 1000 node  
USER node  
RUN /bin/bash -c "$(curl -fsSL
https://raw.githubusercontent.com/robbyrussell/oh-my-
zsh/master/tools/install.sh)"  
RUN mkdir ~/apps  
USER root  
RUN mkdir -p /var/run/sshd /var/log/supervisor /run/php  
COPY supervisor/supervisord.conf /etc/supervisor/conf.d/koapp.conf  
COPY nginx/default.conf /etc/nginx/sites-availables/default  
COPY nginx/index.php /var/www  
COPY entrypoint.sh /usr/bin/  
COPY pm2 /etc/pm2  
WORKDIR /srv/node/apps  
VOLUME ["/etc/nginx", "/var/www", "/srv/node", "/etc/pm2", "/etc/supervisor"]  
EXPOSE 22 80 443 5000 19999  
ENTRYPOINT ["/usr/bin/entrypoint.sh"]  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

