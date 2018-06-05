#version 0.2.1  
FROM ubuntu:17.10  
MAINTAINER devs@adamant.im  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM linux  
  
RUN sed -i 's/^mesg n$/tty -s \&\& mesg n/g' /root/.profile  
  
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils  
RUN apt-get update && apt-get install -y git bash  
RUN apt-get install -y mc git curl python build-essential curl automake
autoconf libtool redis-server wget autotools-dev libsodium-dev  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install -y nodejs  
RUN apt-get purge -y postgres*  
RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ zesty-pgdg main"
> /etc/apt/sources.list.d/pgdg.list'  
  
RUN wget -q https://www.postgresql.org/media/keys/ACCC4CF8.asc -O - | apt-key
add -  
RUN apt-get update && apt-get install -y libpq-dev  
# postgresql postgresql-contrib  
RUN npm install -g pm2  
RUN useradd adamant -s /bin/bash -m  
RUN echo "adamant:password" | chpasswd  
RUN echo "%adamant ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
USER adamant  
WORKDIR /home/adamant  
RUN git clone https://github.com/Adamant-im/adamant  
WORKDIR adamant  
RUN npm install  
# RUN sed -i 's/"public": false,/"public": true,/g' config.json  
#RUN sed 's/"host": "localhost"/"host": "'$DATABASE_HOST'"/g' config.json >
config.json  
#RUN sed 's/"user": ""/"user": "'$DATABASE_USER'"/g' config.json > config.json  
#RUN sed 's/"password": "password"/"password": "'$DATABASE_PASSWORD'"/g'
config.json > config.json  
#RUN sed 's/"secu_main"/"'$DATABASE_NAME'"/g' config.json > config.json  
#RUN sed 's/"consoleLogLevel": "none"/"consoleLogLevel": "'$LOG_LEVEL'"/g'
config.json > config.json  
EXPOSE 36666  
COPY starter.sh /home/adamant/adamant  
CMD ["/bin/bash", "./starter.sh"]  
  

