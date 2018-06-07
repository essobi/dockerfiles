FROM ubuntu  
MAINTAINER Ilya Fourmanov <ilya.fourmanov@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y -q curl git docker.io && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
apt-get clean  
  
RUN locale-gen en_US.UTF-8  
  
RUN curl -L https://www.opscode.com/chef/install.sh | sudo bash -s -- -P
chefdk  
  
RUN chef gem install kitchen-ec2 -n /opt/chefdk/bin/ && \  
chef gem install kitchen-azure -n /opt/chefdk/bin/ && \  
chef gem install kitchen-docker -v 2.0.0 -n /opt/chefdk/bin/ && \  
chef gem install kitchen-nodes -n /opt/chefdk/bin/  
  
WORKDIR /kitchen  

