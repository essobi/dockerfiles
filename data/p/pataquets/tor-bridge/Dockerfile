FROM pataquets/tor  
  
RUN \  
cat /etc/tor/conf-available/common/* | tee -a /etc/tor/torrc && \  
cat /etc/tor/conf-available/client/SocksPort-Disable | tee -a /etc/tor/torrc
&& \  
cat /etc/tor/conf-available/relay/BridgeRelay-On | tee -a /etc/tor/torrc && \  
cat /etc/tor/conf-available/relay/ExitPolicy-RejectAll | tee -a /etc/tor/torrc
&& \  
cat /etc/tor/conf-available/relay/ORPort | tee -a /etc/tor/torrc && \  
cat /etc/tor/conf-available/relay/ORPort-443 | tee -a /etc/tor/torrc  

