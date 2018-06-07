FROM node:6.9.2-alpine  
  
RUN npm install -qg raml2html@~3.0 \  
&& npm cache clean  
  
RUN mkdir -p /data  
VOLUME /data  
WORKDIR /data  
  
ENTRYPOINT ["raml2html"]  
  
CMD ["--help"]  

