FROM codenvy/debian_jre  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN sudo apt-get update && sudo apt-get install -y \  
nano \  
curl && \  
curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash - && \  
sudo apt-get -y install nodejs && \  
sudo apt-get -y install build-essential && \  
sudo apt-get -y clean && \  
sudo apt-get -y autoremove && \  
sudo apt-get -y clean && \  
sudo rm -rf /var/lib/apt/lists/*  
  
LABEL che:server:3000:ref=nodejs che:server:3000:protocol=http  
  
EXPOSE 3000  
WORKDIR /projects  
  
CMD tail -f /dev/null  

