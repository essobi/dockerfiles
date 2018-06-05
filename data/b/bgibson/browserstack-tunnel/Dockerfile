FROM ubuntu  
MAINTAINER Bryce Gibson "bryce.gibson@unico.com.au"  
# make sure the package repository is up to date  
RUN apt-get update && apt-get upgrade -y && apt-get install -y wget unzip  
RUN cd /usr/local/bin; wget https://www.browserstack.com/browserstack-
local/BrowserStackLocal-linux-x64.zip && unzip BrowserStackLocal-linux-x64.zip
&& chmod +x BrowserStackLocal && rm BrowserStackLocal-linux-x64.zip  
  
CMD /usr/local/bin/BrowserStackLocal ${ARGS:--v} ${KEY}  

