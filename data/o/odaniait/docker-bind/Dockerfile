FROM odaniait/docker-base:latest  
MAINTAINER Mike Petersen <mike@odania-it.de>  
  
RUN apt-get update && apt-get install -y bind9 dnsutils \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Setup service  
RUN mkdir -p /etc/service/bind  
COPY runit/bind.sh /etc/service/bind/run  
  
COPY . /srv/bind  
WORKDIR /srv/bind  
RUN bundle install  
  
RUN mkdir -p /srv/data && chown -R bind:bind /srv/data  
COPY templates/named.conf.options /etc/bind/named.conf.options  
  
ENV COPY_REFERENCE_FILE_LOG /srv/data/copy_reference_file.log  
VOLUME '/srv/data' '/srv/bind'  
EXPOSE 53/udp 53/tcp  

