FROM openjdk:8-jre  
ENV IPS_VERSION="5.25-64.0" PATH="/opt/interproscan:${PATH}"  
RUN apt-get update && \  
apt-get install -y python && \  
wget -e dotbytes=1M
"http://ftp.ebi.ac.uk/pub/software/unix/iprscan/5/${IPS_VERSION}/interproscan-${IPS_VERSION}-64-bit.tar.gz"
-O /root/interproscan.tar.gz && \  
tar xf /root/interproscan.tar.gz --exclude data -C /root/ && \  
mv /root/interproscan-${IPS_VERSION}/ /opt/interproscan && \  
ln -s /var/spool/cwl/interproscan-data-${IPS_VERSION}/ /opt/interproscan/data
&& \  
mkdir -p /opt/interproscan/.interproscan-5/ && \  
chmod go+rx /opt/interproscan/.interproscan-5/ && \  
ln -s /var/spool/cwl/interproscan.properties
/opt/interproscan/.interproscan-5/interproscan.properties && \  
rm -r /root/interproscan* && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

