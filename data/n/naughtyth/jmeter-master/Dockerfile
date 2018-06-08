FROM naughtyth/jmeter-base  
  
  
CMD jmeter -n -t /files/test.jmx -l /files/results.csv -j /files/jmeter.log
-R$IPSLAVES  
  
# Ports to be exposed from the container for JMeter Master  
EXPOSE 60000  

