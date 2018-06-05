##  
#  
# Dockerfile for Aerospike Server v 3.6.3  
#  
##  
FROM sunnybhanot/ubuntu  
  
# Version  
ENV AEROSPIKE_VERSION 3.6.3  
ENV AEROSPIKE_TOOLS_VERSION 3.6.3  
# Install  
RUN apt-get update -y \  
&& apt-get install -y python-dev wget logrotate ca-certificates \  
&& wget "https://www.aerospike.com/artifacts/aerospike-server-
community/${AEROSPIKE_VERSION}/aerospike-server-
community-${AEROSPIKE_VERSION}-ubuntu12.04.tgz" -O aerospike-server.tgz \  
&& mkdir aerospike \  
&& tar xzf aerospike-server.tgz --strip-components=1 -C aerospike \  
&& dpkg -i aerospike/aerospike-server-*.deb \  
&& rm -rf aerospike-server.tgz aerospike \  
&& wget "http://www.aerospike.com/artifacts/aerospike-
tools/${AEROSPIKE_TOOLS_VERSION}/aerospike-
tools-${AEROSPIKE_TOOLS_VERSION}-ubuntu12.04.tgz" -O aerospike-tools.tgz \  
&& mkdir aerospike_tools \  
&& tar xzf aerospike-tools.tgz --strip-components=1 -C aerospike_tools \  
&& dpkg -i aerospike_tools/aerospike-tools-*.deb \  
&& rm -rf aerospike-tools.tgz aerospike_tools \  
&& apt-get purge -y --auto-remove wget ca-certificates \  
&& rm -rf /var/lib/apt/lists/*  
  
# Add Configuration Files  
ADD config/aerospike/aerospike.conf /etc/aerospike/aerospike.conf  
  
# Mount Folder  
VOLUME ["/opt/aerospike/data"]  
  
# Export Ports  
EXPOSE 3000 3001 3002 3003  
# Default Command  
CMD ["/usr/bin/asd","--foreground"]  

