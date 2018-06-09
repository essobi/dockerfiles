FROM pataquets/tor-client  
  
ADD Bridges /etc/tor/conf-available/client/  
  
RUN \  
cat /etc/tor/conf-available/debug/SafeLogging-Off | tee -a /etc/tor/torrc && \  
cat /etc/tor/conf-available/client/AllowDotExit | tee -a /etc/tor/torrc && \  
cat /etc/tor/conf-available/client/AllowSingleHopCircuits | tee -a
/etc/tor/torrc && \  
cat /etc/tor/conf-available/client/Bridges | tee -a /etc/tor/torrc && \  
cat /etc/tor/conf-available/client/EnforceDistinctSubnets-Off | tee -a
/etc/tor/torrc && \  
cat /etc/tor/conf-available/client/ExcludeSingleHopRelays | tee -a
/etc/tor/torrc && \  
cat /etc/tor/conf-available/client/MaxCircuitDirtiness-24h | tee -a
/etc/tor/torrc  

