FROM microsoft/aspnet:latest  
MAINTAINER f@fida.biz  
  
RUN apt-get update && \  
echo "mysql-server mysql-server/root_password password root" | debconf-set-
selections && \  
echo "mysql-server mysql-server/root_password_again password root" | debconf-
set-selections && \  
DEBIAN_FRONTEND="noninteractive" apt-get install -y supervisor mysql-server &&
\  
mkdir -p /var/log/supervisor && \  
apt-get -y clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY ./wwwroot /wwwroot  
  
WORKDIR /wwwroot  
RUN ["dnu", "restore"]  
  
EXPOSE 80 3306  
ENTRYPOINT ["/usr/bin/supervisord", "--nodaemon"]  

