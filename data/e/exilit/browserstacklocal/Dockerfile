FROM debian:stable-slim  
  
ENV BROWSERSTACK_LOCAL_KEY=  
  
COPY ./entrypoint.sh /  
RUN ["chmod", "+x", "/entrypoint.sh"]  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y wget unzip  
  
RUN wget https://www.browserstack.com/browserstack-local/BrowserStackLocal-
linux-x64.zip && \  
unzip BrowserStackLocal-linux-x64.zip && \  
rm BrowserStackLocal-linux-x64.zip && \  
chmod +x BrowserStackLocal && \  
mv BrowserStackLocal /usr/local/bin  
  
ENTRYPOINT ["/entrypoint.sh"]  

