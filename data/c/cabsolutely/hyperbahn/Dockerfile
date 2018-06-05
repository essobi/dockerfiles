FROM node:0.10.46  
WORKDIR /usr/src/  
RUN git clone https://github.com/uber/hyperbahn && cd hyperbahn && git
checkout tags/v2.17.3 && npm install  
COPY local.json.tpl /tmp/local.json.tpl  
COPY entrypoint.sh /usr/src/hyperbahn/entrypoint.sh  
RUN cd hyperbahn && chmod +x entrypoint.sh  
WORKDIR /usr/src/hyperbahn  
  
ENV NODE_ENV=production  
  
COPY production.json.tpl /tmp/production.json.tpl  
  
CMD [ "./entrypoint.sh"]

