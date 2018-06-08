# Zato  
FROM ubuntu:14.04  
MAINTAINER Rafał Krysiak <rafal@zato.io>  
  
# Install helper programs used during Zato installation  
RUN apt-get update && apt-get install -y \  
apt-transport-https \  
python-software-properties \  
software-properties-common \  
libcurl4-openssl-dev \  
curl \  
redis-server \  
ssh \  
supervisor  
  
# Add the package signing key  
RUN curl -s https://zato.io/repo/zato-0CBD7F72.pgp.asc | sudo apt-key add -  
  
# Add Zato repo to your apt  
# update sources and install Zato  
RUN apt-add-repository https://zato.io/repo/stable/2.0/ubuntu  
RUN apt-get update && apt-get install -y zato  
  
# Setup supervisor  
RUN mkdir -p /var/log/supervisor  
  
# Setup sshd  
RUN mkdir /var/run/sshd/  
  
# Create work environment for Zato 2.0.7  
# Switch to zato user and create Zato environment  
USER zato  
  
EXPOSE 22 6379 8183 17010 17011 11223  
# Get additional config files and starter scripts  
WORKDIR /opt/zato  
RUN wget -P /opt/zato -i https://raw.githubusercontent.com/zatosource/zato-
build/master/docker/quickstart-dh/filelist  
RUN chmod 755 /opt/zato/zato_start_load_balancer \  
/opt/zato/zato_start_server1 \  
/opt/zato/zato_start_server2 \  
/opt/zato/zato_start_web_admin \  
/opt/zato/generate_password_zato_user.sh \  
/opt/zato/generate_password_web_admin.sh \  
/opt/zato/create_quickstart.sh \  
/opt/zato/start.sh  
  
USER root  

