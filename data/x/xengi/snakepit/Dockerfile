FROM fedora:latest  
  
LABEL de.xengi.snakepit.version="1.0.0" vendor="XenGi" de.xengi.release-
date="2018-03-10"  
  
RUN dnf install -y \  
micropython \  
pypy \  
pypy3 \  
jython \  
python26 \  
python27 \  
python33 \  
python34 \  
python35 \  
python36 \  
python37 \  
python-virtualenv \  
python3-virtualenv \  
tox \  
&& dnf autoremove -y \  
&& dnf clean all -y  
  
COPY . /code  
  
WORKDIR /code  
  
CMD ["/bin/bash"]  

