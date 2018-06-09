FROM pataquets/tor  
  
RUN \  
cat /etc/tor/conf-available/common/* | tee -a /etc/tor/torrc && \  
cat /etc/tor/conf-available/client/AllowDotExit | tee -a /etc/tor/torrc && \  
cat /etc/tor/conf-available/client/AllowSingleHopCircuits | tee -a
/etc/tor/torrc && \  
cat /etc/tor/conf-available/client/DNSPort | tee -a /etc/tor/torrc && \  
cat /etc/tor/conf-available/client/ExcludeSingleHopRelays | tee -a
/etc/tor/torrc && \  
cat /etc/tor/conf-available/client/EnforceDistinctSubnets | tee -a
/etc/tor/torrc && \  
cat /etc/tor/conf-available/client/SocksPort | tee -a /etc/tor/torrc && \  
cat /etc/tor/conf-available/directory/DirPort | tee -a /etc/tor/torrc && \  
cat /etc/tor/conf-available/relay/AllowSingleHopExits-On | tee -a
/etc/tor/torrc && \  
cat /etc/tor/conf-available/relay/ExitPolicy-RejectAll | tee -a /etc/tor/torrc
&& \  
cat /etc/tor/conf-available/relay/ExitRelay-Off | tee -a /etc/tor/torrc && \  
cat /etc/tor/conf-available/relay/ORPort | tee -a /etc/tor/torrc  

