FROM centos:centos6  
RUN rpm -ivh http://download.fedoraproject.org/pub/epel/6/i386/epel-
release-6-8.noarch.rpm  
RUN yum -y install python-pip git python-devel curl gcc gcc-c++ wget xz tar
zlib-devel zlib openssl-devel  
  
# install python  
RUN cd /tmp; wget http://python.org/ftp/python/2.7.6/Python-2.7.6.tar.xz  
RUN cd /tmp; xz -d Python-2.7.6.tar.xz; tar -xf Python-2.7.6.tar  
RUN cd /tmp/Python-2.7.6; ./configure --prefix=/usr/local \--enable-
unicode=ucs4 --enable-shared LDFLAGS="-Wl,-rpath /usr/local/lib"; make && make
altinstall  
  
RUN cd /tmp; wget https://bootstrap.pypa.io/ez_setup.py  
RUN cd /tmp; python2.7 ez_setup.py; easy_install-2.7 pip  
  
RUN cd /tmp; git clone https://github.com/ethereum/pyethereum.git  
RUN cd /tmp/pyethereum; pip2.7 install -r requirements.txt;  
RUN cd /tmp; git clone https://github.com/bjornedstrom/python-sha3.git; cd
/tmp/python-sha3; python2.7 setup.py install  

