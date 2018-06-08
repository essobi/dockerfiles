FROM nyasara/docker-managementbase  
  
# Update  
# Install pip  
RUN apt-get update \  
&& apt-get install -y python-pip \  
# Install deps for backports.lmza (python2 requires it)  
python-dev liblzma-dev libevent1-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
# Pull and setup registry  
RUN git clone https://github.com/docker/docker-registry.git \  
&& cp docker-registry/config/boto.cfg /etc/boto.cfg \  
&& pip install /docker-registry/depends/docker-registry-core \  
# Install registry  
&& pip install file:///docker-registry#egg=docker-
registry[bugsnag,newrelic,cors] \  
&& pip install docker-registry-driver-azureblob \  
&& patch \  
$(python -c 'import boto; import os; print
os.path.dirname(boto.__file__)')/connection.py \  
< /docker-registry/contrib/boto_header_patch.diff  
  
#Volumes for logs and config data  
VOLUME /docker-registry/config  
VOLUME /var/log/registry  
  
# Environment variables to run registry  
ENV DOCKER_REGISTRY_CONFIG /docker-registry/config/registry-config.yml  
ENV SETTINGS_FLAVOR prod  
  
EXPOSE 5000  
# Copy the registry template config  
COPY registry-config.toml /etc/confd/conf.d/  
# Copy the run script  
COPY run-registry.sh /docker-registry/run-registry.sh  
# Copy the registry template  
COPY config.tmpl /etc/confd/templates/  
  
# Make the run script executable  
RUN chmod +x /docker-registry/run-registry.sh  
  
CMD ["/bin/bash", "/docker-registry/run-registry.sh"]  

