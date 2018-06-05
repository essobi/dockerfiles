FROM python:2.7  
MAINTAINER Greg Orzell <devops@keen.io>  
  
RUN apt-get update &&\  
apt-get install --no-install-recommends -y apt-transport-https ca-certificates
curl gnupg2 software-properties-common make &&\  
curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add \- &&\  
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian
$(lsb_release -cs) stable" &&\  
curl -sL https://deb.nodesource.com/setup_7.x | bash - &&\  
apt-get update &&\  
apt-get install --no-install-recommends -y docker-ce python-pip nodejs &&\  
pip install docker-compose &&\  
apt-get clean && \  
rm -rf /var/lib/apt/lists  
  
CMD ["/bin/bash"]  
  

