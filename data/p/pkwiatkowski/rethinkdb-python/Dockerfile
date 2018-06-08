#  
# RethinkDB Dockerfile  
#  
# https://github.com/dockerfile/rethinkdb  
#  
# Pull base image.  
FROM cern/cc7-base  
  
# Install RethinkDB.  
RUN yum -y update  
RUN yum -y install wget git sudo make gcc gcc-c++ tar curl bzip2 python
python-devel \  
python-pip python-lxml libxslt-dev libmysqlclient-dev mysql-devel  
RUN wget http://download.rethinkdb.com/centos/7/`uname -m`/rethinkdb.repo \  
-O /etc/yum.repos.d/rethinkdb.repo  
RUN yum -y install rethinkdb  
  
# Install python driver for rethinkdb  
RUN pip install rethinkdb  
  
# Define mountable directories.  
VOLUME ["/data"]  
  
# Define working directory.  
WORKDIR /data  
  
# Define default command.  
CMD ["rethinkdb", "--bind", "all"]  
RUN rethinkdb --bind all &  
  
# Expose ports.  
# - 8080: web UI  
# - 28015: process  
# - 29015: cluster  
EXPOSE 8080  
EXPOSE 28015  
EXPOSE 29015  

