FROM centurylink/mysql:latest  
MAINTAINER lec00q  
  
RUN apt-get update  
RUN apt-get install -y python-dev python-pip python-mysqldb  
  
COPY my.cnf /etc/mysql/conf.d/my.cnf  
COPY requirements.txt /tmp/requirements.txt  
RUN pip install -r /tmp/requirements.txt  
  
# Clean up when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/tmp/requirements.txt  
  
RUN mkdir -p /tmp/db  
WORKDIR /tmp/db  

