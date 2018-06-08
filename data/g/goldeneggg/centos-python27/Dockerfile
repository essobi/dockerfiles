# using centos 6  
FROM goldeneggg/centos  
  
MAINTAINER goldeneggg  
  
RUN yum -y groupinstall "Development tools"  
RUN yum -y install wget zlib-devel bzip2-devel openssl-devel ncurses-devel
sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-
devel  
  
WORKDIR /root  
RUN wget https://www.python.org/ftp/python/2.7.8/Python-2.7.8.tar.xz  
RUN tar xf Python-2.7.8.tar.xz  
  
WORKDIR /root/Python-2.7.8  
ADD ADD_FILES/etc/ld.so.conf /etc/ld.so.conf  
RUN ./configure --prefix=/usr/local \--enable-unicode=ucs4 --enable-shared
LDFLAGS="-Wl,-rpath /usr/local/lib"  
RUN make  
RUN make altinstall  
RUN ln -s /usr/local/bin/python2.7 /usr/local/bin/python  
  
WORKDIR /root  
RUN wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py  
RUN python ez_setup.py  
RUN easy_install pip  

