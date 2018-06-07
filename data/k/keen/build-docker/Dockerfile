FROM ubuntu:17.04  
MAINTAINER Greg Orzell <devops@keen.io>  
  
RUN apt-get update &&\  
apt-get install --no-install-recommends -y apt-transport-https ca-certificates
curl software-properties-common make &&\  
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add \- &&\  
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu
$(lsb_release -cs) stable" &&\  
apt-get update &&\  
apt-get install --no-install-recommends -y docker-ce python python-dev python-
setuptools python-pip &&\  
pip install docker-compose &&\  
apt-get autoremove -y python-pip apt-transport-https &&\  
apt-get clean && \  
rm -rf /var/lib/apt/lists  
  
CMD ["/bin/bash"]  

