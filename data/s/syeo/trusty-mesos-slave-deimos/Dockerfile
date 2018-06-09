FROM syeo/trusty-mesos  
MAINTAINER Stanley Yeo <yyoud88@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y python python-setuptools docker.io && \  
easy_install pip && \  
pip install deimos && \  
mkdir -p /etc/mesos-slave && \  
echo /usr/local/bin/deimos | tee /etc/mesos-slave/containerizer_path && \  
echo external | tee /etc/mesos-slave/isolation  
  
EXPOSE 5051  
CMD ["mesos-slave"]  

