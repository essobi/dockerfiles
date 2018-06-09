FROM opensciencegrid/osg-wn:3.3-el7  
  
  
RUN curl -o /etc/yum.repos.d/djw8605-GRACC-epel-7.repo
https://copr.fedorainfracloud.org/coprs/djw8605/GRACC/repo/epel-7/djw8605-GRACC-
epel-7.repo  
  
RUN yum -y install python-setuptools python2-pika python-dateutil python-toml
python-filelock gracc-request  
  
ADD . /gracc-summary  
WORKDIR /gracc-summary  
RUN python setup.py install  
  
RUN install -d -m 0755 /etc/graccsum/config.d/ && install -m 0744
config/gracc-summary.toml /etc/graccsum/config.d/gracc-summary.toml  
  
  
CMD /usr/bin/graccsumperiodic -c /etc/graccsum/config.d/gracc-summary.toml  

