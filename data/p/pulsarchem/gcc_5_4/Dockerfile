FROM pulsarchem/pulsar-common  
MAINTAINER Pulsar-Chem  
RUN apt-get update && apt-get install -y gcc \  
libblas-dev \  
liblapack-dev  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

