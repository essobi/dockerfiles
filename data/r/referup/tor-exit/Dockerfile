FROM pataquets/tor  
  
RUN \  
cat /etc/tor/conf-available/common/* | tee -a /etc/tor/torrc && \  
cat /etc/tor/conf-available/relay/AllowSingleHopExits-On | tee -a
/etc/tor/torrc && \  
cat /etc/tor/conf-available/relay/ExitRelay-On | tee -a /etc/tor/torrc && \  
cat /etc/tor/conf-available/relay/ExitPolicy-Web | tee -a /etc/tor/torrc && \  
cat /etc/tor/conf-available/relay/ORPort | tee -a /etc/tor/torrc && \  
cat /etc/tor/conf-available/relay/PublishServerDescriptor-Off | tee -a
/etc/tor/torrc  

