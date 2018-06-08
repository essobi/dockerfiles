# See https://github.com/lomadi/app-imdb  
FROM centos  
MAINTAINER lomadi <lomadi@mac.com>  
  
RUN yum install -y gcc python python-devel openssl-devel libxml2-devel
libxslt-devel zlib-devel MySQL-python python-setuptools python-pip  
RUN easy_install -U SQLObject  
RUN yum install -y wget  
  
WORKDIR /opt  
RUN wget http://prdownloads.sourceforge.net/imdbpy/IMDbPY-4.9.tar.gz  
  
RUN tar -xzf IMDbPY-4.9.tar.gz  
  
WORKDIR /opt/IMDbPY-4.9  
RUN python setup.py install  

