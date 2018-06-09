FROM amd64/node:latest  
  
LABEL maintainer="Florian JUDITH <florian.judith.b@gmail.com"  
  
RUN npm install mqtt  
  
ENV
SCRIPT_URL="https://gist.githubusercontent.com/ashvayka/13ee855a1a551f4f6c24adafc834cfaa/raw/635408f6d837d742f33bc23a89b48cd5b822b103/demo-
tool.js"  
RUN mkdir -p /usr/share/thingsboard  
  
COPY /docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
  
WORKDIR /usr/share/thingsboard  
  
USER root  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["node","/usr/share/thingsboard/demo-tools.js"]

