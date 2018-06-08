FROM odaniait/docker-varnish:latest  
MAINTAINER Mike Petersen <mike@odania-it.de>  
  
# install dependencies  
RUN apt-get update && \  
apt-get install -y bundler libxml2-dev && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY docker/varnish.sh /varnish.sh  
  
RUN mkdir -p /srv/odania  
COPY . /srv/odania  
WORKDIR /srv/odania  
RUN bundle install  
  
VOLUME ["/srv/odania"]  
  
ENV OUT_DIR /etc/varnish  

