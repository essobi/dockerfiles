FROM debian:jessie  
  
MAINTAINER Fábio Uechi <fabio.uechi@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y wget curl python  
  
RUN set -x \  
&& curl -SL 'https://bootstrap.pypa.io/get-pip.py' | python2 \  
&& pip install --no-cache-dir virtualenv  
  
RUN wget http://download.ag-projects.com/agp-debian-gpg.key -P /tmp/ && \  
apt-key add /tmp/agp-debian-gpg.key && \  
echo "deb http://ag-projects.com/debian stable main" | tee -a
/etc/apt/sources.list.d/ag-projects.list  
  
RUN apt-get update && \  
apt-get install -y python-sipsimple sipclients  
  
CMD ["/bin/bash"]

