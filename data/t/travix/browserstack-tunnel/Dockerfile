FROM travix/base-debian  
  
MAINTAINER Travix  
  
RUN curl -o browserstack.zip https://www.browserstack.com/browserstack-
local/BrowserStackLocal-linux-x64.zip && \  
unzip browserstack.zip && \  
rm browserstack.zip && \  
chmod +x BrowserStackLocal && \  
mv BrowserStackLocal /usr/local/bin/  
  
ENTRYPOINT ["/usr/local/bin/BrowserStackLocal"]  

