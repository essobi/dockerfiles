# Copyright (c) 2013 theo crevon  
#  
# See the file LICENSE for copying permission.  
FROM ubuntu:14.04  
MAINTAINER tcrevon@gmail.com  
  
# make sure the package repository is up to date  
RUN apt-get update  
  
# Install dependencies  
RUN apt-get install -y libc6-dev build-essential pkg-config  
RUN apt-get install -y sqlite3 fabric  
RUN apt-get install -y python-dev python-pip python-setuptools python-
virtualenv  
  
# Configure a localshop user  
# Prepare user and directories  
RUN addgroup --system localshop  
RUN adduser --system --shell /bin/bash --gecos 'localshop operator' \--uid
4000 --disabled-password --home /home/localshop localshop  
RUN adduser localshop localshop  
  
# Create it's virtualenv  
RUN virtualenv /home/localshop/venv  
RUN mkdir /home/localshop/.localshop  
RUN chown -R localshop:localshop /home/localshop  
RUN chmod -R 775 /home/localshop  
  
# Set up environement variables for proper setup  
ENV HOME /home/localshop  
  
# Proceed to installation and initialisation  
ADD ./context /home/localshop/  
ADD ./fabfile /home/localshop/fabfile  
RUN cd /home/localshop && fab localshop_install  
RUN cd /home/localshop && fab localshop_init  
  
# Ensure localshop sources directory is writable  
RUN mkdir /home/localshop/source  
RUN chown -R localshop:localshop /home/localshop/source  
RUN chmod -R 775 /home/localshop/source  
  
# Ensure localshop db is in read-write mode  
RUN chown localshop:localshop /home/localshop/.localshop/localshop.db  
RUN chmod 775 /home/localshop/.localshop/localshop.db  
  
#Forward ports  
EXPOSE 8000  
# Let's run that shit  
CMD ["su", "localshop", "-c", "source /home/localshop/venv/bin/activate &&
localshop run_gunicorn 0.0.0.0:8000 & localshop celeryd -B -E"]  
  

