FROM ubuntu:14.04.3  
# Last build date - this can be updated whenever there are security updates so  
# that everything is rebuilt  
ENV security_updates_as_of 2016-03-23  
# Install security updates and required packages  
RUN apt-get -qy update && \  
apt-get -qy upgrade && \  
apt-get -qy install python-pip && \  
apt-get -qy install python-dev && \  
apt-get -qy install libyaml-dev && \  
apt-get -qy install libffi-dev && \  
apt-get -qy install libssl-dev && \  
apt-get -qy install python-virtualenv  
  
RUN virtualenv /app/  
  
# It is really very slow to re-install the Python dependencies every time.  
# TODO: Fix this Dockerfile so we don't have to duplicate the dependencies
here  
# but so that we also can cache them in an intermediate image.  
RUN /app/bin/pip install --upgrade setuptools  
  
RUN /app/bin/pip install \  
'PyYAML>=3' \  
'Twisted>=14' \  
'treq>=14' \  
'pyasn1>=0.1' \  
'docker-py>=1.5.0' \  
'pyrsistent>=0.11.9' \  
'eliot>=0.9.0'  
  
ADD . /source  
WORKDIR /source  
  
# Install requirements from the project's setup.py  
RUN /app/bin/pip install .  
  
WORKDIR /app  
ENV PATH "$PATH:/app/bin"  

