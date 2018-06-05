# Dockerfile for krakenceph  
#  
# run this handing it a directory with a ceph.conf file and keys that are
needed:  
#  
# docker run --name krakenceph -d -v $target_dir:/etc/ceph -p 9091:9091
automatikdonn/krakenceph /bin/sh -c /app/contrib/startall.sh  
#  
# Find out more about docker here: www.docker.com  
FROM fedora:latest  
  
MAINTAINER donny@fortnebula.com  
  
  
RUN dnf -y install python-pip git ceph python-lxml libxml2-devel libxslt-devel
python-libxml2  
  
ADD . /app  
RUN cd /app/ && pip install -r requirements.txt  
  
VOLUME /etc/ceph  
EXPOSE 9091  
CMD /app/contrib/startall.sh  

