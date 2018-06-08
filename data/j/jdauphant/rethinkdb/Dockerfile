FROM rethinkdb  
  
MAINTAINER Julien DAUPHANT  
  
RUN apt-get update && \  
apt-get install -y python2.7 python-pip && \  
pip install rethinkdb && \  
apt-get purge -y python-pip && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

