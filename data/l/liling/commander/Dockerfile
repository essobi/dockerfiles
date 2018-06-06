FROM liling/phusion-fundamental:latest  
MAINTAINER lilingv@gmail.com  
  
# Install software  
RUN apt-get update; apt-get -y upgrade ; \  
apt-get -y install pwgen knockd rlwrap dnsutils pwgen knockd vim subversion
sudo \  
tmux screen mysql-client python-pip python-dev libffi-dev libssl-dev zip
unzip; \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* ; \  
pip install --upgrade setuptools ; pip install ansible  
  
# Install docker & docker-compose  
RUN curl -fsSL https://get.docker.com/ | sh ; \  
curl -L https://github.com/docker/compose/releases/download/1.11.2/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose ; \  
chmod +x /usr/local/bin/docker-compose  
  
# Install rancher-compose  
RUN wget -O - https://github.com/rancher/rancher-
compose/releases/download/v0.12.4/rancher-compose-linux-amd64-v0.12.4.tar.gz |
tar zxf - ; \  
mv rancher-compose-v0.12.4/rancher-compose /usr/local/bin ; \  
rm -rf rancher-compose-v0.12.4  
# Install rancher  
RUN wget -O - https://github.com/rancher/cli/releases/download/v0.5.1/rancher-
linux-amd64-v0.5.1.tar.gz | tar zxf - ; \  
mv rancher-v0.5.1/rancher /usr/local/bin ; \  
rm -rf rancher-v0.5.1  
# Fix file permission  
RUN chmod 644 /etc/container_environment.sh  

