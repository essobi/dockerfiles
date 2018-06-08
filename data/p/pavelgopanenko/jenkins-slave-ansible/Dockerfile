FROM csanchez/jenkins-swarm-slave:1.22  
  
MAINTAINER Pavel Gopanenko <pgopanenko@gmail.com>  
  
USER root  
  
RUN apt-get update && \  
apt-get install -q -y --force-yes git python-dev python-pip && \  
pip install ansible && \  
apt-get autoremove -q -y --force-yes && \  
rm -rf /var/lib/apt/lists/*  

