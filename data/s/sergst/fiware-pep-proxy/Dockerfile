FROM ubuntu:16.04  
MAINTAINER FIWARE Wilma PEP Proxy Team. DIT-UPM  
  
WORKDIR /opt  
  
# Install Ubuntu dependencies  
RUN apt-get update && \  
apt-get install build-essential ca-certificates curl git netcat software-
properties-common python-software-properties -y --no-install-recommends && \  
rm -rf /var/lib/apt/lists/*  
  
# Install PPA  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && \  
apt-get install -y nodejs && \  
rm -rf /var/lib/apt/lists/*  
  
# Download latest version of the code and install npm dependencies  
RUN git clone -b entrypoint https://github.com/sstopkin/fiware-pep-proxy.git
&& \  
cd fiware-pep-proxy && \  
npm install  
  
# Change Workdir  
WORKDIR /opt/fiware-pep-proxy  
  
COPY entrypoint-common.sh /opt/fiware-pep-proxy/entrypoint-common.sh  
COPY docker-entrypoint.sh /opt/fiware-pep-proxy/docker-entrypoint.sh  
RUN chmod 755 docker-entrypoint.sh  
  
# Run PEP Proxy  
ENTRYPOINT ["/opt/fiware-pep-proxy/docker-entrypoint.sh"]  

