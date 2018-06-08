FROM davidkarlsen/docker-java:8u151  
ARG VERSION=2.14.1  
RUN wget https://s3-us-west-2.amazonaws.com/opsgeniedownloads/repo/opsgenie-
icinga2_${VERSION}_all.deb -O /tmp/marid.dpkg && \  
dpkg -i /tmp/marid.dpkg && \  
rm /tmp/marid.dpkg && \  
mkdir -p /var/log/opsgenie/marid && \  
chown -R opsgenie:opsgenie /var/log/opsgenie && \  
apt update && apt -y install net-tools netcat vim && apt -y clean  
COPY run.sh /  
COPY log.properties /etc/opsgenie/marid/log.properties  
CMD /run.sh  

