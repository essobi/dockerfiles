# we shall start from ubuntu 12.04 LTS  
FROM ubuntu:12.04  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
RUN apt-get update  
  
# compilers and basic tools  
RUN apt-get install -y wget build-essential openssl libssl-dev  
  
# sqlite for python  
RUN apt-get install -y libsqlite3-dev  
RUN apt-get install -y sqlite3  
RUN apt-get install -y bzip2 libbz2-dev  
  
# python 3.3  
RUN (cd /opt && wget http://python.org/ftp/python/3.3.2/Python-3.3.2.tar.bz2)  
RUN tar jxf /opt/Python-3.3.2.tar.bz2 -C /opt  
RUN (cd /opt/Python-3.3.2 && ./configure --prefix=/usr/local \--enable-shared)  
RUN (cd /opt/Python-3.3.2 && make && make install)  
  
# make symlink  
#RUN ln -s /opt/python3.3/bin/python3.3 /usr/local/bin/python3.3  
RUN (echo '/usr/local/lib' >> /etc/ld.so.conf && ldconfig)  
  
# cleanup  
RUN (cd /opt && rm -R Python-*)  
  
# pip  
RUN (cd /opt && wget http://python-distribute.org/distribute_setup.py)  
RUN python3.3 /opt/distribute_setup.py  
  
# cleanup  
RUN (cd /opt && rm distribute*)  
  
# now install pip for real  
RUN (cd /usr/local/bin && ./easy_install-3.3 pip)

