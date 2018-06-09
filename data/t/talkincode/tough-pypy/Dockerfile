FROM talkincode/pypy  
MAINTAINER jamiesun <jamiesun.net@gmail.com>  
  
RUN apt-get update -y && \  
apt-get install -y mysql-client libmysqlclient-dev libzmq-dev redis-server &&
\  
rm -rf /var/lib/apt/lists/*  
  
RUN pypy -m pip install --upgrade pip  
RUN pypy -m pip install bottle  
RUN pypy -m pip install Mako  
RUN pypy -m pip install Beaker  
RUN pypy -m pip install MarkupSafe  
RUN pypy -m pip install PyYAML  
RUN pypy -m pip install Twisted  
RUN pypy -m pip install treq  
RUN pypy -m pip install tablib  
RUN pypy -m pip install cyclone  
RUN pypy -m pip install six  
RUN pypy -m pip install autobahn  
RUN pypy -m pip install pycrypto  
RUN pypy -m pip install pyOpenSSL>=0.14  
RUN pypy -m pip install service_identity  
RUN pypy -m pip install MySQL-python  
RUN pypy -m pip install SQLAlchemy  
RUN pypy -m pip install pyzmq  
RUN pypy -m pip install txzmq  
RUN pypy -m pip install redis  
RUN pypy -m pip install msgpack-python  
RUN pypy -m pip install python-memcached  
RUN pypy -m pip install psutil  
RUN pypy -m pip install IPy  
RUN pypy -m pip install evernote  
  

