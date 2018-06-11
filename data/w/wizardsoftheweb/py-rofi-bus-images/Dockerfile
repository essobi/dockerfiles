FROM fedora:28  
# https://github.com/pygobject/pygobject-travis-ci-docker-
examples/blob/master/Dockerfile.fedora25.py2  
ENV LANG C.utf8  
  
RUN dnf -y install \  
dbus{,-x11} \  
gtk3 \  
pyflakes \  
pygobject3 \  
python2-pytest \  
python-gobject \  
python-pep8 \  
python-setuptools \  
which \  
xorg-x11-server-Xvfb  
  
RUN dbus-uuidgen --ensure  
  
RUN pip install coveralls  

