#  
# Python versions on CentOS 6  
#  
# Markus Juenemann, 26-Nov-2015  
FROM centos:6  
MAINTAINER Markus Juenemann <markus@juenemann.net>  
  
# Yum proxy  
#  
RUN [ "$http_proxy" == "" ] || echo "proxy=$http_proxy" >> /etc/yum.conf  
RUN yum clean all  
  
# Update  
#  
RUN [ -f /etc/yum.repos.d/epel.repo ] || yum -y -v install
https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm  
RUN [ -f /etc/yum.repos.d/repoforge ] || yum -y -v install
http://pkgs.repoforge.org/rpmforge-release/rpmforge-
release-0.5.3-1.el6.rf.x86_64.rpm  
RUN yum -y update  
  
# Install requirements  
#  
RUN yum -y install sqlite-devel \  
gdbm-devel \  
zlib-devel \  
ncurses-devel \  
openssl-devel \  
readline-devel \  
bzip2-devel \  
libxslt-devel \  
python-devel \  
libxml2-devel \  
gcc \  
make \  
file \  
which \  
sudo \  
tar \  
wget \  
git \  
gitflow \  
subversion \  
mercurial \  
vim-enhanced \  
rpm-build  
  
# Pypy and Jython  
#  
RUN yum -y install pypy jython  
  
# Download get-pip.py  
#  
RUN wget --no-check-certificate https://bootstrap.pypa.io/get-pip.py  
  
# Python 2.6.9  
#  
RUN wget https://www.python.org/ftp/python/2.6.9/Python-2.6.9.tgz && \  
tar xvfz Python-2.6.9.tgz && \  
cd Python-2.6.9 && \  
./configure && \  
make clean && \  
make && \  
make altinstall && \  
cd \- && \  
/usr/local/bin/python2.6 get-pip.py && \  
pip2.6 install tox setuptools nose coverage minimock instrumental && \  
pip2.6 install --upgrade pip && \  
rm -rfv Python* \  
rm -fv `find /usr/local/lib -name "*.pyc"` && \  
rm -fv `find /usr/local/lib -name "*.pyo"`  
  
# Python 2.7.11  
#  
RUN wget https://www.python.org/ftp/python/2.7.11/Python-2.7.11.tgz && \  
tar xvfz Python-2.7.11.tgz && \  
cd Python-2.7.11 && \  
./configure && \  
make clean && \  
make && \  
make altinstall && \  
cd \- && \  
/usr/local/bin/python2.7 get-pip.py && \  
pip2.7 install tox setuptools nose coverage minimock instrumental && \  
pip2.7 install --upgrade pip && \  
rm -rfv Python-* \  
rm -fv `find /usr/local/lib -name "*.pyc"` && \  
rm -fv `find /usr/local/lib -name "*.pyo"`  
  
## Python 3.2.6  
##  
RUN wget https://www.python.org/ftp/python/3.2.6/Python-3.2.6.tgz && \  
tar xvfz Python-3.2.6.tgz && \  
cd Python-3.2.6 && \  
./configure && \  
make clean && \  
make && \  
make altinstall && \  
cd \- && \  
#/usr/local/bin/python3.2 get-pip.py && \  
#pip3.2 install setuptools && \  
rm -rfv Python-* \  
rm -fv `find /usr/local/lib -name "*.pyc"` && \  
rm -fv `find /usr/local/lib -name "*.pyo"`  
  
# Python 3.3.6  
#  
RUN wget https://www.python.org/ftp/python/3.3.6/Python-3.3.6.tgz && \  
tar xvfz Python-3.3.6.tgz && \  
cd Python-3.3.6 && \  
./configure && \  
make clean && \  
make && \  
make altinstall && \  
cd \- && \  
/usr/local/bin/python3.3 get-pip.py && \  
pip3.3 install tox setuptools nose coverage minimock instrumental && \  
pip3.3 install --upgrade pip && \  
rm -rfv Python-* \  
rm -fv `find /usr/local/lib -name "*.pyc"` && \  
rm -fv `find /usr/local/lib -name "*.pyo"`  
  
# Python 3.4.4  
#  
RUN wget https://www.python.org/ftp/python/3.4.4/Python-3.4.4.tgz && \  
tar xvfz Python-3.4.4.tgz && \  
cd Python-3.4.4 && \  
./configure && \  
make clean && \  
make && \  
make altinstall && \  
cd \- && \  
/usr/local/bin/python3.4 get-pip.py && \  
cp /usr/local/bin/pip3 /usr/local/bin/pip3.4 && \  
pip3.4 install tox setuptools nose coverage minimock instrumental && \  
pip3.4 install --upgrade pip && \  
rm -rfv Python-* \  
rm -fv `find /usr/local/lib -name "*.pyc"` && \  
rm -fv `find /usr/local/lib -name "*.pyo"`  
  
# Python 3.5.1  
#  
RUN wget https://www.python.org/ftp/python/3.5.1/Python-3.5.1.tgz && \  
tar xvfz Python-3.5.1.tgz && \  
cd Python-3.5.1 && \  
./configure && \  
make clean && \  
make && \  
make altinstall && \  
cd \- && \  
/usr/local/bin/python3.5 get-pip.py && \  
pip3.5 install tox setuptools nose coverage minimock instrumental && \  
pip3.5 install --upgrade pip && \  
rm -rfv Python-* \  
rm -fv `find /usr/local/lib -name "*.pyc"` && \  
rm -fv `find /usr/local/lib -name "*.pyo"`  
  
# Undo yum proxy  
#  
RUN [ "$http_proxy" == "" ] || sed --in-place 's/^proxy=http.*$//g'
/etc/yum.conf  
  
RUN useradd developer  
USER developer  
ENV HOME /home/developer  
WORKDIR /home/developer  
CMD /bin/bash  
  
# Fix pip3.4  
#  
COPY pip3.4 /usr/local/bin/pip3.4  

