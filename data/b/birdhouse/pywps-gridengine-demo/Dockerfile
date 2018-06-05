# vim:set ft=dockerfile:  
FROM birdhouse/emu  
MAINTAINER Birdhouse <wps@dkrz.de>  
  
LABEL Description="pywps gridengine demo" Vendor="Birdhouse" Version="0.1.3"  
  
# Add jessie backports repo for gridengine packages  
RUN echo "deb http://httpredir.debian.org/debian jessie-backports main contrib
non-free" >> /etc/apt/sources.list  
RUN apt-get update  
  
# install ansible  
RUN conda install -y -c conda-forge ansible  
  
# get ansible playbooks  
RUN git clone https://github.com/bird-house/birdhouse-ansible.git /opt/ansible  
  
# install gridengine master  
WORKDIR /opt/ansible/gridengine  
RUN ansible-playbook \  
-e sge_server_name=gridengine \  
-e sge_type_of_node=client \  
playbooks/gridengine.yml  
  
# config  
ENV SGE_ROOT /var/lib/gridengine  
  
# Install conda packages for scheduler extension  
RUN conda install -y -n emu -c birdhouse -c conda-forge psycopg2 drmaa dill  
  
# add wps user  
RUN useradd -d /home/wps -m --uid 1000 wps  
  
# update emu wps config  
ADD custom.cfg /opt/birdhouse/src/emu/custom.cfg  
  
# copy start script  
COPY start-services.sh /etc/start-services.sh  
  
# go to emu source  
WORKDIR /opt/birdhouse/src/emu  
  
# Start service ...  
ENTRYPOINT ["/etc/start-services.sh"]  

