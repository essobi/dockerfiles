FROM quay.io/loganv/docker-ci:ubuntu-xenial  
  
USER root  
  
RUN apt-get update && \  
apt-get install -y s3cmd && rm -rf /var/lib/apt/lists/*  
  
USER ubuntu  
  
RUN virtualenv ~/.openstack && \  
echo 'source ~/.local_profile' >> ~/.profile && \  
~/.openstack/bin/pip install python-openstackclient  
  
COPY limestone-openrc /home/ubuntu  
COPY buildvm /home/ubuntu/.buildvm  
COPY profile /home/ubuntu/.local_profile  
COPY s3cmd.cfg /home/ubuntu/.s3cfg  
CMD bash -l  

