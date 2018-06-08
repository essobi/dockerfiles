FROM mustardgrain/base:latest  
  
MAINTAINER Kirk True <kirk@mustardgrain.com>  
  
CMD ["/sbin/my_init"]  
  
RUN \  
apt-get update ; \  
apt-get install -y gearman-job-server  
  
COPY . /src  
  
RUN mkdir -p /etc/service/gearman-server && cp /src/run /etc/service/gearman-
server/run  
  
EXPOSE 4730  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

