# DOCKER-VERSION 0.7.2  
FROM ubuntu:12.10  
MAINTAINER John Yi "john.yi@rackspace.com"  
RUN apt-get -y update  
RUN apt-get -y install curl build-essential libxml2-dev libxslt-dev git
zlib1g-dev libssl-dev python openssh-server python-dev software-properties-
common gcc python-dev  
RUN curl
https://pypi.python.org/packages/source/s/setuptools/setuptools-1.1.6.tar.gz |
(cd /root;tar xvzf -;cd setuptools-1.1.6;python setup.py install)  
RUN easy_install pip  
RUN pip install python-novaclient python-swiftclient python-heatclient python-
cinderclient python-keystoneclient pyrax ansible python-glanceclient python-
troveclient python-neutronclient supernova paramiko  
# Setting the $HOME variable here  
ENV HOME /root  
# Uses raxcloud queues  
# run producer with: docker run -d raxcloud/raxcloud-queue-demo producer -u
<username> -k <apikey>  
# run consumer with: docker run -d raxcloud/raxcloud-queue-demo consumer -u
<username> -k <apikey>  
# run autoscale with: docker run -d raxcloud/raxcloud-queue-demo monitor -u
<username> -k <apikey>  
ADD ./queue_demo.py $HOME/  
ENTRYPOINT [ "/root/queue_demo.py" ]  

