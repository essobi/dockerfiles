FROM nlesc/xenon-slurm-fixture  
  
# become root user  
USER root  
  
# install SSH client  
RUN apt-get update && apt-get install -y openssh-server  
  
# When this image is used as ssh client then ignore the known hosts  
RUN echo "StrictHostKeyChecking no" >> /etc/ssh/ssh_config  
  
# Don't hash the entries in /home/xenon/.ssh/known_hosts  
RUN echo "HashKnownHosts no" >> /etc/ssh/ssh_config  
  
# Expose the OpenSSH server on port 22  
EXPOSE 22  
# change into user xenon's home directory  
WORKDIR /home/xenon/  
  
# Add the ssh configuration from the Docker context to inside the Docker
container  
ADD .ssh .ssh  
  
# SSH has strict requirements on the permissions of its configuration files,
set them here  
RUN chmod 700 .ssh && \  
chmod 600 .ssh/id_rsa .ssh/id_dsa && \  
chmod 644 .ssh/authorized_keys .ssh/id_rsa.pub .ssh/id_dsa.pub && \  
chown -R xenon:xenon .ssh  
  
# define the test that tells us if the docker container is healthy  
HEALTHCHECK \--interval=1s CMD ssh -i /home/xenon/.ssh/id_rsa xenon@localhost
/bin/true || exit 1  
  

