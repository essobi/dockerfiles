# This is the container acting as Command Center  
# playbooks and tests are run from it  
FROM tuxpiper/ansible-testinfra-docker:ubuntu-trusty  
  
ENV ANSIBLE_VERSION 2.1.2.0  
ENV TESTINFRA_VERSION 1.4.2  
  
RUN apt-get update && \  
apt-get install -y python-dev python-pip git libffi6 libffi-dev libssl1.0.0
libssl-dev && \  
pip install ansible==${ANSIBLE_VERSION} && \  
pip install testinfra==${TESTINFRA_VERSION} && \  
apt-get remove -y python-dev libffi-dev libssl-dev && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD setup_inventory.sh
/boot.d/scripts/010_ansible_inventory/setup_inventory.sh  

