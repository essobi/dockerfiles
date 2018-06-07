# Dockerfile to build a condor with a personal installatin of HTCondor  
# Better than ubuntu  
FROM phusion/baseimage:0.9.18  
# set HOME as it is missing from the base image  
ENV HOME /root  
  
# regenerate host ssh keys  
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
# install required software  
ARG DEBIAN_FRONTEND=noninteractive  
RUN apt-get update -y \  
&& apt-get install -y htcondor man \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# add files to container from local directory  
COPY docker_condor_init.sh /etc/my_init.d/01_docker_condor_init.sh  
COPY condor_config.local /etc/condor/condor_config.local  
  
# install Condor user with password-less sudo access  
RUN useradd -r -m -U -G sudo -d /home/condoradmin -s /bin/bash -c "Docker
Condor Admin" condoradmin \  
&& echo "condoradmin ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
  
# start my_init on execution and pass bash to runit  
ENTRYPOINT ["/sbin/my_init", "--"]  
CMD ["/bin/login", "-f", "condoradmin"]  

