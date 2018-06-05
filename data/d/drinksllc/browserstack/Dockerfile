FROM ubuntu:16.04  
RUN apt-get update && \  
apt-get install -y --no-install-recommends wget unzip ca-certificates && \  
rm -rf /var/lib/apt/lists/*  
  
RUN wget -O /tmp/BrowserStackLocal-linux-x64.zip
https://www.browserstack.com/browserstack-local/BrowserStackLocal-
linux-x64.zip && \  
/usr/bin/unzip /tmp/BrowserStackLocal-linux-x64.zip -d /usr/local/bin/ && \  
rm -f /tmp/BrowserStackLocal-linux-x64.zip  
  
CMD /usr/local/bin/BrowserStackLocal ${ARGS:--v} ${KEY}  

