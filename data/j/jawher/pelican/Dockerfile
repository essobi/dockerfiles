FROM debian:jessie  
  
MAINTAINER jawher  
  
RUN apt-get update && \  
apt-get -y dist-upgrade && \  
apt-get install -y git python-pip graphviz && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY requirements.txt /tmp/  
  
RUN pip install -r /tmp/requirements.txt && rm /tmp/requirements.txt  
  
WORKDIR /blog  
  
ENTRYPOINT ["/usr/bin/make"]  
  
CMD ["html"]  
  
EXPOSE 8000  

