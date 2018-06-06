# based on https://github.com/arun-gupta/docker-images/tree/master/couchbase-
server  
FROM anduin/couchbase_server:4.5.1  
MAINTAINER Binh Nguyen "binhnguyen@anduintransact.com"  
RUN apt-get update -y \  
&& apt-get install -y --no-install-recommends \  
build-essential git rebar software-properties-common \  
python-software-properties supervisor  
  
##### supervisor  
# Configure  
RUN rm -rf /etc/supervisor  
ADD ./config/supervisord /etc/supervisor  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY configure-node.sh /opt/anduin/couchbase/  
  
CMD exec /opt/anduin/couchbase/configure-node.sh  

