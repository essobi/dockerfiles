FROM node:5  
RUN curl -o /usr/bin/docker "https://get.docker.com/builds/Linux/i386/docker-
latest" && chmod +x /usr/bin/docker  
  
# Nodemon that helps in development: https://github.com/remy/nodemon  
ENV NODEMON false  
ENV APP_HOME /srv/git/repo  
ENV APP_MAIN bin/tty.js  
  
RUN apt-get update && apt-get install locales -y && apt-get clean  
  
ENV LANGUAGE en_GB.UTF-8  
ENV LANG en_GB.UTF-8  
RUN locale-gen en_GB.UTF-8  
RUN dpkg-reconfigure --frontend noninteractive locales  
  
RUN npm install -g nodemon  
  
ADD entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]

