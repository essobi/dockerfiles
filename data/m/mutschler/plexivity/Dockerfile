FROM ubuntu:latest  
MAINTAINER Raphael Mutschler <https://github.com/mutschler>  
  
# Do updates  
RUN apt-get update && apt-get upgrade -y && apt-get install -y python \  
python-dev \  
python-distribute \  
python-pip \  
build-essential \  
git \  
supervisor  
  
# Get source  
RUN git clone https://github.com/mutschler/plexivity.git  
  
# Install dependency  
RUN pip install -r plexivity/requirements.txt  
  
# default port for plexivity  
EXPOSE 8080  
# Supervisor will watch the sickbeard process and restart it after updates  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
CMD ["/usr/bin/supervisord"]  

