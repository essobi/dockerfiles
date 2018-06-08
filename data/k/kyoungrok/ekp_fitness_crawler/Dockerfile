FROM python:2.7  
# install arangoDB client and other packages  
RUN wget
http://www.arangodb.com/repositories/arangodb31/Debian_8.0/Release.key && \  
apt-key add - < Release.key && \  
echo 'deb http://www.arangodb.com/repositories/arangodb31/Debian_8.0/ /' | tee
/etc/apt/sources.list.d/arangodb.list && \  
apt-get update && \  
apt-get install -y arangodb3-client=3.1.0 \  
supervisor \  
cron && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY crawler/ /crawler  
COPY run.sh /run.sh  
COPY wait-for-it.sh /wait-for-it.sh  
  
WORKDIR /crawler  
  
RUN chmod -R +x /crawler && \  
chmod +x /run.sh && \  
chmod +x /wait-for-it.sh && \  
pip install -r requirements.txt  
  
CMD ["/run.sh"]

