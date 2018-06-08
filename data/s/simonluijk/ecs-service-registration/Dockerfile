FROM debian:jessie  
MAINTAINER simon@simonluijk.com  
  
RUN echo 'DPkg::Post-Invoke {"/bin/rm -f /var/cache/apt/archives/*.deb ||
true";};' | tee /etc/apt/apt.conf.d/no-cache && \  
apt-get update -y && \  
apt-get dist-upgrade -y && \  
apt-get clean && \  
rm -rf /var/cache/apt/* && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y git python-pip  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y wget && \  
wget http://ftp.us.debian.org/debian/pool/main/p/python-urllib3/python-
urllib3_1.11-1_all.deb && \  
dpkg -i python-urllib3_1.11-1_all.deb && \  
rm python-urllib3_1.11-1_all.deb && \  
wget http://ftp.us.debian.org/debian/pool/main/r/requests/python-
requests_2.7.0-3_all.deb && \  
dpkg -i python-requests_2.7.0-3_all.deb && \  
rm python-requests_2.7.0-3_all.deb && \  
pip install git+https://github.com/simonluijk/aws-ecs-service-
discovery.git#egg=ecs_discovery && \  
pip install Jinja2 simplejson && \  
pip install git+https://github.com/simonluijk/PythonEtcdClient.git#egg=etcd
requests==2.7.0  
  
CMD ["bash"]  

