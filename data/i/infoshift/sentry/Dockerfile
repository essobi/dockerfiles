FROM ubuntu:14.04  
MAINTAINER Jesse Panganiban <jesse.panganiban@infoshiftinc.com>  
  
# Install dependencies  
RUN apt-get update && \  
apt-get install -y \  
python-dev \  
python-pip \  
libmysqlclient-dev  
  
# Install sentry and deps  
ADD requirements.txt /opt/requirements.txt  
RUN pip install -r /opt/requirements.txt  
  
# Mount sentry configuration into the container.  
VOLUME ["/etc/sentry.conf.py"]  
  
# Expose the port sentry will run  
EXPOSE 9000  
# Default cmd  
CMD ["sentry", "--config=/etc/sentry.conf.py", "start"]  

