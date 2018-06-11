FROM mdillon/postgis:9.4  
MAINTAINER Kelvin Nicholson  
  
RUN apt-get update && apt-get install -y python-dev lzop pv daemontools curl
build-essential  
RUN curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py
| python  
RUN pip install wal-e  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD fix-acl.sh /docker-entrypoint-initdb.d/  
ADD setup-wale.sh /docker-entrypoint-initdb.d/  
ADD additional-tweaks.sh /docker-entrypoint-initdb.d/  

