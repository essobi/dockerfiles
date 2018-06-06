# Need a debian sid for now to get decent version of couchdb  
FROM debian:sid  
MAINTAINER Rony Dray <contact@obigroup.fr>, Jonathan Dray
<jonathan.dray@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y update && apt-get install --quiet --assume-yes --no-install-
recommends \  
couchdb \  
&& apt-get clean  
  
# Clean APT cache for a lighter image  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Create Cozy users, without home directories  
# Create user early to avoid uid / gid issues  
RUN useradd -M cozy  
ADD local.ini /etc/couchdb/local.ini  
# Generate a random login and password for couchdb  
RUN mkdir /var/run/couchdb \  
&& chown -hR couchdb /var/run/couchdb /etc/couchdb/local.ini  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/couchdb/couchdb.log  
  
# Expose couch port to make it easier for other docker containers  
EXPOSE 5984  
VOLUME ["/var/lib/couchdb/"]  
  
# Setting config dir to couch main directory  
WORKDIR /var/lib/couchdb  
  
# Default user when running the container  
USER couchdb  
CMD ["/usr/bin/couchdb"]  

