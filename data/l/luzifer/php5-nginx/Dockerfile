FROM ubuntu:14.04  
MAINTAINER Knut Ahlers  
  
RUN \  
apt-get -y update && \  
apt-get install -y ansible python-apt  
  
ADD . /tmp/ansible  
  
RUN \  
cd /tmp/ansible && \  
ansible-playbook playbook.yml -c local -i /tmp/ansible/inventory && \  
apt-get purge -y ansible python-apt && \  
apt-get autoremove -y && \  
echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \  
cd / && rm -rf /tmp/ansible && \  
rm -rf /var/lib/apt/lists/*  
  
EXPOSE 80  
CMD ["/usr/local/bin/container-run.sh"]  

