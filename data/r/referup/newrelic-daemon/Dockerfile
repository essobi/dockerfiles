FROM pataquets/newrelic-daemon  
  
RUN \  
mkdir -vp /tmp/newrelic && \  
chmod -v 1777 /tmp/newrelic  
  
CMD [ "--port", "/tmp/newrelic/.newrelic.sock" ]  

