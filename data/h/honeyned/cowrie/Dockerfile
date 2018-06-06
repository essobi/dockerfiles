############################################################  
# Dockerfile to build Cowrie SSH honeypot  
# Based on Ubuntu  
# Partly based on micheloosterhof/docker-cowrie  
############################################################  
  
# Set the base image to Ubuntu  
FROM ubuntu:xenial  
  
# File Author / Maintainer  
LABEL "maintainer"="HoneyNED" \  
"version"="1.0"  
  
# Update the repository sources list and install prerequisites  
RUN apt-get --quiet update && \  
apt-get install --assume-yes \  
git \  
python-virtualenv \  
python-setuptools \  
libmpfr-dev \  
libssl-dev \  
libmpc-dev \  
libffi-dev \  
build-essential \  
libpython-dev \  
python2.7-minimal \  
authbind \  
python-pip \  
python-twisted  
  
# Add new non-root user  
RUN groupadd -r cowrie && \  
useradd --system \  
\--gid cowrie \  
\--create-home \  
\--shell /sbin/nologin cowrie && \  
mkdir -p /opt/cowrie  
  
RUN chown -R cowrie:cowrie /opt/cowrie  
  
# Switch to cowrie user  
USER cowrie  
WORKDIR /opt/cowrie  
  
# Download the code from GitHub  
RUN git clone http://github.com/honeyned/cowrie /opt/cowrie  
  
# Setup Virtual Environment  
RUN virtualenv cowrie-env  
RUN /bin/bash -c "source cowrie-env/bin/activate"  
RUN pip install -r requirements.txt  
RUN exit  
  
# Export the python path for running cowrie  
RUN export PYTHONPATH=/opt/cowrie  
  
USER cowrie  
WORKDIR /opt/cowrie  
  
# This is used by the Splunk forwarder  
RUN touch /opt/cowrie/log/cowrie.json  
  
VOLUME ["/opt/cowrie/etc/", "/opt/cowrie/dl/", "/opt/cowrie/log/"]  
  
##################### INSTALLATION END #####################  
  
# Open the port and start cowrie  
EXPOSE 2222 2223  
  
ENTRYPOINT ["/opt/cowrie/bin/cowrie", "start"]  

