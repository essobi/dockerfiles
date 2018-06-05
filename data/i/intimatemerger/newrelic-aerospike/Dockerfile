FROM java:openjdk-8-jre  
  
LABEL maintainer "mats116 <mats.kazuki@gmail.com>"  
  
ENV PREFIX=/opt/newrelic \  
DEFAULTUSER=newrelic  
  
RUN apt-get update && \  
apt-get install -y vim && \  
apt-get clean && \  
rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/* && \  
useradd --create-home --home-dir $PREFIX -s /bin/bash $DEFAULTUSER  
  
USER $DEFAULTUSER  
WORKDIR $PREFIX  
  
RUN yes | bash -c "$(curl -sSL
https://download.newrelic.com/npi/release/install-npi-linux-debian-x64.sh)" &&
\  
./npi fetch com.aerospike.newrelic.connector --yes  
  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ./npi start com.aerospike.newrelic.connector --foreground  

