FROM shipito/dind:latest  
MAINTAINER Patrik Votocek <patrik@votocek.cz>  
  
RUN apt-get update -yqq && \  
apt-get upgrade -yqq && \  
apt-get install curl git -yqq && \  
curl -L https://www.opscode.com/chef/install.sh | sudo bash -s -- -P chefdk &&
\  
locale-gen en_US.UTF-8 && \  
apt-get clean -yqq && \  
apt-get autoremove -yqq && \  
chef gem install kitchen-docker  

