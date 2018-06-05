# Base docker image  
FROM ubuntu:rolling  
#FROM tsslab/firefox:latest  
MAINTAINER Timophey Smetanko <ts@tsslab.xyz>  
  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
RUN apt-get update && apt-get install -y firefox wget xz-utils chromium-
browser  
RUN wget https://www.torproject.org/dist/torbrowser/7.0.8/tor-browser-
linux64-7.0.8_en-US.tar.xz -O /tmp/tor-browser.tar.xz  
RUN tar -xf /tmp/tor-browser.tar.xz -C /opt  
RUN mv /opt/tor-browser* /opt/tor-browser  
  
RUN useradd -G audio,video -m -s /bin/bash browser  
RUN chown browser -R /opt/tor-browser  
# Autorun chrome  
USER browser  
ENTRYPOINT [ "/entrypoint.sh" ]  

