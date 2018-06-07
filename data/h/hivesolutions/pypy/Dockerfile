FROM pypy:2  
  
LABEL version="1.0"  
LABEL maintainer="Hive Solutions <development@hive.pt>"  
  
RUN if [ -e /usr/bin/python ]; then mv /usr/bin/python /usr/bin/python.old; fi
&&\  
if [ -e /usr/bin/pip ]; then mv /usr/bin/pip /usr/bin/pip.old; fi &&\  
ln -s /usr/local/bin/pypy /usr/bin/python &&\  
ln -s /usr/local/bin/pip /usr/bin/pip  

