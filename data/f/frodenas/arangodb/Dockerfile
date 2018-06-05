FROM frodenas/ubuntu  
MAINTAINER Ferran Rodenas <frodenas@gmail.com>  
  
# Install and configure ArangoDB 2.2  
RUN DEBIAN_FRONTEND=noninteractive && \  
cd /tmp && \  
wget https://www.arangodb.org/repositories/arangodb2/xUbuntu_14.04/Release.key
&& \  
apt-key add - < Release.key && \  
echo 'deb https://www.arangodb.org/repositories/arangodb2/xUbuntu_14.04/ /' >>
/etc/apt/sources.list.d/arangodb.list && \  
apt-get update && \  
apt-get install -y --force-yes arangodb=2.2.7 && \  
service arangodb stop && \  
sed -e 's/^directory = .*$/directory = \/data\/databases/' -i
/etc/arangodb/arangod.conf && \  
sed -e 's/^app-path = .*$/app-path = \/data\/apps/' -i
/etc/arangodb/arangod.conf && \  
sed -e 's/^data-path = .*$/data-path = \/data\/cluster/' -i
/etc/arangodb/arangod.conf && \  
sed -e 's/^disable-authentication = .*$/disable-authentication = no/' -i
/etc/arangodb/arangod.conf && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Add scripts  
ADD scripts /scripts  
RUN chmod +x /scripts/*.sh  
RUN touch /.firstrun  
  
# Command to run  
ENTRYPOINT ["/scripts/run.sh"]  
CMD [""]  
  
# Expose listen port  
EXPOSE 8529  
# Expose our data, logs and configuration volumes  
VOLUME ["/data", "/var/log/arangodb", "/etc/arangodb"]  

