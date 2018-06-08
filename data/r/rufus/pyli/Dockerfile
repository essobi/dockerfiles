FROM ubuntu:14.04  
RUN apt-get update; apt-get install -y python python-pip wget python-dev
libmysqlclient-dev libpq-dev git mercurial  
ADD / licensefu  
WORKDIR licensefu  
ENTRYPOINT ["/bin/bash","./pyli.sh"]  

