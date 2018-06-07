FROM node:latest  
  
RUN npm install -g mermaid phantomjs && npm cache clean  
  
WORKDIR /data  
  
ENTRYPOINT ["mermaid"]  
CMD ["--help"]  

