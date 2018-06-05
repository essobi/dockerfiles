FROM continuumio/miniconda  
MAINTAINER Birdhouse <wps@dkrz.de>  
LABEL Description="gridengine" Vendor="Birdhouse" Version="0.2.1"  
  
# Add jessie backports repo for gridengine packages  
RUN echo "deb http://httpredir.debian.org/debian jessie-backports main contrib
non-free" >> /etc/apt/sources.list  
  
#ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update  
  
# install ansible  
RUN conda install -y -c conda-forge ansible  
  
# get ansible playbooks  
RUN git clone https://github.com/bird-house/birdhouse-ansible.git /opt/ansible  
  
# install gridengine master  
WORKDIR /opt/ansible/gridengine  
RUN ansible-playbook \  
-e sge_server_name=gridengine \  
-e sge_type_of_node=front \  
-e sge_submission_node=wps \  
playbooks/gridengine.yml  
  
# install gridengine worker  
RUN ansible-playbook \  
-e sge_server_name=gridengine \  
-e sge_type_of_node=worker \  
playbooks/gridengine.yml  
  
# config  
ENV SGE_ROOT /var/lib/gridengine  
  
# copy start script  
ADD start-services.sh /etc/start-services.sh  
RUN chmod +x /etc/start-services.sh  
  
# Expose sge qmaster  
EXPOSE 6444  
# Expose sge execd  
EXPOSE 6445  
# Start service ...  
ENTRYPOINT ["/etc/start-services.sh"]  
CMD ["gridengine-master", "gridengine-exec"]  

