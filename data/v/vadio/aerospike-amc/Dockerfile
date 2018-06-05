#  
# Aerospike AMC Dockerfile  
#  
# http://github.com/vadio/aerospike-amc.docker  
#  
FROM ubuntu:trusty  
  
ENV AEROSPIKE_AMC_VERSION 3.6.11  
# Work from /aerospike  
WORKDIR /aerospike  
  
# Install Aerospike  
RUN \  
apt-get update -y \  
&& apt-get install -y python wget ca-certificates python-dev python-setuptools
\  
&& wget "http://artifacts.aerospike.com/aerospike-amc-
community/${AEROSPIKE_AMC_VERSION}/aerospike-amc-
community-${AEROSPIKE_AMC_VERSION}.all.x86_64.deb" -O aerospike-amc.deb \  
&& apt-get purge -y --auto-remove wget ca-certificates \  
&& dpkg -i aerospike-amc.deb \  
&& rm aerospike-amc.deb  
  
CMD [ "/opt/amc/bin/gunicorn", "--config",
"/etc/amc/config/gunicorn_config.py", "flaskapp:app" ]  

