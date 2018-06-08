FROM node:slim  
  
RUN npm install --global gatsby-cli && \  
apt-get update && \  
apt-get install entr libpng-dev make g++ python -y && \  
# Clean  
apt-get autoclean -y && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
mkdir -p /site  
  
WORKDIR /site  
VOLUME ["/site", "/site/content", "/public"]  
EXPOSE 8000  
COPY scripts/*.sh /  
  
ENTRYPOINT ["bash", "/entry.sh"]  

