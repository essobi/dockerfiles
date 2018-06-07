# Dockerfile for PyPy  
FROM buildpack-deps:jessie-scm  
MAINTAINER Jeethu Rao <jeethu@jeethurao.com>  
  
ENV LANG C.UTF-8  
  
RUN set -e; \  
umask 0022; \  
apt-get update; apt-get install bzip2; \  
wget -q https://bitbucket.org/squeaky/portable-
pypy/downloads/pypy-5.0.1-linux_x86_64-portable.tar.bz2 -P /tmp/; \  
tar -xjf /tmp/pypy-5.0.1-linux_x86_64-portable.tar.bz2 -C /usr/local; \  
ln -s /usr/local/pypy-5.0.1-linux_x86_64-portable/bin/libpypy-c.so
/usr/lib/x86_64-linux-gnu/; \  
ldconfig; \  
wget -qO- 'https://bootstrap.pypa.io/get-pip.py' |
/usr/local/pypy-5.0.1-linux_x86_64-portable/bin/pypy; \  
/usr/local/pypy-5.0.1-linux_x86_64-portable/bin/pip install virtualenv; \  
ln -s /usr/local/pypy-5.0.1-linux_x86_64-portable/bin/* /usr/local/bin/; \  
rm /tmp/pypy-5.0.1-linux_x86_64-portable.tar.bz2; \  
apt-get purge -yq wget; \  
apt-get -yq autoremove; \  
apt-get clean;  
  
CMD ["pypy"]  

