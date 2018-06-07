FROM pataquets/tor  
  
RUN \  
cat /etc/tor/conf-available/common/* | tee -a /etc/tor/torrc && \  
cat /etc/tor/conf-available/hidden-service/HiddenServiceDir | tee -a
/etc/tor/torrc && \  
cat /etc/tor/conf-available/hidden-service/HiddenService-http | tee -a
/etc/tor/torrc  

