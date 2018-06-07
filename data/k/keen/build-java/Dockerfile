FROM openjdk:8  
MAINTAINER Greg Orzell <devops@keen.io>  
  
RUN apt-get update &&\  
apt-get install --no-install-recommends -y apt-transport-https ca-certificates
curl gnupg2 software-properties-common make &&\  
curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add \- &&\  
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian
$(lsb_release -cs) stable" &&\  
apt-get update &&\  
apt-get install --no-install-recommends -y docker-ce python-setuptools python-
pip &&\  
pip install docker-compose &&\  
apt-get autoremove -y python-pip &&\  
apt-get clean && \  
rm -rf /var/lib/apt/lists  
  
CMD ["/bin/bash"]  

