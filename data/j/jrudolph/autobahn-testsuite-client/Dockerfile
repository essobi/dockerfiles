FROM jrudolph/autobahn-testsuite  
  
MAINTAINER jrudolph  
  
ADD fuzzingclient.json /tmp/fuzzingclient.json  
  
VOLUME /tmp/server-report  
  
CMD wstest -m fuzzingclient  

