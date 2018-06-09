FROM debian:wheezy  
MAINTAINER Paddy Carey <patrick@rehabstudio.com>  
  
# install apt dependencies  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
apt-transport-https \  
build-essential \  
libxslt1-dev \  
python-imaging \  
python-numpy \  
python-dev \  
python-pip \  
sudo && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# install all the packages we need from pypi  
ADD ops/assets/requirements.txt /tmp/requirements.txt  
RUN pip install -r /tmp/requirements.txt  
  
# add remote shell script to allow python shell access to running instance  
ADD ops/scripts/remote_shell.py /usr/local/bin/remote_shell.py  
  
# add custom motd to remind users of how persistance works  
ADD ops/assets/motd /etc/motd  
  
# Download and install the Appengine Python SDK  
ADD ops/scripts/gaesdk_download.py /tmp/gaesdk_download.py  
RUN /tmp/gaesdk_download.py 1.9.50 && \  
rm -rf /tmp/*  
ENV PATH /opt/google_appengine:$PATH  
  
# Add volumes for pesistence between runs  
VOLUME ["/.ipython", "/home/aeuser"]  
  
# create a non-root user we can use to run the application inside the
container  
RUN groupadd -r aeuser -g 1000 && \  
useradd -u 1000 -rg aeuser -md /home/aeuser -s /bin/bash aeuser  
  
# ensure aeuser owns volumes  
RUN mkdir -p /.ipython && \  
chown -R aeuser:aeuser /.ipython && \  
chown -R aeuser:aeuser /home/aeuser  
  
# add .bashrc for aeuser  
ADD ops/assets/bashrc /home/aeuser/.bashrc  
  
# add sudo config to enable root access for aeuser  
ADD ops/assets/sudoers /etc/sudoers.d/aeuser  
  
# switch to the new user account so that all commands run as `aeuser`  
ENV HOME /home/aeuser  
USER aeuser  
  
# default run command  
CMD bash  
  
# expose ports (application server & admin server)  
EXPOSE 8000 8080  

