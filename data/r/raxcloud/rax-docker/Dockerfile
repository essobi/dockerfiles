# DOCKER-VERSION 0.11.1  
FROM ubuntu:12.04  
MAINTAINER John Yi "john.yi@rackspace.com"  
RUN apt-get -y update  
RUN apt-get -y install curl build-essential libxml2-dev libxslt-dev git
zlib1g-dev libssl-dev  
RUN apt-get -y install python openssh-server python-dev software-properties-
common net-tools vim  
RUN curl
https://pypi.python.org/packages/source/s/setuptools/setuptools-1.1.6.tar.gz |
tar xvzf -;cd setuptools-1.1.6;python setup.py install  
RUN easy_install pip  
RUN pip install python-novaclient python-swiftclient python-heatclient python-
cinderclient python-keystoneclient python-troveclient python-neutronclient  
RUN pip install pyrax ansible supernova ipython  
RUN git clone https://github.com/rackerlabs/python-cloudlb.git
$HOME/cloudlb;cd $HOME/cloudlb;python setup.py install;cd $HOME  
RUN git clone https://github.com/jyidiego/clb.git $HOME/clb;cd
$HOME/clb;python setup.py install;cd $HOME  
RUN chmod -R 544 /usr/local/lib/python2.7/dist-
packages/python_dateutil-*-py2.7.egg/EGG-INFO/* # needed because perms are
screwed.  
ADD . /code  
RUN cp /code/motd.tail /etc  
RUN rm /code/motd.tail  
RUN cd /code;git clone https://github.com/jyidiego/rax_examples.git  
RUN cd /code;git clone https://github.com/heat-ci/heat-templates.git  
RUN mkdir /root/.ssh  
CMD bash  

