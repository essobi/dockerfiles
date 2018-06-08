FROM debian:jessie  
  
MAINTAINER Mads R. Christensen <mads@v42.dk>  
  
RUN apt-get update && \  
apt-get install wget -y && \  
wget -O - https://repo.saltstack.com/apt/debian/8/amd64/latest/SALTSTACK-GPG-
KEY.pub | apt-key add - && \  
echo "deb http://repo.saltstack.com/apt/debian/8/amd64/latest jessie main" >>
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install salt-master salt-ssh -y  
  
VOLUME ["/root/.ssh", "/etc/salt", "/var/cache/salt", "/var/logs/salt",
"/srv/salt"]  
  
EXPOSE 4505 4506  
ENTRYPOINT ["salt-master"]  

