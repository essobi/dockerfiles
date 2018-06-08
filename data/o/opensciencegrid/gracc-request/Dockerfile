  
FROM opensciencegrid/osg-wn:3.4-el7  
  
  
RUN curl -o /etc/yum.repos.d/djw8605-GRACC-epel-7.repo
https://copr.fedorainfracloud.org/coprs/djw8605/GRACC/repo/epel-7/djw8605-GRACC-
epel-7.repo  
  
RUN yum -y install python-setuptools python2-pika python-elasticsearch-dsl
python-dateutil python-toml python-filelock  
  
ADD . /gracc-request  
WORKDIR /gracc-request  
RUN python setup.py install  
  
RUN install -d -m 0755 /etc/graccreq/config.d/ && install -m 0744
config/gracc-request.toml /etc/graccreq/config.d/gracc-request.toml  
  
CMD /usr/bin/graccreq  
  

