FROM fedora:20  
MAINTAINER Pulp QE <pulp-list@redhat.com>  
  
# install deps  
RUN yum update -y && yum install -y python-ecdsa python-devel python-nose
m2crypto gcc file dnf python-pip PyYAML python-qpid python-requests python-
plumbum python-paramiko python-rpyc && yum clean all  
  
# these deps aren't available in Fedora at the correct version, or at all  
RUN pip install gevent  
RUN pip install stitches  
RUN pip install requestbin  
  
# add source  
ADD pulp_auto /src/pulp_auto  
ADD tests /src/tests  
ADD setup.py /src/setup.py  
  
# install!  
RUN pip install --no-index /src/  
  
# stuff that will configure and run the tests  
ADD docker/inventory-example.yml /src/inventory-example.yml  
ADD docker/geninventory.py /usr/local/bin/geninventory  
CMD cd /src/ && geninventory && nosetests -vs tests/general_tests/  

