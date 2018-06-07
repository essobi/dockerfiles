# Dockerfile for PRISONER  
# http://prisoner.cs.st-andrews.ac.uk  
# Version 0.2  
# Last updated June 23rd 2016  
FROM ubuntu  
MAINTAINER Luke Hutton <luke.hutton@open.ac.uk>  
LABEL Description="This image prepares a virtual environment with the
dependencies needed to execute a PRISONER instance"  
  
# creates a virtual environment for PRISONER  
RUN apt-get update && apt-get install -y python python-dev python-distribute
python-pip libxml2-dev libxslt1-dev zlib1g-dev vim sqlite3 libsqlite3-dev  
  
COPY ./ /usr/bin/prisoner/  
  
# install python requirements into this environment  
RUN pip install -r /usr/bin/prisoner/requirements.txt  
  
EXPOSE 5000  
CMD ["python","/usr/bin/prisoner/server/prisoner.wsgi"]  

