FROM scrapybook/base  
  
COPY scripts /tmp/scripts  
  
# Enable scrapyd  
RUN mkdir -p /etc/service/scrapyd /etc/scrapyd/conf.d && \  
mv /tmp/scripts/scrapyd /etc/default/ && \  
mv /tmp/scripts/scrapyd.sh /etc/service/scrapyd/run && \  
mv /tmp/scripts/000-default /etc/scrapyd/conf.d/ && \  
rm -rf /tmp/scripts  
  
EXPOSE 6800  

