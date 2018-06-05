FROM debian:jessie-slim  
  
# Install  
RUN apt-get update -y \  
&& apt-get install -y wget \  
&& wget http://www.aerospike.com/download/amc/4.0.13/artifact/debian6 -O
/tmp/aerospike-amc-community.deb \  
&& dpkg -i /tmp/aerospike-amc-community.deb \  
&& apt-get purge -y --auto-remove  
  
# Export Ports  
EXPOSE 8081  
CMD /opt/amc/amc  
  

