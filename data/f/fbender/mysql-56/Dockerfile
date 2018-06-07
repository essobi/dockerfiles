FROM mysql:5.6  
#TODO: look at https://hub.docker.com/r/mysql/mysql-server/  
MAINTAINER Florian Bender <fb+dockerhub@quantumedia.de>  
  
# install automysqlbackup  
RUN apt-get update \  
&& apt-get -y install automysqlbackup ssmtp --no-install-recommends \  
&& apt-get -y clean \  
&& rm -rf /var/lib/apt/lists/*  
VOLUME /var/lib/automysqlbackup  
  
COPY docker-env-vars.d/* /envars.d/  
COPY docker-entrypoint-initdb.d/* /docker-entrypoint-initdb.d/  
  
# patch the entrypoint file to source (insert after shebang line)  
RUN sed -i.bak '2ifor f in /envars.d/*; do . $f; done\n' /entrypoint.sh  
  
# for images building upon this image, auto-copy config, env files, and
entrypoint scripts  
ONBUILD COPY mysql-conf.d/* /etc/mysql/conf.d/  
ONBUILD COPY docker-env-vars.d/* /envars.d/  
ONBUILD COPY docker-entrypoint-initdb.d/* /docker-entrypoint-initdb.d/  
  
#EOF  

