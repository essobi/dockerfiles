FROM postgres:9.4  
  
RUN apt-get update && apt-get install -y python-pip python-dev lzop pv
daemontools  
RUN pip install wal-e  
RUN pip install -U requests six  
  
RUN chmod a+xr -R /usr/local/lib/python2.7/dist-packages/requests*  
RUN chmod a+xr -R /usr/local/lib/python2.7/dist-packages/six*  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD fix-acl.sh /docker-entrypoint-initdb.d/  
ADD setup-wale.sh /docker-entrypoint-initdb.d/  

