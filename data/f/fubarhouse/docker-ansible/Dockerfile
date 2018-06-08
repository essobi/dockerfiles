FROM geerlingguy/docker-ubuntu1404-ansible  
MAINTAINER Karl Hepworth  
  
# Add a PPA for Python  
RUN add-apt-repository ppa:fkrull/deadsnakes-python2.7  
  
# Install our dependencies  
RUN apt-get update && \  
apt-get install -y \  
wget gcc make python-pip  
  
RUN apt-get install --force-yes --yes python2.7  
  
RUN pip install -i https://pypi.python.org/simple/ --upgrade pip  
  
# Install Ansible  
RUN apt-get remove -y ansible  
RUN pip install urllib3 pyOpenSSL ndg-httpsclient pyasn1 cryptography  
# RUN pip install virtualenv virtualenvwrapper  
RUN pip install ansible  
  
# General cleanup.  
RUN rm -rf /var/lib/apt/lists/* \  
&& rm -Rf /usr/share/doc && rm -Rf /usr/share/man \  
&& apt-get clean  
  
# Verify important installations with stdout.  
RUN python --version  
RUN ansible --version

