FROM tutum/ubuntu:trusty  
  
MAINTAINER Michael Sevilla <mikesevilla3@gmail.com>  
  
RUN echo "===> Install the basics..." && \  
DEBIAN_FRONTEND=noninteractive apt-get update && \  
apt-get install -yq --force-yes collectl && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* tmp/* /var/tmp/*  
  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod 750 /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  

